


class Calculator:
    def sum(self,num1,num2,num3=None):
       if num3 is None:
           return num1+num2
       return num1+num2+num3
    
    
cal = Calculator()
print(cal.sum(1,2,3))
print(cal.sum(1,2))