"""
storage/database.py

Simple SQLite-based datas storage for Telegram bot.
- Persistent (restart-safe)
- Auto-init default value
- All values stored as STRING (best practice)

Cara pakai ada di bagian bawah file ini.
"""

import sqlite3
from pathlib import Path


DB_PATH = Path("storage/data.db")
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS datas (
    key TEXT PRIMARY KEY,
    value TEXT
)
""")
conn.commit()


def set_data(key: str, value):
    """
    Set / update data value.
    Value akan disimpan sebagai STRING.
    """
    cursor.execute(
        "REPLACE INTO datas (key, value) VALUES (?, ?)",
        (key, str(value))
    )
    conn.commit()


def get_data(key: str, default=None):
    """
    Get data value.
    Jika belum ada di DB, default akan:
    - dikembalikan
    - SEKALIGUS disimpan ke DB
    """
    cursor.execute("SELECT value FROM datas WHERE key=?", (key,))
    row = cursor.fetchone()

    if row:
        return row[0]

    # auto-init default
    set_data(key, default)
    return default


def get_bool(key: str, default=False) -> bool:
    """
    Ambil data sebagai boolean.
    """
    return get_data(key, str(default)).lower() == "true"


def get_int(key: str, default=0) -> int:
    """
    Ambil data sebagai integer.
    """
    try:
        return int(get_data(key, default))
    except (ValueError, TypeError):
        return default


def get_str(key: str, default="") -> str:
    """
    Ambil data sebagai string.
    """
    return str(get_data(key, default))



DEFAULT_dataS = {
    "public": "true",
    "prefix": "/"
}

#don't touch this
def init_datas():
    for key, value in DEFAULT_dataS.items():
        get_data(key, value)


# =========================================================
# ===================== CARA PAKAI =========================
# =========================================================
#
# Import di file mana pun (plugin / main / handler)
#   from storage.database import (
#       get_bool, get_int, get_str,
#       set_data, init_datas
#   )
#
# Ambil data
#   is_public = get_bool("public", True)
#   prefix = get_str("prefix", ".")
#
# Ubah data (misalnya di plugin option)
#   current = get_bool("public", True)
#   set_data("public", not current)
