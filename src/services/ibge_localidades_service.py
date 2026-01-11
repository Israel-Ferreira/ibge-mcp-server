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


    async def get_cities_of_state(self, state_acronym: str):
        states = await self.get_states()
        state_id =  [state["id"] for state in states if state["sigla"] == state_acronym]

        if not state_id:
            raise ValueError(f"Estado com a sigla {state_acronym} não encontrado")


        response = await self._client.get(f"/estados/{state_id[0]}/municipios")        

        return response.json()

    
    async def get_metropolitan_region_cities(self, state_acronym: str, metropolitan_region_name: str):
        """
        Retorna as cidades de uma região metropolitana específica.
        Para a Região Metropolitana de São Paulo, retorna os 39 municípios oficiais.
        """
        # Lista oficial dos municípios da Região Metropolitana de São Paulo (RMSP)
        rmsp_cities = [
            "Arujá", "Barueri", "Biritiba-Mirim", "Cajamar", "Carapicuíba",
            "Cotia", "Diadema", "Embu das Artes", "Embu-Guaçu", "Ferraz de Vasconcelos",
            "Francisco Morato", "Franco da Rocha", "Guararema", "Guarulhos", "Itapecerica da Serra",
            "Itapevi", "Itaquaquecetuba", "Jandira", "Juquitiba", "Mairiporã",
            "Mauá", "Mogi das Cruzes", "Osasco", "Pirapora do Bom Jesus", "Poá",
            "Ribeirão Pires", "Rio Grande da Serra", "Salesópolis", "Santa Isabel",
            "Santana de Parnaíba", "Santo André", "São Bernardo do Campo", "São Caetano do Sul",
            "São Lourenço da Serra", "São Paulo", "São Roque", "Suzano", "Taboão da Serra",
            "Vargem Grande Paulista"
        ]
        
        if state_acronym.upper() == "SP" and metropolitan_region_name.lower() == "são paulo":
            # Busca todas as cidades de SP
            cities = await self.get_cities_of_state(state_acronym)
            
            # Filtra apenas as cidades da RMSP
            rmsp_cities_result = [
                city for city in cities 
                if city["nome"] in rmsp_cities
            ]
            
            return rmsp_cities_result
        
        # Para outras regiões metropolitanas, retorna erro (poderia ser expandido)
        raise ValueError(
            f"Região metropolitana '{metropolitan_region_name}' no estado '{state_acronym}' "
            "ainda não está implementada. Atualmente suportamos apenas a Região Metropolitana de São Paulo."
        )

    async def  get_cities(self, state_id: int):
        pass