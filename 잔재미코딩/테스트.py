def mark_bold(function):
    def wrapper(*args, **kwargs):
        return '<b>' + function(*args, **kwargs) + '</b>'
    return wrapper

def mark_italic(function):
    def wrapper(*args, **kwargs):
        return '<i>' + function(*args, **kwargs) + '</i>'
    return wrapper

@mark_bold
@mark_italic
def add_html(string):
    return string

print (add_html('안녕하세요'))

##############################################################################

def mark_html(tag):
    def outer_wrapper(function):
        def inner_wrapper(*args, **kwargs):
            return '<' + tag + '>' + function(*args, **kwargs) + '</' + tag + '>'
        return inner_wrapper
    return outer_wrapper

@mark_html('b')
def print_bold(title):
    return title

@mark_html('h1')
def print_title(title):
    return title

print(print_title('잔재미코딩 Dave Lee 입니다.'))