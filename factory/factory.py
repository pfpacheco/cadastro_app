from services.cadastro_service import CadastroService


class ServiceFactory:
    """
    Factory class for creating service instances.
    """

    @staticmethod
    def get_service(name):
        """
        Get an instance of the requested service.

        Args:
            name (str): The name of the service to instantiate.

        Returns:
            object: An instance of the requested service, or None if the name is not recognized.
        """
        if name == "cadastro":
            return CadastroService()
