import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat

from app.core.config import settings
from app.core.database import engine, Base, async_session_maker
from app.database.repositories import seed_default_categories

# Middlewares
from app.middlewares.db_session import DatabaseSessionMiddleware
from app.middlewares.throttling import ThrottlingMiddleware
from app.middlewares.subscription import SubscriptionMiddleware

# Handlers
from app.handlers import common
from app.handlers.user import catalog, search, download, favorites, request_app
from app.handlers.admin import (
    admin_menu, add_program, manage_programs,
    categories, broadcast, channels, stats_backup
)

# Windows console UTF-8 qo'llab-quvvatlash
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Logging sozlamalari
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

async def setup_commands(bot: Bot):
    """Telegram menyusidagi standart buyruqlar."""
    # Barcha oddiy foydalanuvchilar menyusi (faqat /start)
    user_commands = [
        BotCommand(command="start", description="Botni qayta ishga tushirish")
    ]
    await bot.set_my_commands(user_commands, scope=BotCommandScopeDefault())

    # Faqat adminlar menyusi (/start va /admin)
    admin_commands = [
        BotCommand(command="start", description="Botni qayta ishga tushirish"),
        BotCommand(command="admin", description="Admin panel")
    ]
    for admin_id in settings.admin_ids:
        try:
            await bot.set_my_commands(admin_commands, scope=BotCommandScopeChat(chat_id=admin_id))
        except Exception as e:
            logger.warning(f"Admin {admin_id} uchun maxsus buyruqlarni o'rnatishda xatolik: {e}")

async def init_database():
    """Baza jadvallarini yaratish va boshlang'ich ma'lumotlarni kiritish."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("✅ Ma'lumotlar bazasi jadvallari muvaffaqiyatli tekshirildi/yaratildi.")

    # Boshlang'ich default kategoriyalarni kiritish
    async with async_session_maker() as session:
        await seed_default_categories(session)
    logger.info("✅ Standart kategoriyalar tekshirildi.")

async def main():
    logger.info("🚀 Dasturlar Telegram Boti ishga tushmoqda...")

    # Bazani ishga tushirish
    await init_database()

    # Bot va Dispatcher yaratish
    bot = Bot(token=settings.BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    # Middlewarelarni ro'yxatdan o'tkazish
    dp.update.outer_middleware(DatabaseSessionMiddleware())
    dp.message.middleware(ThrottlingMiddleware(limit=0.5))
    dp.callback_query.middleware(ThrottlingMiddleware(limit=0.5))
    dp.message.middleware(SubscriptionMiddleware())
    dp.callback_query.middleware(SubscriptionMiddleware())

    # Handler Routerlarini ulash
    # 1. Admin routerlari
    dp.include_router(admin_menu.router)
    dp.include_router(add_program.router)
    dp.include_router(manage_programs.router)
    dp.include_router(categories.router)
    dp.include_router(broadcast.router)
    dp.include_router(channels.router)
    dp.include_router(stats_backup.router)

    # 2. Foydalanuvchi routerlari
    dp.include_router(common.router)
    dp.include_router(catalog.router)
    dp.include_router(search.router)
    dp.include_router(download.router)
    dp.include_router(favorites.router)
    dp.include_router(request_app.router)

    # Buyruqlarni sozlash
    try:
        await setup_commands(bot)
    except Exception as e:
        logger.warning(f"Buyruqlarni o'rnatishda ogohlantirish (Token noto'g'ri bo'lishi mumkin): {e}")

    # Pollingni boshlash
    logger.info("🤖 Bot muvaffaqiyatli ishga tushdi va xabarlarni qabul qilishga tayyor!")
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()
        await engine.dispose()
        logger.info("🛑 Bot to'xtatildi.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot qo'lda to'xtatildi.")
