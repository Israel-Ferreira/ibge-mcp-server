from httpx import AsyncClient

class IbgeLocalidadesService:
    def __init__(self):
        self._client = AsyncClient(base_url="https://servicodados.ibge.gov.br/api/v1/localidades")


    async def get_countries(self):
        response = await self._client.get("/paises")
        return response.json()


    async def get_states(self):
        response = await self._client.get("/estados")
        return response.json()

    

    async def  get_cities(self, state_id: int):
        pass