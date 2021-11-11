import socket
import colorama
from colorama import Fore
import threading

colorama.init()

print_lock = threading.Lock()
