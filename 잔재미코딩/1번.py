def outer_func():
    print('call outer_func function')
    
    # 중첩 함수의 정의
    def inner_func():
        return 'call inner_func function'
    
    # 중첩 함수 호출 
    print(inner_func())

outer_func()
def outer_func(num):
    # 중첩 함수에서 외부 함수의 변수에 접근 가능
    def inner_func():
        print(num)
        return 'complex'
    
    return inner_func

fn = outer_func(10)    # <--- First-class function
print(fn())            # <--- Closure 호출 