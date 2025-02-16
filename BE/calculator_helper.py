# import logger

print(" we are in the cal-helper.py file")


class CalculatorHelper():
    log_properties = {
        'custom_dimensions': {
            'userId': 'ahmed_elhasan'
        }
    }

    _instance = None
    _is_initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CalculatorHelper, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._is_initialized:
            self._user_list = []
            self._current_user = None
            admin = self.User('admin', 'test1234')
            self._user_list.append(admin)
            self._is_initialized = True
        #    self.logger = logger.get_logger(__name__)

    class User():
        def __init__(self, username, password):
            self.username = username
            self.password = password

        def __repr__(self):
            return f"User(username={self.username}, password={self.password})"

        print("here we are inside adding function")

    def add(self, a, b):
        # self.logger.debug("test")
        # self.logger.debug("some message", extra=self.log_properties)
        print("here we are inside adding function")
        # self.logger.debug(
        # f"adding {b} with {a} results in {a + b}", extra=self.log_properties)
        result = a+b
        return result
    print("here we are after the adding function")

    def subtract(self, a, b):
        # self.logger.debug(
        # f"Subtracting {b} from {a} results in {a - b}", extra=self.log_properties)
        result = a - b

        return result

    def multiply(self, a, b):
        res = a*b
        # self.logger.debug(
        # f"multiply {b} with {a} results in {res}", extra=self.log_properties)

        return res

    def divide(self, a, b):
        # self.logger.debug(
        # f"dividing {b} from {a} results in { a / b}", extra=self.log_properties)
        res = a/b
        return res

    def register_user(self, username, password):
        for user in self._user_list:
            if (user.username == username):
                return None
        user = self.User(username, password)
        self._user_list.append(user)
        return username

    def login(self, username, password):
        for user in self._user_list:
            if (user.username == username and user.password == password):
                self._current_user = user
                return username
        return None

    def logout(self):
        user = self._current_user
        self._current_user = None
        return user

    def get_current_user(self):
        return self._current_user
