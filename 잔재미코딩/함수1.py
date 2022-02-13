def greturn(a):
    b = a + 1
    return a,b
print(type(greturn(1)));
#//<class 'tuple'>

x = 1
y = 3
x, y = y, x;
print(x, y)


