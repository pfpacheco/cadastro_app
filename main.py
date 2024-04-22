from fastapi import FastAPI

from controllers.cadastro_controller import CadastroController
from models.cadastro_model import CadastroHttpRequest, CadastroHttpResponse


app = FastAPI()
cadastro_controller = CadastroController()


@app.post("/rest/api/cadastro/add")
async def add_cadastro(req: CadastroHttpRequest) -> CadastroHttpResponse:
    if req.body:
        cadastro = req.body.dict()
        resp = await cadastro_controller.add_cadastro(cadastro=cadastro)
        return resp
