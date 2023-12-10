class DatabaseAuthInformation:
    def __init__(self):
        self.host = None
        self.port = None
        self.database_name = None
        self.username = None
        self.password = None

    def parse_auth_info(self, auth_filepath):
        try:
            with open(auth_filepath, 'r') as file:
                for line in file:
                    if not line.strip() or line.strip()[0] == '#':
                        continue

                    key, value = line.strip().split('=', 1)
                    if key == 'host':
                        self.host = value.strip()
                    elif key == 'port':
                        self.port = value.strip()
                    elif key == 'database':
                        self.database_name = value.strip()
                    elif key == 'username':
                        self.username = value.strip()
                    elif key == 'password':
                        self.password = value.strip()

        except Exception as e:
            print(e)
            return False

        if None in (self.host, self.port, self.database_name, self.username, self.password):
            return False

        return True

    def get_host(self):
        return self.host

    def get_port(self):
        return self.port

    def get_database_name(self):
        return self.database_name

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def debug_print(self):
        print(f"Host: {self.host}:{self.port}/{self.database_name}@{self.username}:{self.password}")