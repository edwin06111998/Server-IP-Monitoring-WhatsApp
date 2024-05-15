import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()

filepath = "./numbers.txt"
url = os.getenv('URL')
auth_token=os.getenv('L0NG_TOKEN')
headers = {'Content-Type': "application/json", 'Authorization': 'Bearer ' + auth_token}

def send_whatsapp_message(plantilla, nodo, hora):
    with open(filepath) as f:
        contents = f.readlines()
        for line in contents:
            numero = line.split(",").pop().strip()
            data = {
                "messaging_product": "whatsapp",
                "to": numero,
                "type": "template",
                "template": {
                    "name": plantilla,
                    "language": {
                        "code": "es_ES"
                    },
                    "components": [
                        {
                            "type": "body",
                            "parameters": [
                                {
                                    "type": "text",
                                    "text": nodo
                                },
                                {
                                    "type": "text",
                                    "text": hora
                                }
                            ]
                        }
                    ]
                }
            }

            res = requests.post(url, json=data, headers=headers)

            print(res.status_code)
            response_json = json.loads(res.content)
            print(response_json)

def send_whatsapp_message_(plantilla, nodo):
    with open(filepath) as f:
        contents = f.readlines()
        for line in contents:
            numero = line.split(",").pop().strip()
            data = {
                "messaging_product": "whatsapp",
                "to": numero,
                "type": "template",
                "template": {
                    "name": plantilla,
                    "language": {
                        "code": "es_ES"
                    },
                    "components": [
                        {
                            "type": "body",
                            "parameters": [
                                {
                                    "type": "text",
                                    "text": nodo
                                }
                            ]
                        }
                    ]
                }
            }

            res = requests.post(url, json=data, headers=headers)

            print(res.status_code)
            response_json = json.loads(res.content)
            print(response_json)
