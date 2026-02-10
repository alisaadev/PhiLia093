from telegram.ext import (
    CallbackQueryHandler,
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters
)
from system.core.serialize import Serialize
from system.core.handler import handler
from system.core.callback import callback_router
from system.watcher import start_watcher
from system.loader import load_plugins
from system.bootstrap import bootstrap
from storage.database import init_datas

BOT_TOKEN, OWNER_IDS = bootstrap()


async def on_message(update, ctx: ContextTypes.DEFAULT_TYPE):
    m = await Serialize(update, ctx)
    if not m:
        return

    await handler(m)


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.bot_data["owners"] = OWNER_IDS

    init_datas()
    load_plugins()
    start_watcher()

    app.add_handler(MessageHandler(filters.ALL, on_message))
    app.add_handler(CallbackQueryHandler(callback_router))

    print("🤖 Telegram bot running...")
    app.run_polling()


if __name__ == "__main__":
    main()
