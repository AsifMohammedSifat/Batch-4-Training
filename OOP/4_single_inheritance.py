

class A:
    def __init__(self,name) -> None:
        self.name = name

    def display(self):
        print(self.name)


class B(A):
    def __init__(self, name) -> None:
        super().__init__(name)

obj = B("Sayed")
obj.display()