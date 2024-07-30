from datetime import datetime

from sqlalchemy import Column, UUID, String, DateTime
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Cadastro(Base):
    """
    Represents a Cadastro entity in the database.
    """

    __tablename__ = "t_cadastro"

    uuid = Column(UUID, primary_key=True)
    name = Column(String, nullable=False)
    cnu = Column(String(20), unique=True, nullable=False)  # Assuming 20 is the maximum length
    description = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"Cadastro(id={self.id}, name={self.name}, cnu={self.cnu}, description={self.description}, " \
               f"created_at={self.created_at}, updated_at={self.updated_at})"

    def update_timestamps(self):
        """
        Update the timestamps (created_at and updated_at) for the Cadastro entity.
        """
        self.updated_at = datetime.now()
