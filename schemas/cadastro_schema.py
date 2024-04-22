from datetime import datetime

from sqlalchemy import Column, UUID, String, DateTime
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Cadastro(Base):

    __tablename__ = "cadastro"

    id = Column(UUID, primary_key=True)
    name = Column(String, nullable=False)
    cnu = Column(String(20), unique=True)
    description = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, nullable=True)
