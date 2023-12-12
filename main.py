from DatabaseAuthInformation import DatabaseAuthInformation
import mysql.connector
import hashlib
import os
from db_control import *
import os
import time

def login():
    os.system('cls')
    global islogin
    print("=== 로그인 ===")
    if islogin:
        print("이미 로그인 되어 있습니다.")
        return
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
        global ID, CustomerId, FirstName, LastName, Grade
        islogin = True
        ID, CustomerId, FirstName, LastName, Grade = result[0]
        time.sleep(3)
        os.system('cls')

def logout():
    os.system('cls')
    global islogin, ID, CustomerId, FirstName, LastName, Grade
    islogin = False
    ID = ''
    CustomerId = ''
    FirstName = ''
    LastName = ''
    FirstName = ''
    Grade = ''
    print("로그아웃 되었습니다.")
    time.sleep(3)
    os.system('cls')
    return


def add_account():
    os.system('cls')
    print("=== 회원가입 ===")
    print("회원가입: ")
    ID = (input("ID: "))
    Password = hash_password(input("비밀번호: "))
    RePassword = hash_password(input("새 비밀번호 확인: "))
    if Password != RePassword:
        print("비밀번호가 다릅니다.")
        time.sleep(3)
        os.system('cls')
        return
    FirstName = input("FirstName: ")
    LastName = input("LastName: ")
    Email = input("Email: ")
    Phone = input("Phone: ")
    cursor.callproc('CreateAccountInfo', args=(FirstName,LastName,Email,Phone,ID,Password))
    db.commit()
    print("회원가입이 완료 되었습니다. 되었습니다.")
    time.sleep(3)
    os.system('cls')
    return
    
def change_password():
    os.system('cls')
    print("=== 비밀번호 변경 ===")
    if not islogin:
        print("로그인을 해야 이용할 수 있는 서비스입니다.")
        return
    print("비밀번호 변경")
    OldPassword = hash_password(input("기존 비밀번호: "))
    cursor.execute("SELECT check_user_existence('%s', '%s')"%(ID, OldPassword))
    if cursor.fetchone()[0]:
        NewPassword = hash_password(input("새 비밀번호: "))
        RePassword = hash_password(input("새 비밀번호 확인: "))
        if NewPassword == RePassword:
            cursor.execute("UPDATE account_info SET Password = '%s' WHERE ID = '%s'"%(NewPassword, ID))
            db.commit()
        else:
            print("비밀번호가 다릅니다.")
            time.sleep(3)
            os.system('cls')
            return
    else:
        print("비밀번호가 틀렸습니다.")
        time.sleep(3)
        os.system('cls')
        return

def resign():
    os.system('cls')
    print("=== 회원 탈퇴 ===")
    OldPassword = hash_password(input("탈퇴를 하려면 비밀번호를 입력하세요: "))
    cursor.execute("SELECT check_user_existence('%s', '%s')"%(ID, OldPassword))
    if cursor.fetchone()[0]:
        cursor.execute("UPDATE account_info SET Active = 0 WHERE ID='%s' AND Password = '%s'"%(ID, OldPassword))
    else:
        print("회원 정보가 잘못 되었습니다.")
        return
    db.commit()
    print("회원 탈퇴되어 자동 로그아웃 됩니다. 한달 안에 다시 로그인 시 탈퇴가 취소됩니다.")
    time.sleep(3)
    os.system('cls')
    logout()

def hash_password(password):
    # 무작위 솔트 생성
    salt = os.urandom(16)
    hash = hashlib.sha256()
    hash.update(password.encode('utf-8'))
    return hash.hexdigest()

def reservation():
    os.system('cls')
    print("=== 객실 예약 ===")
    if not islogin:
        print("로그인을 해야 이용할 수 있는 서비스입니다.")
        time.sleep(3)
        os.system('cls')
        return
    
    #여기에 코드 넣어서 해결
    print("객실타입 번호|타입|설명|최대인원수")
    cursor.execute("SELECT RoomTypeID,Typename,Description,Capacity FROM room_type_info");
    data = cursor.fetchall()
    count_rooms = len(data)
    for room in data:
        #룸 타입 출력
        print(room)
    room_type_number = int(input("예약하고 싶은 객실 타입 번호를 입력해주세요."))
    print("선택한 객실 타입")
    print(data[room_type_number-1])
    cursor.execute("SELECT * "
                   "FROM room_info ri "
                   "JOIN room_capacity_info rc ON ri.RoomID = rc.RoomID "
                   "WHERE ri.RoomTypeID = '%s';"%(room_type_number))
    result = cursor.fetchall()
    if result == None:
        print("해당하는 객실번호는 없는 객실입니다.")
        return
    #여러개의 객실이 나올 수 있음. 이때 하나라도 tinyint 값이 1인것이 나오면 예약이 가능하다는 이야기임.
    for room in result:
        #룸 예약이 가능하다면
        #=Tinyint 값이 1이라면
        if(room[5]==1):
            print("해당하는 객실은 현재 이용이 가능합니다.")
            print("1 : 예약한다")
            print("2 : 예약하지 않는다")
            ans = input("값을 입력해주세요")
            if (ans == "1"):
                cursor.execute("UPDATE room_capacity_info SET Available=0 WHERE RoomID='%s';" % (room[0]));
                db.commit();
                return
    #for문을 나왔다는 이야기는 룸 예약이 불가능하다는 것
    print("해당하는 객실번호는 현재 이용할 수 없는 객실입니다.")
    return

    os.system('cls')

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
    if not islogin:
        print("=== Main Menu ===")
        print("1. 로그인")
        print("2. 회원가입")
        print("3. 종료")
        choice = input("메뉴를 선택하세요: ")
        if choice == "1":
            login()
        elif choice == "2":
            add_account()
        elif choice == "3":
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 메뉴를 선택하세요.")
    else:
        print("사용자: %s %s"%(FirstName, LastName))
        print("ID: %s"%(ID))
        print("=== Main Menu ===")
        print("1. 객실 예약")
        print("2. 비밀번호 변경")
        print("3. 탈퇴")
        print("4. 로그아웃")
        print("5. 종료")
        choice = input("메뉴를 선택하세요: ")
        
        
        if choice == "1":
            reservation()
        elif choice == "2":
            change_password()
        elif choice == "3":
            resign()
        elif choice == "4":
            logout()
        elif choice == "5":
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 메뉴를 선택하세요.")
            time.sleep(3)
            os.system('cls')

# 결과 출력

# 연결 종료
cursor.close()
db.close()

'''
# SELECT 쿼리 실행
cursor.execute("""SELECT
FROM customer_info""")
'''
