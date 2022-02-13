def calc_square(digit):
    return digit * digit

def calc_plus(digit):
    return digit + digit

def calc_quad(digit):
    return digit * digit * digit * digit

def list_square(function, digit_list):
    result = list()
    for digit in digit_list:
        result.append(function(digit)) 
    print (result)

num_list = [1, 2, 3, 4, 5]

list_square(calc_square, num_list)
list_square(calc_plus, num_list)
list_square(calc_quad, num_list)

