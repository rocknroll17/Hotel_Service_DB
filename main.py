from DatabaseAuthInformation import DatabaseAuthInformation
import mysql.connector
import hashlib
import os


def main_menu():
    while True:
        print("=== Main Menu ===")
        print("1. 사용자 계정 추가")
        print("1. 사용자 계정 탈퇴")
        print("3. 종료")
        
        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            option_1()
        elif choice == "2":
            option_2()
        elif choice == "3":
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 메뉴를 선택하세요.")

def option_1():
    print("사용자 계정 추가: ")
    ID = input("ID: ")
    password = input("Password: ")
    print(ID, hash_password(password))

def option_2():
    print("옵션 2가 선택되었습니다.")

def hash_password(password):
    # 무작위 솔트 생성
    salt = os.urandom(16)
    hash = hashlib.sha256()
    hash.update(password.encode('utf-8'))
    return hash.hexdigest()


















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

main_menu()


# 결과 가져오기
result = cursor.fetchall()

# 결과 출력
for row in result:
    print(row)
# 연결 종료
cursor.close()
db.close()

'''
# SELECT 쿼리 실행
cursor.execute("""SELECT
FROM customer_info""")
'''
