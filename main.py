from DatabaseAuthInformation import DatabaseAuthInformation
import mysql.connector
import hashlib
import os
from db_control import *

def main_menu():
    while True:
        print("=== Main Menu ===")
        print("1. 사용자 계정 추가")
        print("2. 사용자 계정 탈퇴")
        print("3. 종료")
        
        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            add_account()
        elif choice == "2":
            resign()
        elif choice == "3":
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 메뉴를 선택하세요.")

def add_account():
    print("사용자 계정 추가: ")
    user_controller.set_ID(input("ID: "))
    user_controller.set_Password(input("Password: "))
    user_controller.set_FirstName(input("FirstName: "))
    user_controller.set_LastName(input("LastName: "))
    user_controller.set_Email(input("Email: "))
    user_controller.set_Phone(input("Phone: "))
    print(hash_password(user_controller.Password))
    cursor.callproc('CreateAccountInfo', args=(user_controller.FirstName,user_controller.LastName,user_controller.Email,user_controller.Phone,user_controller.ID,hash_password(user_controller.Password)))
    db.commit()


def hash_password(password):
    # 무작위 솔트 생성
    salt = os.urandom(16)
    hash = hashlib.sha256()
    hash.update(password.encode('utf-8'))
    return hash.hexdigest()

def resign():
    user_controller.set_ID(input("ID: "))



















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
#cursor.execute("INSERT INTO customer_info (CustomerID, FirstName, LastName, Email, Phone, Grade) VALUES (16, 'John', 'Kim', 'john.kim@example.com', '122-456-7890', 'Gold');")

main_menu()

# 결과 출력

# 연결 종료
cursor.close()
db.close()

'''
# SELECT 쿼리 실행
cursor.execute("""SELECT
FROM customer_info""")
'''
