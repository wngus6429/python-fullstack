#파라미터와 관계없이 모든 함수에 적용 가능한 Decorator 만들기
#파라미터는 어떤 형태이든 결국 (args, **kwargs) 로 표현 가능
#데코레이터의 내부함수 파라미터를 (args, **kwargs) 로 작성하면 어떤 함수이든 데코레이터 적용 가능

# 데코레이터 작성하기
def general_decorator(function):
    def wrapper(*args, **kwargs):
        print('function is decorated')
        return function(*args, **kwargs)
    return wrapper

# 데코레이터 적용하기
@general_decorator
def calc_square(digit):
    return digit * digit

@general_decorator
def calc_plus(digit1, digit2):
    return digit1 + digit2

@general_decorator
def calc_quad(digit1, digit2, digit3, digit4):
    return digit1 * digit2 * digit3 * digit4

# 함수 호출하기
print (calc_square(2))
print (calc_plus(2, 3))
print (calc_quad(2, 3, 4, 5))