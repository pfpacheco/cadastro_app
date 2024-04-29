from decouple import config

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database:

    def __init__(self):
        self.database_url = config("POSTGRES_URL")
        self.engine = create_engine(self.database_url, connect_args={"check_same_thread": False})
        self.session_local = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_db(self):
        db = self.session_local()
        try:
            yield db
        finally:
            db.close()
