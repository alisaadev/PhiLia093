from system.core.context import MessageContext
from system.loader import PLUGINS


async def callback_router(update, ctx):
    query = update.callback_query
    await query.answer()

    m = MessageContext(update, ctx)
    await m.load_bot()
    await m.load_admin()
    cb_id = query.data

    for plugin in PLUGINS.values():
        callbacks = plugin.get("callbacks", {})
        if cb_id in callbacks:
            await callbacks[cb_id](query, m)
            return
