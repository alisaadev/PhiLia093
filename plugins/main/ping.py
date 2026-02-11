import time


async def run_ping(m):
    start = time.perf_counter()

    msg = await m.reply("🏓 Pinging...")

    end = time.perf_counter()

    latency = (end - start) * 1000  # ms

    await msg.edit_text(
        f"🏓 Pong!\n"
        f"⚡ Response: {latency:.2f} ms\n"
    )


plugin = {
    "command": ["ping"],
    "run": run_ping
}
