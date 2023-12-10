import hashlib
import os

class user_controller:
    ID=None
    deleteID=None
    Password=None
    query=None

    FirstName=None
    LastName=None
    Email=None
    Phone=None
    def hash_password(password):
        # 무작위 솔트 생성
        salt = os.urandom(16)
        hash = hashlib.sha256()
        hash.update(password.encode('utf-8'))
        return hash.hexdigest()
    
    @staticmethod
    def isresign():
        user_controller.query = "SELECT your_function('%s', '%s');"%(user_controller.ID,user_controller.Password)

    @staticmethod
    def login_account():
        user_controller.query = "call CreateAccountInfo('%s', '%s', '%s', '%s', '%s', '%s');"%(user_controller.FirstName,user_controller.LastName,user_controller.Email,user_controller.Phone,user_controller.ID,user_controller.Password)

    def resign_account():
        user_controller.query="UPDATE account_info SET Active = 0 WHERE ID='%s' AND Password = '%s'"%(user_controller.deleteID, user_controller.Password)

    @staticmethod
    def update_password():
        user_controller.query="UPDATE account_info SET Password = %s WHERE ID = %s"%(user_controller.Password,user_controller.ID)

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