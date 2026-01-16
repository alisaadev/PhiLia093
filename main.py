# main.py (update)
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters
)
from core.serialize import Serialize
from core.handler import handler
from watcher import start_watcher
from loader import load_plugins
import config

BOT_TOKEN = "8240977347:AAHeNICTyHuugEDOf9xCeFN3OwUuQZK_4j4"


async def on_message(update, ctx: ContextTypes.DEFAULT_TYPE):
    m = await Serialize(update, ctx)
    if not m:
        return

    await handler(m)


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.bot_data["owners"] = config.OWNER_IDS

    load_plugins()
    start_watcher()

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, on_message)
    )

    print("🤖 Telegram bot running...")
    app.run_polling()


if __name__ == "__main__":
    main()
