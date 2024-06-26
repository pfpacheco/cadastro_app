from models.cadastro_model import CadastroHttpResponse
from factory.factory import ServiceFactory


class CadastroController:

    def __init__(self):
        self.response = None

    async def add_cadastro(self, cadastro) -> CadastroHttpResponse:
        self.response = await ServiceFactory.get_service(name="cadastro").add_cadastro(cadastro=cadastro)
        return self.response
