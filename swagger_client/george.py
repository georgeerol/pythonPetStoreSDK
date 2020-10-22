from swagger_client import api_client
from swagger_client.api.pet_api import PetApi
import json

if __name__ == '__main__':
    api = api_client.ApiClient()
    url = "https://petstore.swagger.io/v2/pet/findByStatus?status=available"
    data = api.request("GET", url)
    print(data.data)

    post_url = "https://petstore.swagger.io/v2/pet"
    body = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "dog"
        },
        "name": "blaki",
        "status": "available"
    }
    data = api.request("POST", url=post_url, body=body)
    print(data.data)








