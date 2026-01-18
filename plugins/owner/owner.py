import asyncio
import subprocess
import textwrap
import traceback


async def run_eval(m):
    if not m.text:
        return await m.reply("Masukkan kode Python")

    import textwrap
    import traceback

    code = textwrap.dedent(m.text)

    env = {
        "m": m,
        "ctx": m.ctx,
        "bot": m.ctx.bot,
        "__builtins__": __builtins__,
    }

    try:
        exec(
            "async def __eval_fn__():\n"
            + textwrap.indent(code, "    "),
            env
        )
        result = await env["__eval_fn__"]()
        if result is not None:
            await m.reply(f"✅ Result:\n{result}")
    except Exception:
        await m.reply(f"❌ Error:\n{traceback.format_exc()}")

async def run_exec(m):
    if not m.text:
        return await m.reply("Masukkan command shell")

    try:
        proc = await asyncio.create_subprocess_shell(
            m.text,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()

        output = stdout.decode() or stderr.decode()
        if not output:
            output = "(no output)"

        # Telegram limit ~4096 char
        await m.reply(f"🖥️ Output:\n{output[:4000]}")
    except Exception as e:
        await m.reply(f"❌ Error:\n{e}")


plugin = {
    "command": ["eval", "exec"],
    "owner": True,

    "run": lambda m: run_eval(m) if m.command == "eval" else run_exec(m)
}
