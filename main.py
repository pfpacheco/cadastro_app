from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException

from controllers.cadastro_controller import CadastroController
from models.cadastro_model import CadastroHttpRequest, CadastroHttpResponse


app = FastAPI()
cadastro_controller = CadastroController()


@app.post("/rest/api/cadastro/add")
async def add_cadastro(req: CadastroHttpRequest) -> CadastroHttpResponse:
    if req.body:
        return await cadastro_controller.add_cadastro(cadastro=req.body.dict())
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"error": "Request not valid!"})

