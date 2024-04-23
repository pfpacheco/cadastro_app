from fastapi import status
from fastapi.exceptions import HTTPException

from models.cadastro_model import CadastroHttpResponse
from repositories.cadastro_repository import CadastroRepositorio


class CadastroService:

    def __init__(self):
        self.response = None
        self.cadastro_repository = CadastroRepositorio()

    async def add_cadastro(self, cadastro) -> CadastroHttpResponse:
        if cadastro:
            cadastro = await self.cadastro_repository.save(cadastro=cadastro)
            self.response = CadastroHttpResponse(
                body=cadastro
            )
        else:
            raise HTTPException(status_code=status.HTTP_412_PRECONDITION_FAILED, detail="Entity could not be empty")
        return self.response
