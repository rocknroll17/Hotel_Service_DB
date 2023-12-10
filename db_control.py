class user_controller:
    username=None
    password=None
    insert_user_query=None

    def set_insert_query():
        insert_user_query = "INSERT account_info (username,password) VALUES (%s,%s)"

    def getUsername():
        return user_controller.username
    def getPassword():
        return user_controller.password
    def set_username(username):
        user_controller.username = username
    def set_password(password):
        user_controller.password = password