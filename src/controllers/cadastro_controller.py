from src.factory.factory import ServiceFactory
from src.models.cadastro_model import CadastroHttpResponse


class CadastroController:
    """
    Controller class for Cadastro-related operations.
    """

    @staticmethod
    async def add_cadastro(cadastro) -> CadastroHttpResponse:
        """
        Add a new Cadastro.

        Args:
            cadastro: The data for the new Cadastro.

        Returns:
            CadastroHttpResponse: The HTTP response containing the saved Cadastro.
        """
        return await ServiceFactory.get_service(service_name="cadastro").add_cadastro(cadastro=cadastro)
