from typing import List
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.database.models import Category, Program

def get_admin_main_menu() -> InlineKeyboardMarkup:
    """Admin bosh paneli menyusi (rangli tugmalar bilan)."""
    keyboard = [
        [
            InlineKeyboardButton(text="➕ Dastur qo'shish", callback_data="admin_add_prog", style="success")
        ],
        [
            InlineKeyboardButton(text="📋 Dasturlar ro'yxati", callback_data="admin_prog_list_1", style="primary"),
            InlineKeyboardButton(text="🗂 Kategoriyalar", callback_data="admin_cats", style="primary")
        ],
        [
            InlineKeyboardButton(text="📊 To'liq statistika", callback_data="admin_stats", style="primary"),
            InlineKeyboardButton(text="📢 Xabar tarqatish", callback_data="admin_broadcast", style="primary")
        ],
        [
            InlineKeyboardButton(text="📢 Homiy kanallar", callback_data="admin_channels", style="primary"),
            InlineKeyboardButton(text="📩 Buyurtmalar", callback_data="admin_requests", style="primary")
        ],
        [
            InlineKeyboardButton(text="💾 Baza zaxirasi (.db)", callback_data="admin_backup", style="primary"),
            InlineKeyboardButton(text="🚪 Panelni yopish", callback_data="admin_close", style="danger")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_os_selection_keyboard() -> InlineKeyboardMarkup:
    """Dastur qo'shishda Operatsion Tizimni tanlash."""
    keyboard = [
        [
            InlineKeyboardButton(text="💻 Windows", callback_data="os_windows", style="primary"),
            InlineKeyboardButton(text="📱 Android (APK)", callback_data="os_android", style="primary")
        ],
        [
            InlineKeyboardButton(text="🍏 macOS", callback_data="os_macos", style="primary"),
            InlineKeyboardButton(text="🐧 Linux", callback_data="os_linux", style="primary")
        ],
        [
            InlineKeyboardButton(text="🌐 Boshqa", callback_data="os_other", style="primary"),
            InlineKeyboardButton(text="❌ Bekor qilish", callback_data="admin_cancel", style="danger")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_admin_categories_select_keyboard(categories: List[Category]) -> InlineKeyboardMarkup:
    """Dastur qo'shishda kategoriyani tanlash."""
    keyboard = []
    row = []
    for cat in categories:
        row.append(
            InlineKeyboardButton(
                text=f"{cat.icon} {cat.name}",
                callback_data=f"selcat_{cat.id}",
                style="primary"
            )
        )
        if len(row) == 2:
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)

    keyboard.append([
        InlineKeyboardButton(text="❌ Bekor qilish", callback_data="admin_cancel", style="danger")
    ])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def get_skip_or_cancel_keyboard(skip_cb: str = "skip_step") -> InlineKeyboardMarkup:
    """Ixtiyoriy qadamlar (masalan rasm yoki parol) uchun o'tkazib yuborish tugmasi."""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="⏭ O'tkazib yuborish", callback_data=skip_cb, style="primary")
            ],
            [
                InlineKeyboardButton(text="❌ Bekor qilish", callback_data="admin_cancel", style="danger")
            ]
        ]
    )

def get_confirm_program_upload_keyboard() -> InlineKeyboardMarkup:
    """Dasturni bazaga qo'shishni tasdiqlash."""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Tasdiqlash va chop etish", callback_data="confirm_upload", style="success")
            ],
            [
                InlineKeyboardButton(text="❌ Bekor qilish", callback_data="admin_cancel", style="danger")
            ]
        ]
    )

def get_manage_program_keyboard(program_id: int) -> InlineKeyboardMarkup:
    """Dasturni boshqarish (o'chirish) tugmalari."""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🗑 Dasturni o'chirish", callback_data=f"admin_del_prog_{program_id}", style="danger")
            ],
            [
                InlineKeyboardButton(text="🔙 Ro'yxatga qaytish", callback_data="admin_prog_list_1", style="primary")
            ]
        ]
    )

def get_request_actions_keyboard(request_id: int) -> InlineKeyboardMarkup:
    """Kelgan buyurtmani ko'rish va bajarish."""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Bajarildi deb belgilash", callback_data=f"req_done_{request_id}", style="success"),
                InlineKeyboardButton(text="❌ Rad etish", callback_data=f"req_reject_{request_id}", style="danger")
            ]
        ]
    )
