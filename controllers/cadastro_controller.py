from factory.factory import ServiceFactory
from models.cadastro_model import CadastroHttpResponse

from fastapi.exceptions import HTTPException


class CadastroController:

    def __init__(self):
        self.response = None

    async def add_cadastro(self, cadastro) -> HTTPException | CadastroHttpResponse:
        self.response = await ServiceFactory.get_service(name="cadastro").add_cadastro(cadastro=cadastro)
        return self.response
