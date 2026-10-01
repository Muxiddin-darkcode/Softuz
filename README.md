# 🚀 Dasturlar Telegram Boti

Ushbu bot kompyuter (Windows, macOS) va mobil qurilmalar (Android) uchun dasturlarni Telegram orqali tarqatish, qidirish va yuklab olish uchun mo'ljallangan professional yechimdir.

Fayllar server xotirasini to'ldirmasligi uchun Telegramning o'zidan bepul bulutli ombor (Cloud Storage) sifatida foydalaniladi. Ma'lumotlar bazasi sifatida **SQLite + SQLAlchemy 2.0 Async** ishlatilgan.

---

## 🌟 Imkoniyatlar

### 👤 Foydalanuvchi qismi:
* 🔍 **Aqlli qidiruv:** Dastur nomini yozib tezkor topish.
* 📂 **Kategoriyalar va OS filtr:** Windows, Android (APK), macOS, Linux va boshqa yo'nalishlar.
* 📄 **Sahifalash (Pagination):** Har sahifada 5 tadan dastur qulay navigatsiya bilan.
* 🖼 **Dastur kartochkasi:** Rasm/logo, versiya, hajm, arxiv paroli, tavsif, ko'rishlar va yuklab olishlar soni.
* ⬇️ **Tezkor yuklab olish:** 2 GB gacha bo'lgan dasturlarni to'g'ridan-to'g'ri Telegramdan yuklash.
* ⭐ **Saqlanganlar (Favorites):** Dasturlarni shaxsiy xatcho'pga saqlash.
* ⭐️ **Reyting tizimi:** Dasturlarga 1 dan 5 gacha baho berish.
* 💡 **Dastur buyurtma qilish:** Topilmagan dasturni adminga so'rov qilib yuborish.
* 🔗 **Deep-Linking:** Kanallarga `https://t.me/bot?start=prog_1` havolasini qo'yish imkoniyati.
* 📢 **Majburiy obuna:** Homiy kanallarga obuna bo'lguncha botni cheklash.

### 🛠 Admin paneli (`/admin`):
* ➕ **Dastur qo'shish (FSM):** Fayl, nom, versiya, OS, kategoriya, parol, tavsif va rasm yuklash.
* 📋 **Dasturlar boshqaruvi:** Dasturlarni ko'rish va o'chirish.
* 🗂 **Kategoriyalar boshqaruvi:** Yangi bo'limlar ochish va o'chirish.
* 📊 **Jonli statistika:** Jami va kunlik foydalanuvchilar, yuklab olishlar, eng ko'p yuklangan TOP dasturlar.
* 📢 **Xabar tarqatish (Broadcast):** Barcha a'zolarga progress-bar bilan reklama jo'natish.
* 📢 **Homiy kanallar:** Majburiy obuna kanallarini qo'shish va olib tashlash.
* 📩 **Buyurtmalar nazorati:** Foydalanuvchilar so'ragan dasturlarni ko'rish va tasdiqlash.
* 💾 **Baza zaxirasi (Backup):** Bitta bosish bilan `.sqlite3` bazani adminga yuklab berish.

---

## ⚙️ O'rnatish va Ishga Tushirish

### 1. `.env` faylini sozlash
Loyihaning ildiz papkasidagi `.env` faylini oching va o'z ma'lumotlaringizni kiriting:

```env
# @BotFather dan olingan bot tokeni
BOT_TOKEN=123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ_12345678

# Sizning shaxsiy Telegram ID raqamingiz (@userinfobot dan olishingiz mumkin)
ADMINS=123456789

# Dasturlar saqlanadigan Yopiq Arxiv Kanali ID si (masalan: -1001234567890)
# Bot ushbu kanalda administrator bo'lishi shart!
STORAGE_CHANNEL_ID=-1001234567890

# SQLite bazasi
DATABASE_URL=sqlite+aiosqlite:///data/bot_database.sqlite3
```

### 2. Yopiq Saqlash Kanalini sozlash (Telegram Cloud Storage)
1. Telegramda bitta yangi **Xususiy (Yopiq) Kanal** oching (masalan: `Dasturlar Ombori`).
2. Yaratgan botingizni ushbu kanalga **Administrator** qilib qo'shing (xabar yozish huquqi bilan).
3. Kanal ID raqamini oling (masalan, `@userinfobot` orqali kanaldan bitta xabarni forward qilib bilish mumkin) va uni `.env` dagi `STORAGE_CHANNEL_ID` ga yozing.

### 3. Botni ishga tushirish
Terminalda (PowerShell yoki CMD) quyidagi buyruqni bering:

```bash
.venv\Scripts\python run.py
```

---

## 📁 Loyiha Strukturasi

```
Dasturlar bot/
├── .env                  # Konfiguratsiya fayli
├── .env.example          # Shablon
├── requirements.txt      # Kutubxonalar
├── run.py                # Asosiy ishga tushiruvchi fayl
├── README.md             # Qo'llanma
├── data/
│   └── bot_database.sqlite3 # SQLite ma'lumotlar bazasi
└── app/
    ├── core/             # Konfiguratsiya va DB engine
    ├── database/         # Modellar va CRUD amallari
    ├── handlers/         # User va Admin komandalari
    ├── keyboards/        # Reply va Inline tugmalar
    ├── middlewares/      # Anti-flood va Majburiy obuna tekshiruvi
    └── utils/            # Formatlash va Sahifalash (Paginator)
```
