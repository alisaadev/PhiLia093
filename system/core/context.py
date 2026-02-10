from telegram import Update
from telegram.ext import ContextTypes
from storage.database import get_str


class MessageContext:
    def __init__(self, update: Update, ctx: ContextTypes.DEFAULT_TYPE):
        self.update = update
        self.ctx = ctx
        self.message = update.effective_message
        self.chat = update.effective_chat
        self.user = update.effective_user

        # BASIC
        self.body = self.message.text or ""
        self.prefix = get_str("prefix")
        self.command = ""
        self.args = []
        self.text = ""

        # BOT INFO
        self.bot_id = None
        self.bot_username = None
        self.bot_name = None

        # FLAGS
        self.is_admin = False
        self.is_group = self.chat.type in ("group", "supergroup")
        self.is_private = self.chat.type == "private"
        self.is_owner = self.user.id == ctx.bot_data.get("owners")

        # PARSE COMMAND
        self._parse_command()

        # QUOTED
        self.isQuoted = bool(self.message.reply_to_message)
        self.quoted = self._parse_quoted()

    def _parse_command(self):
        if not self.body.startswith(self.prefix):
            return

        parts = self.body.split()
        self.command = parts[0][1:].split("@")[0]
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

    async def load_admin(self):
        if not self.is_group:
            self.is_admin = False
            return

        try:
            member = await self.ctx.bot.get_chat_member(
                self.chat.id,
                self.from_user.id
            )
            self.is_admin = member.status in ("administrator", "creator")
        except Exception:
            self.is_admin = False

    async def load_bot(self):
        if self.bot_id is not None:
            return

        me = await self.ctx.bot.get_me()

        self.bot_id = me.id
        self.bot_username = me.username
        self.bot_name = me.first_name

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
