import os
from send_message import*
from datetime import datetime
import time

start_time = time.time()

filepath = "repository_path"

ip_dict = {}
control_dict = {}

with open(f"{filepath}/control.txt") as file:
    dump = file.read()
    dump = dump.splitlines()

# Almacena todas las ips y el status de control.txt en un diccionario clave-valor (ip-status)
for data in dump:
    ip,status,time_data = data.split(",")
    control_dict[ip] = [status, time_data]

with open(f"{filepath}/ips.txt") as file:
    dump_ips = file.read()
    dump_ips = dump_ips.splitlines()

# Almacena todas las ips de ips.txt en un diccionario clave-valor (nodo-ip)
for data_ips in dump_ips:
    ip,server_name = data_ips.split(",")
    if(ip not in ip_dict):
        ip_dict[ip] = server_name

def ping_ip (ip):
    res = os.popen(f"ping -c 4 {ip}").read().strip()
    res_list = res.split("\n")
    percentage = 0
    reference = res_list.pop()
    if "packet loss" in reference:
        reference_list = reference.split(",")
        reference_list.pop()
        loss_string = reference_list.pop()
        percentage = int(loss_string.split("%")[0].strip())
    else:
        reference = res_list.pop()
        reference_list = reference.split(",")
        reference_list.pop()
        loss_string = reference_list.pop()
        percentage = int(loss_string.split("%")[0].strip())
    return percentage

# Hace ping por cada direccion IP y guarda el status en output.txt
for ip in ip_dict:
    server_name = ip_dict[ip]
    hour = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
    percentage = ping_ip(ip)     
    if ip not in control_dict:
            control_dict[ip] = ["up", 0]  

    if percentage >= 75: 
        time.sleep(0) # Sleep for 30 seconds
        percentage = ping_ip(ip)
        if percentage >= 75: 
            if control_dict[ip][0] == "up":
                send_whatsapp_message("servidor_desconectado", server_name, hour)
                f = open(f"{filepath}/output.txt", "a")
                f.write(server_name + " (" + str(ip) + ")" + '\t' + "is DOWN" + '\t' + hour + '\n')
                f.close()
                control_dict[ip] = ["down", 0]
            else:
                time_data = int(control_dict[ip][1])
                if(time_data < 3):
                    control_dict[ip] = ["down", time_data + 1]
                else:
                    send_whatsapp_message_("conexion_sigue_perdida", server_name)
                    f = open(f"{filepath}/output.txt", "a")
                    f.write(server_name + " (" + str(ip) + ")" + '\t' + "is DOWN" + '\t' + hour + '\n')
                    f.close()
                    control_dict[ip] = ["down", 0]                            
    else:
        if control_dict[ip][0] == "down":
            send_whatsapp_message("servidor_conectado", server_name, hour)            
            f = open(f"{filepath}/output.txt", "a")
            f.write(server_name + " (" + str(ip) + ")" + '\t' + "is UP" + '\t' + hour + '\n')
            f.close()
        control_dict[ip] = ["up", 0]

with open(f"{filepath}/control.txt", "w") as file:
        pass

for key in control_dict:  
    f = open(f"{filepath}/control.txt", "a")      
    f.write(key + "," + str(control_dict[key][0]) + "," + str(control_dict[key][1]) + '\n')
    f.close()

"""
# Abre el archivo output.txt
    with open('output.txt') as file:
        output = file.read()
        print(output)

 # Elimina contenido de output.txt
    with open('output.txt', "w") as file:
        pass
"""
   
