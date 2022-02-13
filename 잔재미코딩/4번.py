def logger(msg):
    message = msg
    def msg_creator():    # <--- 함수 안에 함수를 만들 수도 있음
        print ('[HIGH LEVELS]: ', msg)
    return msg_creator
log1 = logger('Dave Log-in')
log2 = logger("Park Juhyun")
log1()
log2()

def html_creator(tag):
    def text_wrapper(msg):
        print ('<{0}>{1}</{0}>'.format(tag, msg))
    return text_wrapper
h1_html_creator = html_creator('h1') #1
h1_html_creator('H1 태그는 타이틀을 표시')
h1_html_creator2 = html_creator('p') #1
h1_html_creator2('p 태그는 설명을 표시')

def list_creator(tag):
    def text_wrapper(list_data):
        for item in list_data:
            print ('{0} {1}'.format(tag, item))
    return text_wrapper

data_list_minus = list_creator('-')
data_list_minus(['안녕', '하세요'])

data_list_mul = list_creator('*')
data_list_mul(['안녕', '하세요'])

data_list_x = list_creator('X')
data_list_x(['안녕', '하세요'])