# decorator 함수 정의
def outer_func(function):
    def inner_func():
        print('decoration added')
        function()
    return inner_func

# decorating할 함수
def log_func():
    print('logging')

# 본래 함수
#log_func()

# log_func 함수에 inner_func 함수의 기능을 추가한 decorated_func 함수
decorated_func = outer_func(log_func)
decorated_func()  # <--- 결과는 데코레이터를 사용할 때와 동일함

@outer_func
def logg_func():
    print('로깅')

logg_func()