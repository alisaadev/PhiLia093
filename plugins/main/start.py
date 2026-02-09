async def run_start(m):
    await m.reply("Masih Maintenance ❗")


plugin = {
    "command": ["start"],
    "tags": "main",

    "run": run_start
}
