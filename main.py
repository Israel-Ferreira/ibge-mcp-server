from fastmcp import FastMCP
from httpx import AsyncClient

from src.services import IbgeLocalidadesService

mcp = FastMCP(name="Ibge-MCP", version="1.0.0")

ibge_localidades_service = IbgeLocalidadesService()


@mcp.tool(
    name="get_countries",
    description="Retorna todos os países da API do IBGE"
)
async def get_countries():
    countries = await ibge_localidades_service.get_countries()
    return countries



@mcp.tool(
    name="get_all_states_of_brazil",
    description="Retorna todos os estados do Brasil da API do IBGE",
)
async def get_all_states_of_brazil():
    states = await ibge_localidades_service.get_states()
    return states


@mcp.tool(
    name="get_cities_of_state",
    description="Retorna todas as cidades de um estado da API do IBGE",
)
async def get_cities_of_state(state_acronym: str):
    cities = await ibge_localidades_service.get_cities_of_state(state_acronym)
    return cities


if __name__ == "__main__":
    mcp.run(
        transport="http",
        port=8080,
    )