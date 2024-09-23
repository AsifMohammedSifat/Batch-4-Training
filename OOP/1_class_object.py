
class A:
    value = 5 #class variable
    def __init__(self) -> None:
        print("I am Constructor")
    
    def display(self):
        print("I am method")

    def __del__(self):
        print("I am destructor")

    def __str__(self) -> str:
        return "I am ClasS A"




obj = A()
obj1 = A()
obj.display()
obj.value = 5

print(obj.__dict__)





print(obj.value)
print(A.value)






