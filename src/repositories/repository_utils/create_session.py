from decouple import config

from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine
from sqlalchemy.exc import SQLAlchemyError

from fastapi import status
from fastapi.exceptions import HTTPException


class CreateSession:

    def __init__(self):
        self.db_url = config("POSTGRES_URL")
        self.engine = create_engine(url=self.db_url)
        self.session = sessionmaker(bind=self.engine)

    def get_new_session(self):
        try:
            return self.session()
        except SQLAlchemyError as error:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail={"error": f"{error.__cause__}"})
