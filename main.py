from DatabaseAuthInformation import DatabaseAuthInformation
import mysql.connector
import hashlib
import os
from db_control import *
import os
import time

def login():
    login_ID = input("ID: ")
    Password = input("Password: ")
    cursor.execute("SELECT login('%s', '%s')" % (login_ID, hash_password(Password)))
    result = cursor.fetchone()[0]
    os.system('cls')
    if result == 0:
        print("로그인 실패")
    else:
        if result == 2:
            print("탈퇴를 신청한 회원입니다. 탈퇴를 취소합니다.")
        print("로그인 성공")
        cursor.execute("""SELECT a.ID, a.CustomerID, c.Firstname, c.Lastname, c.Grade
FROM account_info a
JOIN customer_info c ON a.customerID = c.customerID
WHERE a.ID = '%s' AND a.Password = '%s';""" % (login_ID, hash_password(Password)))
        result = cursor.fetchall()
        #print(result)
        global islogin, ID, CustomerId, FirstName, LastName, Grade
        islogin = True
        ID, CustomerId, FirstName, LastName, Grade = result[0]
        time.sleep(3)
        os.system('cls')

def add_account():
    print("사용자 계정 추가: ")
    ID = (input("ID: "))
    Password = input("Password: ")
    FirstName = input("FirstName: ")
    LastName = input("LastName: ")
    Email = input("Email: ")
    Phone = input("Phone: ")
    cursor.callproc('CreateAccountInfo', args=(FirstName,LastName,Email,Phone,ID,hash_password(Password)))
    db.commit()

def resign():
    ID = input("ID: ")
    Password = input("Password: ")
    cursor.execute("UPDATE account_info SET Active = 0 WHERE ID='%s' AND Password = '%s'"%(ID, hash_password(Password)))
    db.commit()

def hash_password(password):
    # 무작위 솔트 생성
    salt = os.urandom(16)
    hash = hashlib.sha256()
    hash.update(password.encode('utf-8'))
    return hash.hexdigest()

def reservation():
    if not islogin:
        print("로그인을 해야 이용할 수 있는 서비스입니다.")
        return



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
os.system('cls')
print("데이터 베이스에 성공적으로 연결 했습니다.",end="")
time.sleep(0.7)
print(".",end="")
time.sleep(0.7)
print(".")
time.sleep(0.7)
os.system('cls')
# 커서 생성
cursor = db.cursor()
islogin = False
ID = ''
CustomerId = ''
FirstName = ''
LastName = ''
FirstName = ''
Grade = ''
while True:
    if islogin:
        print("사용자: %s %s"%(FirstName, LastName))
        print("ID: %s"%(ID))
    print("=== Main Menu ===")
    print("1. 로그인")
    print("2. 사용자 계정 추가")
    print("3. 사용자 계정 탈퇴")
    print("4. 객실 예약")
    print("5. 종료")
        
    choice = input("메뉴를 선택하세요: ")
    if choice == "1":
        login()
    elif choice == "2":
        add_account()
    elif choice == "3":
        resign()
    elif choice == "4":
        reservation()
    elif choice == "5":
        print("프로그램을 종료합니다.")
        break
    else:
         print("올바른 메뉴를 선택하세요.")

# 결과 출력

# 연결 종료
cursor.close()
db.close()

'''
# SELECT 쿼리 실행
cursor.execute("""SELECT
FROM customer_info""")
'''
