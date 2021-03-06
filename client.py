from dataclasses import dataclass
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
from swagger_client.api.pet_api import PetApi
from swagger_client.api.store_api import StoreApi
from swagger_client.api.user_api import UserApi


@dataclass
class AutogeneratedApiClient:
    configuration: Configuration
    client: ApiClient
    pet: PetApi
    store: StoreApi
    user: UserApi


def new_client(
        configuration: Configuration
) -> AutogeneratedApiClient:
    client = ApiClient(configuration=configuration)
    return AutogeneratedApiClient(
        configuration,
        client=client,
        pet=PetApi(client),
        store=StoreApi(client),
        user=UserApi(client),
    )
