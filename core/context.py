# core/context.py
from telegram import Update
from telegram.ext import ContextTypes


class MessageContext:
    def __init__(self, update: Update, ctx: ContextTypes.DEFAULT_TYPE):
        self.update = update
        self.ctx = ctx
        self.message = update.effective_message
        self.chat = update.effective_chat
        self.user = update.effective_user

        # BASIC
        self.body = self.message.text or ""
        self.prefix = "."
        self.command = ""
        self.args = []
        self.text = ""

        # FLAGS
        self.isGroup = self.chat.type in ("group", "supergroup")
        self.isPrivate = self.chat.type == "private"
        self.isOwner = self.user.id in ctx.bot_data.get("owners", [])

        # PARSE COMMAND
        self._parse_command()

        # QUOTED
        self.isQuoted = bool(self.message.reply_to_message)
        self.quoted = self._parse_quoted()

    def _parse_command(self):
        if not self.body.startswith(self.prefix):
            return

        parts = self.body[len(self.prefix):].strip().split()
        self.command = parts[0].lower() if parts else ""
        self.args = parts[1:]
        self.text = " ".join(self.args)

    def _parse_quoted(self):
        if not self.isQuoted:
            return None

        q = self.message.reply_to_message
        return {
            "body": q.text or "",
            "sender": q.from_user.id if q.from_user else None,
            "isMedia": bool(q.photo or q.video or q.document)
        }

    def to_dict(self):
        return {
            "body": self.body,
            "command": self.command,
            "args": self.args,
            "text": self.text,
            "isGroup": self.isGroup,
            "isOwner": self.isOwner,
            "chat_id": self.chat.id,
            "user_id": self.user.id,
            "username": self.user.username,
            "quoted": self.quoted
        }

    async def reply(self, text: str, **kwargs):
        return await self.message.reply_text(text, **kwargs)
