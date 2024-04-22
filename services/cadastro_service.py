from models.cadastro_model import CadastroHttpResponse
from repositories.cadastro_repository import CadastroRepositorio


class CadastroService:

    def __init__(self):
        self.response = None
        self.cadastro_repository = CadastroRepositorio()

    async def add_cadastro(self, cadastro) -> CadastroHttpResponse:
        try:
            if cadastro["cnu"]:
                cadastro = await self.cadastro_repository.save(cadastro=cadastro)
                self.response = CadastroHttpResponse(
                    status_code=200,
                    body=cadastro
                )
        except Exception as error:
            raise error
        return self.response
