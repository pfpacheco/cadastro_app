from uuid import UUID
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class CadastroBodyRequest(BaseModel):
    name: str
    cnu: str
    description: str


class CadastroHttpRequest(BaseModel):
    body: CadastroBodyRequest


class CadastroBodyResponse(BaseModel):
    id: UUID
    name: str
    cnu: str
    description: str
    createdAt: datetime
    updatedAt: Optional[datetime]


class CadastroHttpResponse(BaseModel):

    code: int
    status: str
    body: Optional[CadastroBodyResponse]
