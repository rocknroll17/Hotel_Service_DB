class user_controller:
    ID=None
    deleteID=None
    Password=None
    query=None

    FirstName=None
    LastName=None
    Email=None
    Phone=None
    config = {
    'FirstName': FirstName,
    'LastName': LastName,
    'Email': Email,
    'Phone': Phone,
    'ID': ID,
    'Password': Password
    }
    @staticmethod
    def set_insert_query():
        user_controller.query = "call CreateAccountInfo('%s', '%s', '%s', '%s', '%s', '%s');"%(user_controller.get_FirstName(),user_controller.get_LastName(),user_controller.get_Email(),user_controller.get_Phone(),user_controller.get_ID(),user_controller.get_Password())

    @staticmethod
    def set_delete_query():
        user_controller.query="DELETE account_info FROM account_info WHERE ID='%s'"%(user_controller.deleteID)

    @staticmethod
    def set_update_query():
        user_controller.query="UPDATE account_info SET password = %s WHERE ID = %s"%(user_controller.Password,user_controller.ID)

    @staticmethod
    def get_ID():
        return user_controller.ID

    @staticmethod
    def get_Password():
        return user_controller.Password

    @staticmethod
    def set_ID(ID):
        user_controller.ID = ID

    @staticmethod
    def set_Password(password):
        user_controller.Password = password

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