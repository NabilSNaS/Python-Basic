def counter(num):
    print(num)
    num+=1
    counter(num)

counter(1)
'''print('Please input your number:')
number=int(input())
temp=number
while number>1:
    number-=1
    temp=temp*number
if temp==0:
    print(1)
else:
    print(temp)'''


'''def factorial(number):
     if number==0:
         return 1
     else:
         return number*factorial(number-1)
print('Please input your number:')
number=int(input())
print(factorial(number))'''

'''sum=lambda a ,b : a+b
print(sum(10,20))
print((lambda a,b :a+b)(10,20))'''

'''def my_function(func,arg1,arg2):
    return func(arg1,arg2)
print(my_function(lambda a,b : a+b,10,20))'''

'''my_list=[2,3,4,5,6,7]
def square(x):
    return x*x
new_list = map(square,my_list)
print(new_list)
print(list(new_list))'''

'''my_list=[2,3,4,5,6,7]
def is_even(x):
    if (x%2)==0:
        return True
    else:
        return False
new_list=filter(is_even,my_list)
print(new_list)
print(list(new_list))'''

'''print("Please input three integers:")
a,b,c=map(int,input().split())
if a>=b and a>=c:
    greatest = a
elif b>=a and b>=c:
    greatest = b
else:
    greatest =c
print(greatest)'''

'''def gcd(a,b):
    if b>a:
        gcd(b,a)
    while b!=0:
        temp=a%b
        a=b
        b=temp
    return a
print("Please input two integers:")
a,b=map(int,input().split())
print(gcd(a,b))'''

'''def gcd(a,b):
    if b>a:
        gcd(b,a)
    while b!=0:
        temp=a%b
        a=b
        b=temp
    return a
def lcm(a,b):
    return(a*b)//gcd(a,b)
print("Please input two integers:")
a,b=map(int,input().split())
print(lcm(a,b))'''

def is_prime(n):
    if n <= 1:
            raise ValueError("The number must be greater than 1.")
    elif n<=3:
        return True
    elif(n%2)==0 or (n%3)==0:
        return False
    else:
        i=5
        while (i*i)<=n:
            if(n%i)==0 or (n% i+2)==0:
                return False
            i=i+6
        return True
        
print("Please input your number:")
number=int(input())

if is_prime(number):
    print(number,'is a prime number.')
else:
    print(number,'is a composite number.')


    

