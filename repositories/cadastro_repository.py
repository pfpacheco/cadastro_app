from decouple import config
from datetime import datetime
from uuid import uuid4

from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine
from sqlalchemy.exc import SQLAlchemyError

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
            self.body_response = await self.find_by_cnu(cnu=cadastro["cnu"])
        except SQLAlchemyError as error:
            raise error
        finally:
            session.close()
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
        except SQLAlchemyError as error:
            raise error
        finally:
            session.close()
        return self.body_response
