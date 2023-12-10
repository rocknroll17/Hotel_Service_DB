class user_controller:
    username=None
    password=None
    insert_user_query=None

    def set_insert_query(self):
        insert_user_query = "INSERT account_info (username,password) VALUES (%s,%s)"

    def getUsername(self):
        return self.username
    def getPassword(self):
        return self.password
    def set_username(self,username):
        self.username = username
    def set_password(self,password):
        self.password = password