class user_controller:
    username=None
    password=None

    @staticmethod
    def set_insert_query():
        return "INSERT account_info (ID,Password) VALUES (%s,%s)" %(user_controller.getUsername(), user_controller.getPassword())
    
    @staticmethod
    def getUsername():
        return user_controller.username
    
    @staticmethod
    def getPassword():
        return user_controller.password
    
    @staticmethod
    def set_username(username):
        user_controller.username = username

    @staticmethod
    def set_password(password):
        user_controller.password = password