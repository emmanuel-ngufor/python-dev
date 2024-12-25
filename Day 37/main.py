import requests
from datetime import datetime

USERNAME = "emman"
TOKEN = "bbgu&387sb!~*)idu:>?\]+\"`<>,.dhjh"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# User profile acc created.
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hrs",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()
today = today.strftime("%Y%m%d")

pixel_data_config = {
    "date": f"{today}",
    "quantity": input("How many hours did your spend coding today?:  "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data_config, headers=headers)
print(response.text)



yesterday = datetime(year=2024, month=12, day=23)
yesterday = yesterday.strftime("%Y%m%d")
pixel_update_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{yesterday}"
pixel_data_config = {
    "quantity": "0.35",
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_data_config, headers=headers)
# print(response.text)

delete_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{yesterday}"

# response = requests.delete(url=delete_endpoint, json=pixel_data_config, headers=headers)
# print(response.text)




