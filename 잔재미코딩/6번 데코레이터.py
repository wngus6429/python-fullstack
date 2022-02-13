# 시간을 앞뒤로 추가하고 싶다.
# 이렇게 넣으면 됩니다.
import datetime
def logger_login():
    print (datetime.datetime.now())
    print ("Dave login")
    print (datetime.datetime.now())
#logger_login()


# 데코레이터 작성하기
def datetime_decorator(func):           # <--- datetime_decorator 는 데코레이터 이름, func 가 이 함수 안에 넣을 함수가 됨
    def wrapper():                      # <--- 호출할 함수를 감싸는 함수
        print ('time ' + str(datetime.datetime.now())) # <--- 함수 앞에서 실행할 내용
        func()                          # <--- 함수  
        print (datetime.datetime.now()) # <--- 함수 뒤에서 실행할 내용
    return wrapper                      # <--- closure 함수로 만든다.

# 데코레이터 적용하기
@datetime_decorator    # @데코레이터
def logger_login_david():
     print ("David login")

logger_login_david()

@datetime_decorator    # @데코레이터
def logger_login_anthony():
     print ("Anthony login")

logger_login_anthony()

@datetime_decorator    # @데코레이터
def logger_login_tina():
     print ("Tina login")

logger_login_tina()