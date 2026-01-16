# loader.py
import importlib
import os
import sys

PLUGINS = {}
PLUGIN_MODULES = {}


def load_plugins(path="plugins"):
    for file in os.listdir(path):
        if not file.endswith(".py") or file.startswith("_"):
            continue

        name = file[:-3]
        module_path = f"{path}.{name}"

        try:
            if module_path in sys.modules:
                module = importlib.reload(sys.modules[module_path])
            else:
                module = importlib.import_module(module_path)

            PLUGIN_MODULES[name] = module
            PLUGINS[name] = getattr(module, "plugin", None)

        except Exception as e:
            print(f"[PLUGIN LOAD ERROR] {name}", e)

    return PLUGINS
