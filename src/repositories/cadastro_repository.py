from sqlalchemy.exc import IntegrityError

from fastapi import status
from fastapi.exceptions import HTTPException

from src.database.database import Database
from src.schemas.cadastro_schema import Cadastro
from src.models.cadastro_model import CadastroResponseBody


class CadastroRepository:
    """
    Repository class for handling database operations related to Cadastro.
    """

    def __init__(self):
        """
        Initialize CadastroRepositorio.

        This class manages database interactions for Cadastro objects.
        """
        self.database = Database()
        self.body_response = None
        self.session = self.database.get_db()

    async def save(self, entity) -> CadastroResponseBody:
        """
        Save a Cadastro record in the database.

        Args:
            cadastro: The data for the new Cadastro.

        Returns:
            CadastroBodyResponse: The response body for the saved Cadastro.

        Raises:
            HTTPException: If there's an IntegrityError or if the provided CNU is empty.
            :param entity:
        """
        try:
            self.session.add(entity)
            self.session.commit()
            self.session.refresh(entity)
        except IntegrityError as error:
            self.session.rollback()
            raise HTTPException(status_code=status.HTTP_428_PRECONDITION_REQUIRED,
                                detail={"status_code": status.HTTP_428_PRECONDITION_REQUIRED,
                                        "error": f"{error.__cause__}"})
        try:
            self.body_response = CadastroResponseBody(id=str(entity.id), name=entity.name, cnu=entity.cnu,
                                                      description=entity.description,
                                                      created_at=entity.created_at,updated_at=None)
        except HTTPException as error:
            raise HTTPException(status_code=status.HTTP_417_EXPECTATION_FAILED,
                                detail={"status_code": status.HTTP_417_EXPECTATION_FAILED,
                                        "error": f"{error.__cause__}"})
        finally:
            self.session.close()
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
            if cnu != "":
                cadastro = self.session.query(Cadastro).filter_by(cnu=cnu).first()
                if cadastro is not None:
                    self.body_response = CadastroResponseBody(id=str(cadastro.id), name=cadastro.name, cnu=cadastro.cnu,
                                                              description=cadastro.description,
                                                              created_at=cadastro.created_at, updated_at=None)
                else:
                    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                        detail={"status_code": status.HTTP_404_NOT_FOUND,
                                                "error": "Cadastro not found!"})
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail={"status_code": status.HTTP_404_NOT_FOUND,
                                            "error": "CNU is empty!"})
        except HTTPException as error:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail={"status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                                        "error": f"{error.__cause__}"})
        finally:
            self.session.close()
        return self.body_response
