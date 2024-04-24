from datetime import datetime
from uuid import uuid4
from fastapi import status, HTTPException

from models.cadastro_model import CadastroHttpResponse
from schemas.cadastro_schema import Cadastro
from repositories.cadastro_repository import CadastroRepository


class CadastroService:
    """
    Service class for Cadastro-related operations.
    """

    def __init__(self):
        """
        Initialize CadastroService.
        """
        self.schema = None
        self.cadastro_repository = CadastroRepository()

    async def add_cadastro(self, cadastro) -> CadastroHttpResponse:
        """
        Add a new Cadastro.

        Args:
            cadastro: The data for the new Cadastro.

        Returns:
            CadastroHttpResponse: The HTTP response containing the saved Cadastro.

        Raises:
            HTTPException: If the provided Cadastro data is empty.
        """
        if not cadastro:
            raise HTTPException(
                status_code=status.HTTP_412_PRECONDITION_FAILED,
                detail={"error": "Entity is empty"}
            )
        saved_cadastro = await self.cadastro_repository.save(cadastro=cadastro)
        return CadastroHttpResponse(body=saved_cadastro)
