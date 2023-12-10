from DatabaseAuthInformation import DatabaseAuthInformation
import mysql.connector

# Create an instance of DatabaseAuthInformation
db_info = DatabaseAuthInformation()

# Path of the MySQL authentication file
auth_filepath = "mysql.auth"

# Parse the authentication information
if not db_info.parse_auth_info(auth_filepath):
    print("File open has been failed.")
    exit()

# Construct the database connection URL
db_connection_url = f"mysql://{db_info.get_username()}:{db_info.get_password()}@{db_info.get_host()}:{db_info.get_port()}/{db_info.get_database_name()}"
# Establish the database connection
db = mysql.connector.connect(host=db_info.get_host(),
                                        port=db_info.get_port(),
                                        user=db_info.get_username(),
                                        password=db_info.get_password(),
                                        database=db_info.get_database_name())
print("Database connection succeeded.")

# 커서 생성
cursor = db.cursor()

# SELECT 쿼리 실행
cursor.execute("""SELECT ID, name
FROM student
WHERE ID = 1000""")

# 결과 가져오기
result = cursor.fetchall()

# 결과 출력
for row in result:
    print(row)
# 연결 종료
cursor.close()
db.close()