def h1(name='yasoob'):
    print('现在您在hi（）函数中')

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    print(greet())
    print(welcome())
    print("now you are back in the hi() function")

print(h1())


