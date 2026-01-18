from pathlib import Path
import importlib
import sys

PLUGINS = {}
PLUGIN_MODULES = {}


def load_plugins(path="plugins"):
    files = Path(path).rglob("*.py")

    for file in files:
        if file.name.startswith("_"):
            continue

        name = str(file).replace(".py", "").replace("/", ".")
        module_path = f"{name}"

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
