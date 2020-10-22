from swagger_client.api.pet_api import PetApi
from swagger_client.api.store_api import StoreApi
from swagger_client.api.user_api import UserApi
from swagger_client.models.pet import Pet

from swagger_client.configuration import Configuration
from client import new_client

if __name__ == "__main__":
    client = new_client(configuration=Configuration())
    body = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "dog"
        },
        "name": "blaki",
        "status": "available"
    }
    pet = client.pet.add_pet(body)
    data = client.pet.delete_pet(pet_id=1)
    print(data)
