from controllers.cadastro_controller import CadastroController
from models.cadastro_model import CadastroHttpRequest, CadastroHttpResponse
from fastapi import FastAPI


app = FastAPI()
cadastro_controller = CadastroController()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/rest/api/cadastro/add")
async def add_cadastro(req: CadastroHttpRequest) -> CadastroHttpResponse:
    if req.body:
        cadastro = req.body.dict()
        resp = await cadastro_controller.add_cadastro(cadastro=cadastro)
        return resp
