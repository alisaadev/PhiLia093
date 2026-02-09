from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from storage.database import get_bool, set_data


async def run_option(m):
    keyboard = [
        [
            InlineKeyboardButton("Private", callback_data="private"),
            InlineKeyboardButton("Public", callback_data="public")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    mode = "𝗣𝘂𝗯𝗹𝗶𝗰" if get_bool("public") else "𝗣𝗿𝗶𝘃𝗮𝘁𝗲"

    await m.ctx.bot.send_message(
        chat_id=m.chat.id,
        text=f"Bot sedang dalam mode {mode}\npilih untuk mengubah mode:",
        reply_markup=reply_markup
    )

async def on_private(query, m):
    await query.edit_message_text("Sukses mengubah mode bot menjadi private")
    set_data("public", "false")

async def on_public(query, m):
    await query.edit_message_text("Sukses mengubah mode bot menjadi public")
    set_data("public", "true")
    

plugin = {
    "command": ["option"],
    "owner": True,

    "run": run_option,

    "callbacks": {
        "private": on_private,
        "public": on_public
    }
}