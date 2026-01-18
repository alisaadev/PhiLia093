from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters
)
from system.core.serialize import Serialize
from system.core.handler import handler
from system.watcher import start_watcher
from system.loader import load_plugins
from storage.config import BOT_TOKEN, OWNER_IDS


async def on_message(update, ctx: ContextTypes.DEFAULT_TYPE):
    m = await Serialize(update, ctx)
    if not m:
        return

    await handler(m)


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.bot_data["owners"] = OWNER_IDS

    load_plugins()
    start_watcher()

    app.add_handler(
        MessageHandler(filters.ALL, on_message)
    )

    print("🤖 Telegram bot running...")
    app.run_polling()


if __name__ == "__main__":
    main()
