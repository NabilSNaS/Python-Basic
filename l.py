'''list=[]
for i in range(1,101):
    if i%3==0 and i%5!=0:
        list.append(i)

print(list)
'''
'''a=[13,34,19,28,46,61,73,49,1,31,4,7,91,58,52,82,70,43,88,55,97,16,22,25,79,85,40,64,94,67,37]
my_list=[]
for i in a:
    if i<50:
        my_list.append(i)
print(my_list)'''
'''a=[40,45,33,34,8,38,28,22,1,7,49,413,8,9,7,4,33, 90,89,78]
my_list=[]
for i in a:
    if i not in my_list:
        my_list.append(i)
print(my_list)
'''
'''print('Please,input the number:')
number=int(input())
temp=number
while number>0:
    count=temp
    while count>0:
        print ('*',end='')
        count-=1
    print()
    number-=1'''
'''print('Please input your word:')
word=input()
word=word.casefold()
reversed_word=word[::-1]
if word==reversed_word:
    print('Great! It is a pallindrome.')


else :
    print('LOL! It is not a pallindrome.')'''
my_list=[1,3,5,7,11,13,15,17,20,26,31,44,54,56,65,77,94,100]
print('Input the number:')
number=int(input())
first=0
last=len(my_list)-1
found=False
cycle=0
while first<=last and not found:
    midpoint=(first+last)//2
    if my_list[midpoint]==number:
        found=True
    else:
        if number < my_list[midpoint]:
            last=midpoint-1
        else:
            first=midpoint+1
    cycle+=1
print('Found after', cycle,'cycle.')
            


    
