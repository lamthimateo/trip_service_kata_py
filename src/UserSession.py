from DependendClassCallDuringUnitTestException import DependendClassCallDuringUnitTestException


# Singleton class to manage user session.
class UserSession:
    _instance = None

    @staticmethod
    def get_instance():
        # Returns the singleton instance of UserSession.
        if UserSession._instance is None:
            UserSession._instance = UserSession()
        return UserSession._instance

    def get_logged_user(self):
        # Raises an exception in unit tests to prevent real session access.
        raise DependendClassCallDuringUnitTestException(
            "UserSession.get_logged_user should not be called during a unit test.")
