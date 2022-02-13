def outer_func(num):
    # 중첩 함수에서 외부 함수의 변수에 접근 가능
    def inner_func():
        print(num)
        return '안녕'
    
    return inner_func                 # 중첩 함수 이름을 리턴합니다.
closure_func = outer_func(10)    # <--- First-class function
closure_func()            # <--- Closure 호출 
del outer_func
closure_func()