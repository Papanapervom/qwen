import os
import socket
import subprocess
import datetime

def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, timeout=10, text=True).strip()
    except Exception as e:
        return f"Error: {str(e)}"

print("=== Qwen Coder Sandbox Info Collector ===")
print(f"Время: {datetime.datetime.now()}")

info = f"""=== ИНФОРМАЦИЯ О ПЕСОЧНИЦЕ QWEN CODER ===

Время: {datetime.datetime.now()}

Пользователь:
{run('whoami')}
{run('id')}

Система:
{run('uname -a')}
Hostname: {run('hostname')}

IP адреса:
External IP: {run('curl -s --max-time 5 ifconfig.me || echo "не получилось")}
Internal IP: {socket.gethostbyname(socket.gethostname())}

Диск:
{run('df -h')}

Память:
{run('free -h')}

CPU:
{run('cat /proc/cpuinfo | grep "model name" | head -n 4')}

Топ процессов:
{run('ps aux --sort=-%cpu | head -n 20')}

Python окружение:
{run('python3 --version')}
Pip packages:
{run('pip list | head -n 40')}

Сеть:
{run('ip addr show | grep "inet " || echo "нет ip addr"')}

OSS хранилище:
{run('ls -lh /oss 2>/dev/null || echo "/oss не найдена")}
{run('df -h | grep -i oss || echo "OSS не виден")}

=== КОНЕЦ ИНФОРМАЦИИ ===
"""

# Сохраняем в два места
try:
    with open("/tmp/qwen_sandbox_info.txt", "w", encoding="utf-8") as f:
        f.write(info)
    print("✅ Сохранено в /tmp/qwen_sandbox_info.txt")
except Exception as e:
    print("Ошибка при сохранении в /tmp:", e)

try:
    with open("/oss/qwen_sandbox_info.txt", "w", encoding="utf-8") as f:
        f.write(info)
    print("✅ Сохранено в /oss/qwen_sandbox_info.txt")
except Exception as e:
    print("Ошибка при сохранении в /oss:", e)

print("\nГотово! Теперь выполни команду:")
print("cat /oss/qwen_sandbox_info.txt")
print("или")
print("cat /tmp/qwen_sandbox_info.txt")