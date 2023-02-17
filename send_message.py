import json
import requests

filepath = "repository_path"

url = 'https://graph.facebook.com/v15.0/{id_app}/messages'
auth_token='permanent_token'
headers = {'Content-Type': "application/json", 'Authorization': 'Bearer ' + auth_token}

def send_whatsapp_message(template, server_name, hour):
    with open(f"{filepath}/numbers.txt") as f:
        contents = f.readlines()
        for line in contents:
            number = line.split(",").pop().strip()
            data = {
                "messaging_product": "whatsapp",
                "to": number,
                "type": "template",
                "template": {
                    "name": template,
                    "language": {
                        "code": "es_ES"
                    },
                    "components": [
                        {
                            "type": "body",
                            "parameters": [
                                {
                                    "type": "text",
                                    "text": server_name
                                },
                                {
                                    "type": "text",
                                    "text": hour
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

def send_whatsapp_message_(template, server_name):
    with open(f"{filepath}/numbers.txt") as f:
        contents = f.readlines()
        for line in contents:
            number = line.split(",").pop().strip()
            data = {
                "messaging_product": "whatsapp",
                "to": number,
                "type": "template",
                "template": {
                    "name": template,
                    "language": {
                        "code": "es_ES"
                    },
                    "components": [
                        {
                            "type": "body",
                            "parameters": [
                                {
                                    "type": "text",
                                    "text": server_name
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