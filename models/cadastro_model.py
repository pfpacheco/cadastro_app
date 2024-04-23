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
    id: str
    name: str
    cnu: str
    description: str
    created_at: datetime
    updated_at: Optional[datetime]


class CadastroHttpResponse(BaseModel):
    body: Optional[CadastroBodyResponse]
