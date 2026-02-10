import time
from storage.database import get_data, set_data


def bootstrap():
    """
    Initial setup.
    Akan dijalankan saat bot start.
    Jika token / owner belum ada, minta input via terminal.
    """

    bot_token = get_data("bot_token")
    owner_id = get_data("owner_id")

    if bot_token and owner_id:
        return bot_token, int(owner_id)

    print("=== BOT FIRST TIME SETUP ===")
    time.sleep(2)

    while not bot_token:
        bot_token = input("Enter Bot Token: ").strip()
        time.sleep(0.2)

    while not owner_id:
        owner_id = input("Enter Owner ID: ").strip()

    set_data("bot_token", bot_token)
    set_data("owner_id", owner_id)

    time.sleep(1)
    print("Setup complete. Restart not required.\n")
    time.sleep(1)

    return bot_token, int(owner_id)
