'''class WaltonUsta:
    # Our new car class
    def drving(self):
        run_the_car
    def music(self):
        run_the_music
    def fuel(self):
        load_the_fuel
    def horn(self):
        make_sound_pollution

our_car=WaltonUsta()
her_car=WaltonUsta()
your_car=WaltonUsta()
    '''

'''class Calculator:
    #Do addition,Subtraction,Multiplication and Division.
    def addition(self,a,b):
        return a+b
    def subtraction(self,a,b):
        return a-b
    def multiplication(self,a,b):
        return a*b
    def division(self,a,b):
        try:
            return a/b
        except ZeroDivisionError:
             return 'It is impossible to divide by zero.'

class SuperCalculator(Calculator):
    #child class of Calculator.Do square and cube.
    def square(self, a):
        return a*a
    def cube(self, a):
        return a*a*a
    
my_calculator=SuperCalculator()
temp=my_calculator.addition(23,47)
print(temp)

temp=my_calculator.subtraction(87,54)
print(temp)

temp=my_calculator.multiplication(65,56)
print(temp)

temp=my_calculator.division(852,76)

print( temp)

temp=my_calculator.square(7)

print( temp)

temp=my_calculator.cube(3)

print( temp)'''


'''class Calculator:
     #Do addition,subtraction,multiplication and division
          def __init__(self, a, b):
              self.a=a
              self.b=b
          def addition(self):
              return self.a+self.b

          def subtraction(self):
              return self.a-self.b

          def multiplication(self):
              return self.a*self.b

          def division(self):
              try:
                  return self.a/self.b
              except ZeroDivisionError:
                  return 'It is impossible to divide by zero.'


my_calculator=Calculator(45,3)

temp=my_calculator.addition()
print(temp)

temp=my_calculator.subtraction()
print(temp)

temp=my_calculator.multiplication()
print(temp)

temp=my_calculator.division()
print(temp)'''

'''class SuperCalculator:
    #Do addition,subtractor,multiplication,division, square and cube
    def addition(self,a,b):
       return a+b

    def subtraction(self,a,b):
        return a-b

    def multiplication(self,a,b):
        return a*b
    def division(self,a,b):
        try:
            return a/b
        except ZeroDivisionError:
            return 'It is impossible to divide by zero.'
    def square(self,a):
        return a*a
    def cube(self,a):
        return a*a*a
my_Calculator=SuperCalculator()
temp=my_Calculator.addition(23,47)
print(temp)

temp=my_Calculator.subtraction(87,54)
print(temp)

temp=my_Calculator.multiplication(65,56)
print(temp)

temp=my_Calculator.division(852,76)
print(temp)

temp=my_Calculator.square(7)
print(temp)

temp=my_Calculator.cube(3)
print(temp)'''
    

'''class CustomError(Exception):
    #just for example

    def __init__(self,message):
        self.message=message
try:
    raise CustomError('It is an custom error.')
except CustomError as e:
    print(e)'''

class Calculator:
    #Do addition,subtraction,multiplication and division
    def addition(self,a,b):
        return a+b
    def subtraction(self,a,b):
        return a-b
    def multiplication(self,a,b):
        return a*b
    def division(self,a,b):
        try:
            return a/b
        except ZeroDivisionError:
            return 'It is impossible to divide by zero.'
class SuperCalculator(Calculator):
    #Do addition,subtraction,multiplication,division,square and cube
    def addition(self,a,b,c):
        return a+b+c
    def square(self,a):
        return a*a
    def cube(self,a):
        return a*a*a
my_Calculator=SuperCalculator()

temp=my_Calculator.addition(23,47,22)
print(temp)

temp=my_Calculator.subtraction(87,54)
print(temp)

temp=my_Calculator.multiplication(65,56)
print(temp)

temp=my_Calculator.division(852,76)
print(temp)

temp=my_Calculator.square(7)
print(temp)

temp=my_Calculator.cube(3)
print(temp)        
        
    
