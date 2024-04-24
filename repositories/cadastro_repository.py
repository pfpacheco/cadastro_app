from decouple import config
from datetime import datetime
from uuid import uuid4

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine

from fastapi import status
from fastapi.exceptions import HTTPException

from models.cadastro_model import CadastroResponseBody
from schemas.cadastro_schema import Cadastro

class CadastroRepository:
    """
    Repository class for handling database operations related to Cadastro.
    """

    def __init__(self):
        """
        Initialize CadastroRepositorio.

        This class manages database interactions for Cadastro objects.
        """
        self.db_url = config("POSTGRES_URL")
        self.engine = create_engine(url=self.db_url)
        self.session = sessionmaker(bind=self.engine)
        self.body_response = None

    async def save(self, entity) -> CadastroResponseBody:
        """
        Save a Cadastro record in the database.

        Args:
            cadastro: The data for the new Cadastro.

        Returns:
            CadastroBodyResponse: The response body for the saved Cadastro.

        Raises:
            HTTPException: If there's an IntegrityError or if the provided CNU is empty.
        """
        try:
            session = self.session()
            session.add(entity)
            session.commit()
            session.refresh(entity)
            self.body_response = CadastroResponseBody(id=str(entity.id), name=entity.name, cnu=entity.cnu,
                                                      description=entity.description,
                                                      created_at=entity.created_at,updated_at=None)
        except IntegrityError as error:
            session.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"error": f"Integrity error {error}"})
        finally:
            session.close()
        return self.body_response

    async def find_by_cnu(self, cnu: str) -> CadastroResponseBody:
        """
        Find a Cadastro record by its CNU (Customer Number).

        Args:
            cnu (str): The CNU to search for.

        Returns:
            CadastroBodyResponse: The response body for the found Cadastro.

        Raises:
            HTTPException: If the provided CNU is empty or if the Cadastro with the provided CNU is not found.
        """
        try:
            session = self.session()
            if cnu is not None:
                rows = session.query(Cadastro).filter_by(cnu=cnu).first()
                if rows:
                    self.body_response = CadastroResponseBody(id=str(rows.id), name=rows.name, cnu=rows.cnu,
                                                              description=rows.description,
                                                              created_at=rows.created_at, updated_at=None)
                else:
                    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"error": "Cadastro not found!"})
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"error": "CNU is empty"})
        except HTTPException as error:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"error": "Entity not found"})
        return self.body_response
