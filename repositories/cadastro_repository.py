from decouple import config
from datetime import datetime
from uuid import uuid4

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine

from fastapi import status
from fastapi.exceptions import HTTPException

from models.cadastro_model import CadastroBodyResponse
from schemas.cadastro_schema import Cadastro


class CadastroRepositorio:

    def __init__(self):
        self.db_url = config("POSTGRES_URL")
        self.schema = None
        self.engine = create_engine(url=self.db_url)
        self.session = sessionmaker(bind=self.engine)
        self.body_response = None

    async def save(self, cadastro) -> CadastroBodyResponse:
        session = self.session()
        try:
            self.schema = Cadastro(
                id=uuid4(),
                name=cadastro["name"],
                cnu=cadastro["cnu"],
                description=cadastro["description"],
                created_at=datetime.now()
            )
            session.add(self.schema)
            session.commit()
        except IntegrityError as error:
            session.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message": error.__cause__.__str__()})
        finally:
            self.body_response = await self.find_by_cnu(cnu=cadastro["cnu"])
        return self.body_response

    async def find_by_cnu(self, cnu: str) -> CadastroBodyResponse:
        session = self.session()
        try:
            if cnu != "":
                rows = session.query(Cadastro).filter_by(cnu=cnu).first()
                if rows:
                    self.body_response = CadastroBodyResponse(
                        id=str(rows.id),
                        name=rows.name,
                        cnu=rows.cnu,
                        description=rows.description,
                        created_at=rows.created_at,
                        updated_at=None
                    )
                else:
                    raise "Not found"
        except HTTPException as error:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"message": "Entity not found"})
        return self.body_response
