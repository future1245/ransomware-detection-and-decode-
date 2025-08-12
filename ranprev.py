import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from cryptography.fernet import Fernet

print("="*60)
print("[🔍] Ransomware Decryption Monitor Started")
print("="*60)

class Decrypter(FileSystemEventHandler):
    def __init__(self):
        self.possible_keys = []
        self.key_no = 0
        self.fernet = None

    def on_created(self, event):
        if event.is_directory:
            return 
        
        self.possible_keys.append(event.src_path)
        print(self.possible_keys, "is added as a possible key")
        self.key_no += 1

    def on_modified(self, event):
        if event.is_directory:
            return 
        
        if self.key_no == 0:
            print("no possible keys to decrypt")
            return 
        
        for keys in self.possible_keys:
            try:
                with open(keys, "rb") as k:
                    key = k.read()
                    if len(key) != 44:
                        print("the key", key, "is invalid")
                        continue

                    try:
                        with open(event.src_path, "rb") as file:
                            program = file.read()
                        decrypted = Fernet(key).decrypt(program)
                        with open(event.src_path, "wb") as files:
                            files.write(decrypted)
                        print(f"[✔] Decrypted {event.src_path} using key {keys}")
                        break 

                    except Exception as e:
                        print(f" Decryption failed with key {keys}: {e}")
                        continue

            except Exception as e:
                print(f"Failed to open/read key file {keys}: {e}")
                continue

if __name__ == "__main__":
    path = input("Enter the full path to the folder to monitor: ").strip()
    event_handler = Decrypter()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

