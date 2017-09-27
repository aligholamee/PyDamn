# Private variables :)
class Foo:
    def __init__(self):
        self.__private = 3.14
        print(self.__private)



foo = Foo()        # Prints 3.14

# runtime error(we have runtime only in python :D)
print(foo.__private)

# access the member
print(foo._Foo__private)
