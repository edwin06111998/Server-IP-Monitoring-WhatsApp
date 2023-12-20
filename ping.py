import os
from send_message import*
from datetime import datetime
import time

start_time = time.time()

filepath = "/home/edwin/Repositorios/caida_nodos"
#filepath = "/caida_nodos"

diccionario_ip = {}
diccionario_control = {}

with open(f"{filepath}/control.txt") as file:
    dump = file.read()
    dump = dump.splitlines()

# Almacena todas las ips y el estado de control.txt en un diccionario clave-valor (ip-estado)
for data in dump:
    ip,estado,tiempo = data.split(",")
    diccionario_control[ip] = [estado, tiempo]

with open(f"{filepath}/ips.txt") as file:
    dump_ips = file.read()
    dump_ips = dump_ips.splitlines()

# Almacena todas las ips de ips.txt en un diccionario clave-valor (nodo-ip)
for data_ips in dump_ips:
    ip,nodo = data_ips.split(",")
    if(ip not in diccionario_ip):
        diccionario_ip[ip] = nodo

def ping_ip (ip):
    res = os.popen(f"ping -c 4 {ip}").read().strip()
    res_list = res.split("\n")
    porcentaje = 0
    referencia = res_list.pop()
    if "packet loss" in referencia:
        referencia_list = referencia.split(",")
        referencia_list.pop()
        loss_string = referencia_list.pop()
        porcentaje = int(loss_string.split("%")[0].strip())
    else:
        referencia = res_list.pop()
        referencia_list = referencia.split(",")
        referencia_list.pop()
        loss_string = referencia_list.pop()
        porcentaje = int(loss_string.split("%")[0].strip())
    return porcentaje

# Hace ping por cada direccion IP y guarda el estado en output.txt
for ip in diccionario_ip:
    nodo = diccionario_ip[ip]
    hora = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
    porcentaje = ping_ip(ip)     
    if ip not in diccionario_control:
            diccionario_control[ip] = ["activo", 0]  

    if porcentaje >= 75: 
        time.sleep(30) # Sleep for 5  seconds
        porcentaje = ping_ip(ip)
        if porcentaje >= 75: 
            if diccionario_control[ip][0] == "activo":
                send_whatsapp_message("servidor_desconectado", nodo, hora)
                f = open(f"{filepath}/output.txt", "a")
                f.write(nodo + " (" + str(ip) + ")" + '\t' + "esta CAIDO" + '\t' + hora + '\n')
                f.close()
                diccionario_control[ip] = ["caido", 0]
                print(hora)
            else:
                tiempo = int(diccionario_control[ip][1])
                if(tiempo < 8):
                    diccionario_control[ip] = ["caido", tiempo + 1]
                else:
                    send_whatsapp_message_("conexion_sigue_perdida", nodo)
                    f = open(f"{filepath}/output.txt", "a")
                    f.write(nodo + " (" + str(ip) + ")" + '\t' + "esta CAIDO" + '\t' + hora + '\n')
                    f.close()
                    diccionario_control[ip] = ["caido", 0]
                    print(hora)
    else:
        if diccionario_control[ip][0] == "caido":
            send_whatsapp_message("servidor_conectado", nodo, hora)            
            f = open(f"{filepath}/output.txt", "a")
            f.write(nodo + " (" + str(ip) + ")" + '\t' + "esta ACTIVO" + '\t' + hora + '\n')
            f.close()
            print(hora)
        diccionario_control[ip] = ["activo", 0]

with open(f"{filepath}/control.txt", "w") as file:
        pass

for key in diccionario_control:  
    f = open(f"{filepath}/control.txt", "a")      
    f.write(key + "," + str(diccionario_control[key][0]) + "," + str(diccionario_control[key][1]) + '\n')
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
