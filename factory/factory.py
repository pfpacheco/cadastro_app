from services.cadastro_service import CadastroService


class ServiceFactory:

    @staticmethod
    def get_service(name):
        if name == "cadastro":
            cadastro_service = CadastroService()
            return cadastro_service
        elif name == "some else":
            return None
