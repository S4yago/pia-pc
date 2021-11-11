import socket
import colorama
from colorama import Fore
import threading

colorama.init()

print_lock = threading.Lock()

def connscan(tgtHost, tgtPort):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((tgtHost, tgtPort))
        scanner.close()
        with print_lock:
            print(Fore.WHITE + f"[{tgtPort}]" + Fore.GREEN + "Abierto")
    except:
        print (Fore.WHITE + f"[{tgtPort}]" + Fore.RED + "Cerrado")
    finally:
        scanner.close()
