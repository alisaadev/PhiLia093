from system.core.context import MessageContext


async def Serialize(update, ctx):
    if not update.effective_message:
        return None
    return MessageContext(update, ctx)
    