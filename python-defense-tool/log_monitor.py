import time
from collections import defaultdict
from datetime import datetime

LOG_FILE = "security_logs.txt"
ALERT_FILE = "alerts.txt"

MAX_ATTEMPTS = 3

failed_attempts = defaultdict(int)

print("SOC Monitor iniciado...\n")

while True:
    try:
        with open(LOG_FILE, "r") as file:
            logs = file.readlines()

        for log in logs:

            if "Failed login" in log:

                ip = log.split("from")[-1].strip()

                failed_attempts[ip] += 1

                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                print(f"[INFO] {timestamp} - Tentativa inválida detectada do IP: {ip}")

                if failed_attempts[ip] >= MAX_ATTEMPTS:

                    alert = f"""
[ALERTA CRÍTICO]
Data/Hora: {timestamp}
Tipo: Possível ataque de brute force
IP suspeito: {ip}
Tentativas: {failed_attempts[ip]}
"""

                    print(alert)

                    with open(ALERT_FILE, "a") as alert_file:
                        alert_file.write(alert + "\n")

        open(LOG_FILE, "w").close()

        time.sleep(5)

    except FileNotFoundError:
        print(f"Arquivo '{LOG_FILE}' não encontrado.")
        break