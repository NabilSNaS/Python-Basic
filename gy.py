"""n=1
while n<=10:
    print(n)
    n=n+1
n=1
temp=0
while n<=100:
    temp=temp+n
    n=n+1
print(temp)
n=100
temp=n*(n+1)
temp=temp/2
print(temp)
a=['onion','potato','ginger']
print(type(a))
for item in a:
    print(item)

a='python'
for letter in a:
    print(letter)
    
range(5)
list(range(5))
for number in range (1,11):
    print(number)
for number in range (1,10):
    if number == 5:
        break
    print(number)
"""
'''for number in range(1,11,2):
    if number == 5:
        pass
    print(number)
n=1
while n<=10:
    print(n)
    n=n+1
else:
    print('The loop is over')
for n in range(0,11):
    print(n)
    n=n+1
else:
    print('The loop is over.')
'''
print('Please, input the number:')
number = int(input())
count=1
while  count <=10:
    print(number, 'x', count, '=', number*count)
    count+=1
