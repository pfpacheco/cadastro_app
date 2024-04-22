from models.cadastro_model import CadastroHttpResponse
from fastapi import HTTPException


class CadastroService:

    def __init__(self):
        self.response = None

    async def add_cadastro(self, cadastro) -> CadastroHttpResponse:
        try:
            if cadastro:
                self.response = CadastroHttpResponse(
                    code=200,
                    status="OK",
                    body=cadastro
                )

        except HTTPException:
            raise HTTPException(status_code=500, detail="INTERNAL_SERVER_ERROR")

        return self.response
