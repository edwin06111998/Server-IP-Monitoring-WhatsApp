from send_message import*
from datetime import datetime
import json
import requests

filepath = "repository_path"

antenna_control_dict = {}

with open(f"{filepath}/antenna_control.txt") as file_antennas:
    dump_antennas = file_antennas.read()
    dump_antennas = dump_antennas.splitlines()

# Almacena todas las ips y el estado de control.txt en un diccionario clave-valor (ip-estado)
for data in dump_antennas:
    antenna,estado = data.split(",")
    antenna_control_dict[antenna] = estado

hour = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")    
url = 'https://unms.maxitel.ec/nms/api/v2.1/devices?withInterfaces=true&authorized=true&type=airMax&role=ap'
auth_token='f1a309f6-b90f-4f60-ba94-4498de730057'
headers = {'accept': 'application/json','x-auth-token': auth_token}
r = requests.get(url,headers=headers, verify=False)
json_data = json.loads(r.text)
for antenna in json_data:
    antenna_name = antenna['identification']['name']
    print(antenna_name)
    antenna_status = antenna['identification']['site']['status']
    ip_antenna = antenna['ipAddress']    
    if antenna_name not in antenna_control_dict:
        antenna_control_dict[antenna_name] = antenna_status
    if(antenna_status == 'disconnected'):
        if (antenna_control_dict[antenna_name] == "active"):
            send_whatsapp_message("electricidad_fallida", antenna_name, hour)
            f = open(f"{filepath}/output.txt", "a")
            f.write(antenna_name + " (" + str(ip_antenna) + ")" + '\t' + "is DOWN" + '\t' + hour + '\n')
            f.close()
            antenna_control_dict[antenna_name] = "disconnected"
    else:
        if (antenna_control_dict[antenna_name] == "disconnected"):
            send_whatsapp_message("electricidad_activa", antenna_name, hour)
            f = open(f"{filepath}/output.txt", "a")
            f.write(antenna_name + " (" + str(ip_antenna) + ")" + '\t' + "is UP" + '\t' + hour + '\n')
            f.close()
            antenna_control_dict[antenna_name] = "active"

with open(f"{filepath}/antenna_control.txt", "w") as file:
        pass

for key in antenna_control_dict:  
    f = open(f"{filepath}/antenna_control.txt", "a")      
    f.write(key + "," + str(antenna_control_dict[key]) + '\n')
    f.close()