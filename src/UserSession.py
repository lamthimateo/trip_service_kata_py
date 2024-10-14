class UserSession:
    _instance = None

    @staticmethod
    def get_instance():
        if UserSession._instance is None:
            UserSession._instance = UserSession()
        return UserSession._instance

    def get_logged_user(self):
        # This method should return the logged-in user or None if not logged in.
        pass
