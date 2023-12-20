import json
import requests

filepath = "/home/edwin/Repositorios/caida_nodos"
#filepath = "/caida_nodos"

url = 'https://graph.facebook.com/v15.0/110877225229299/messages'
auth_token='EAAMbhLRv2KUBAO4PRzHwQbYXkDm6vlZCrUZBKKx4oBOSLxdWrNJKTq8rpXQPCckAn9EqDMF7ocPURSn0i3VnbBBrsvlIxvMFmmPA6biz2IkfFlvxu71t1m0ibAbsoD9Rpxicz0zzn8tPvjTEqiRhpHDHPFjkWPfkZAGuLA3RIZBa7px562st'
headers = {'Content-Type': "application/json", 'Authorization': 'Bearer ' + auth_token}

def send_whatsapp_message(plantilla, nodo, hora):
    with open(f"{filepath}/numeros.txt") as f:
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
    with open(f"{filepath}/numeros.txt") as f:
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
