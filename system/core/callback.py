from system.loader import PLUGINS


async def callback_router(update, ctx):
    query = update.callback_query
    await query.answer()

    cb_id = query.data

    for plugin in PLUGINS.values():
        callbacks = plugin.get("callbacks", {})
        if cb_id in callbacks:
            await callbacks[cb_id](query, ctx)
            return
