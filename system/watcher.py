from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from system.loader import load_plugins


class PluginWatcher(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print("🔄 Plugin changed, reloading...")
            load_plugins()


def start_watcher(path="plugins"):
    observer = Observer()
    observer.schedule(PluginWatcher(), path, recursive=False)
    observer.start()
