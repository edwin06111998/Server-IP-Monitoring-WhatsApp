from send_message import*
from datetime import datetime
import json
import requests

#filepath = "/home/edwin/Repositorios/caida_nodos"
filepath = "/caida_nodos"

diccionario_control_antena = {}

with open(f"{filepath}/control_antenas.txt") as file_antenas:
    dump_antenas = file_antenas.read()
    dump_antenas = dump_antenas.splitlines()

# Almacena todas las ips y el estado de control.txt en un diccionario clave-valor (ip-estado)
for data in dump_antenas:
    antena,estado,tiempo = data.split(",")
    diccionario_control_antena[antena] = [estado,tiempo]

hora = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")    
url = 'https://unms.maxitel.ec/nms/api/v2.1/devices?withInterfaces=true&authorized=true&type=airMax&role=ap'
auth_token='f1a309f6-b90f-4f60-ba94-4498de730057'
headers = {'accept': 'application/json','x-auth-token': auth_token}
r = requests.get(url,headers=headers, verify=False)
json_data = json.loads(r.text)
for antena in json_data:
    nombre_antena = antena['identification']['name']
    estado_antena = antena['identification']['site']['status']
    ip_antena = antena['ipAddress']    
    if nombre_antena not in diccionario_control_antena:
        diccionario_control_antena[nombre_antena] = [estado_antena,0]
    if(estado_antena == 'disconnected'):
        if (diccionario_control_antena[nombre_antena][0] == "active"):            
            send_whatsapp_message("electricidad_fallida", nombre_antena, hora)
            f = open(f"{filepath}/output.txt", "a")
            f.write(nombre_antena + " (" + str(ip_antena) + ")" + '\t' + "esta CAIDO" + '\t' + hora + '\n')
            f.close()
            diccionario_control_antena[nombre_antena][0] = estado_antena
            print(hora)
        else: 
            tiempo = int(diccionario_control_antena[nombre_antena][1])
            if (tiempo < 8):
                diccionario_control_antena[nombre_antena] = ["disconnected", tiempo + 1]
            else:
                send_whatsapp_message("electricidad_fallida", nombre_antena, hora)
                f = open(f"{filepath}/output.txt", "a")
                f.write(nombre_antena + " (" + str(ip_antena) + ")" + '\t' + "esta CAIDO" + '\t' + hora + '\n')
                f.close()
                diccionario_control_antena[nombre_antena] = ["disconnected", 0]
                print(hora)
    else:
        if (diccionario_control_antena[nombre_antena][0] == "disconnected"):
            send_whatsapp_message("electricidad_activa", nombre_antena, hora)
            f = open(f"{filepath}/output.txt", "a")
            f.write(nombre_antena + " (" + str(ip_antena) + ")" + '\t' + "esta ACTIVO" + '\t' + hora + '\n')
            f.close()
            diccionario_control_antena[nombre_antena][0] = "active"
            print(hora)

with open(f"{filepath}/control_antenas.txt", "w") as file:
        pass

for key in diccionario_control_antena:  
    f = open(f"{filepath}/control_antenas.txt", "a")      
    f.write(key + "," + str(diccionario_control_antena[key][0]) + "," + str(diccionario_control_antena[key][1]) + '\n')
    f.close()
