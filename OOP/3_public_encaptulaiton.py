
class A:
    __value = 5
    def __init__(self) -> None:
        pass
    def display(self):
        print(self.__value)

obj = A()

obj.__value = 10
print(obj.__value)
obj.display()

print(obj.__dict__)