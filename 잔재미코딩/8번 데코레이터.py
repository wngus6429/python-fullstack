# 데코레이터
def outer_func(function):
    def inner_func(digit1, digit2):
        if digit2 == 0:              # <--- 유효성 검사의 예
            print('cannot be divided with zero')
            return
        function(digit1, digit2)
    return inner_func
# 데코레이터 사용하기 (유효성 검사)
@outer_func
def divide(digit1, digit2):
    print (digit1 / digit2)

divide(4, 2)
divide(9, 0)

# 데코레이터
def type_checker(function):
    def inner_func(digit1, digit2):
        if (type(digit1) != int) or (type(digit2) != int):                       # <--- 유효성 검사의 예
            print('the only int is supported')
            return 
        return function(digit1, digit2)
    return inner_func
# 데코레이터 사용하기 (유효성 검사)
@type_checker
def divide(digit1, digit2):
    return digit1 * digit2

divide(0.1, 1)