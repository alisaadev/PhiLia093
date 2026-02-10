from storage.config import MESSAGES
from system.loader import PLUGINS
from storage.database import get_bool


async def handler(m):
    if not m.body:
        return

    await m.load_bot()
    await m.load_admin()

    # === GLOBAL FILTER ===
    if not get_bool("public") and not m.is_owner:
        return

    for name, plugin in PLUGINS.items():

        # plugin.all
        if callable(plugin.get("all")):
            try:
                await plugin["all"](m)
            except Exception as e:
                print(f"[PLUGIN ALL ERROR] {name}", e)

        # plugin.before
        if callable(plugin.get("before")):
            try:
                stop = await plugin["before"](m)
                if stop:
                    continue
            except Exception as e:
                print(f"[PLUGIN BEFORE ERROR] {name}", e)

        # COMMAND CHECK
        if not m.command:
            continue

        commands = plugin.get("command", [])
        if m.command not in commands:
            continue

        # === PERMISSION CHECK ===
        if plugin.get("owner") and not m.is_owner:
            await m.reply(MESSAGES["owner"])
            continue

        if plugin.get("group") and not m.is_group:
            await m.reply(MESSAGES["group"])
            continue

        if plugin.get("private") and m.is_group:
            await m.reply(MESSAGES["private"])
            continue

        # === RUN ===
        try:
            await plugin["run"](m)
        except Exception as e:
            print(f"[PLUGIN RUN ERROR] {name}", e)
            await m.reply("Terjadi error saat menjalankan perintah")

        # plugin.after
        if callable(plugin.get("after")):
            try:
                await plugin["after"](m)
            except Exception as e:
                print(f"[PLUGIN AFTER ERROR] {name}", e)
                