from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class CadastroRequestBody(BaseModel):
    """
    Represents the request body for creating a new Cadastro.

    Attributes:
        name (str): The name of the Cadastro.
        cnu (str): The CNU (Customer Number) of the Cadastro.
        description (str): The description of the Cadastro.
    """
    name: str
    cnu: str
    description: str


class CadastroResponseBody(BaseModel):
    """
    Represents the response body for a Cadastro.

    Attributes:
        id (str): The unique identifier of the Cadastro.
        name (str): The name of the Cadastro.
        cnu (str): The CNU (Customer Number) of the Cadastro.
        description (str): The description of the Cadastro.
        created_at (datetime): The timestamp when the Cadastro was created.
        updated_at (Optional[datetime]): The timestamp when the Cadastro was last updated (optional).
    """
    id: str
    name: str
    cnu: str
    description: str
    created_at: datetime
    updated_at: Optional[datetime]


class CadastroHttpRequest(BaseModel):
    """
    Represents an HTTP request for creating a new Cadastro.

    Attributes:
        body (CadastroRequestBody): The request body containing Cadastro information.
    """
    body: CadastroRequestBody


class CadastroHttpResponse(BaseModel):
    """
    Represents an HTTP response for Cadastro-related operations.

    Attributes:
        body (Optional[CadastroResponseBody]): The response body containing Cadastro information (optional).
    """
    body: Optional[CadastroResponseBody]
