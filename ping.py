import os
from dotenv import load_dotenv
load_dotenv()
from send_message import*
from ping3 import ping
import time
import datetime

start_time = time.time()
diccionario_ip = {}

with open("./ips.txt") as file:
    dump_ips = file.read()
    dump_ips = dump_ips.splitlines()

# Almacena todas las ips de ips.txt en un diccionario clave-valor (nodo-ip)
for data_ips in dump_ips:
    ip,nodo = data_ips.split(",")
    if(ip not in diccionario_ip):
        diccionario_ip[ip] = nodo

ip_addresses = list(diccionario_ip.keys())

ip_status = {ip: {"down": False, "last_alert_time": 0} for ip in ip_addresses}

while True:
    current_time = time.time()
    
    for ip in ip_addresses:
        response = ping(ip)
        
        if not response:
            # La IP está caída
            hora = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
            if not ip_status[ip]["down"]:
                # Cambiar el estado a caído
                ip_status[ip]["down"] = True
                ip_status[ip]["last_alert_time"] = current_time
                send_whatsapp_message(os.getenv('TEMPLATE_SERVIDOR_CAIDO'), nodo, hora)
            else:
                # La IP sigue caída
                time_since_last_alert = current_time - ip_status[ip]["last_alert_time"]
                if time_since_last_alert >= int(os.getenv('ALERT_INTERVAL')):
                    ip_status[ip]["last_alert_time"] = current_time
                    send_whatsapp_message_(os.getenv('TEMPLATE_SERVIDOR_SIGUE_CAIDO'), nodo, hora)
        else:
            # La IP está arriba
            ip_status[ip]["down"] = False
            ip_status[ip]["last_alert_time"] = 0
            send_whatsapp_message(os.getenv('TEMPLATE_SERVIDOR_CONECTADO'), nodo, hora) 

    time.sleep(int(os.getenv('CHECK_INTERVAL')))