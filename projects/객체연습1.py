class Dave:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
    def what(self):
        return self.width * self.height
    def set_area(self, data1, data2):
        self.width = data1 
        self.height = data2

square1 = Dave(10, 50, 'red')
square2 = Dave(20, 100, 'black')
wngus = Dave(8, 18, 'black')
wngus.set_area(18, 18)

print(square1)
print(square1.width, square1.height)
print(square1.what())
print(wngus.width)
print(wngus.what())