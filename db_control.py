class user_controller:
    ID=None
    deleteID=None
    Password=None
    query=None

    FirstName=None
    LastName=None
    Email=None
    Phone=None

    @staticmethod
    def set_insert_query():
        user_controller.query = "INSERT account_info (username,password) VALUES (%s,%s)"%(user_controller.ID,user_controller.Password)

    @staticmethod
    def set_delete_query():
        user_controller.query="DELETE account_info FROM account_info WHERE ID='%s'"%(user_controller.deleteID)

    @staticmethod
    def set_update_query():
        user_controller.query="UPDATE account_info SET password = %s WHERE ID = %s"%(user_controller.Password,user_controller.ID)
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

    @staticmethod
    def get_FirstName():
        return user_controller.FirstName
    @staticmethod
    def get_LastName():
        return user_controller.LastName
    @staticmethod
    def get_Email():
        return user_controller.Email
    @staticmethod
    def get_Phone():
        return user_controller.Phone

    #customer column 관련 setter
    @staticmethod
    def set_FirstName(firstName):
        user_controller.FirstName =firstName
    @staticmethod
    def set_LastName(lastName):
        user_controller.LastName =lastName
    @staticmethod
    def set_Email(email):
        user_controller.Email =email
    @staticmethod
    def set_Phone(phone):
        user_controller.Phone =phone