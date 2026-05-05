# 🤖 Telegram Bot Framework (Migrated from WhatsApp)

Project ini adalah **framework bot Telegram berbasis Python** yang merupakan hasil **migrasi logic dari bot WhatsApp (Baileys / JavaScript)** ke Telegram.

Tujuan utama project ini:
- mempertahankan **arsitektur plugin system** seperti di bot WhatsApp
- membuat codebase lebih **bersih, modular, dan mudah di-maintain**
- memudahkan pengembangan lintas platform (WA → Telegram)

> ⚠️ Project ini **sementara ditinggalkan karna fokus ke project lain**.

---

## ✨ Fitur Utama

- 🔌 **Plugin System** (mirip handler.js di Baileys)
- 🔄 **Hot Reload Plugin** (tanpa restart bot)
- 🧠 **Message Abstraction (`m`)**
- 🔐 **Permission System (Owner / Group / Private)**
- 🛠️ **Eval & Exec (Owner Only)** untuk maintenance & debugging
- 🧼 Struktur kode **simple, bersih, dan scalable**

---

## 🚀 Cara Menjalankan Bot

### 1️⃣ Clone Repository
```bash
git clone https://github.com/alisaadev/PhiLia093
cd PhiLia093
```

### 2️⃣ Buat Virtual Environment (opsional)
```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
Minimal dependency:
- python-telegram-bot
- watchdog

### 4️⃣ Jalankan Bot
```bash
python -m system
```

---

## 🧪 Debug & Maintenance
Eval (Owner Only)
```
/eval return m.to_dict()
/eval return vars(m)
```

Exec (Owner Only)
```
/exec ls
/exec uptime
```

> ⚠️ Gunakan fitur ini dengan bijak dan hanya untuk owner.

---

## 🔄 Hot Reload Plugin
- Edit file di folder `plugins/`
- Simpan file
- Plugin akan **reload otomatis** tanpa restart bot

---

## 🚫 SCRIPT INI TIDAK UNTUK DIJUAL

Dilarang menjual ulang script ini dalam bentuk apa pun
Dilarang mengklaim sebagai karya pribadi tanpa kredit

Diperbolehkan untuk:
- belajar
- pengembangan pribadi
- modifikasi untuk penggunaan sendiri

Gunakan dengan **etika & tanggung jawab.**

---

## 🧩 Catatan

Project ini dibuat dengan tujuan **belajar, eksplorasi, dan peningkatan kualitas arsitektur bot,**
bukan sebagai produk komersial.

Jika kamu paham struktur ini, kamu bisa:
- port plugin WhatsApp > Telegram dengan mudah
- membuat bot Telegram yang scalable & maintainable

---
