class BaseAPI:
    def __init__(self):
        self.__token="ABC123SECRET"

    def _gettoken(self):
        return self.__token

class UserAPI(BaseAPI):
    def get_user_data(self):
        print("Fetching user data using token:", self._gettoken())

obj_user=UserAPI()
obj_user.get_user_data()