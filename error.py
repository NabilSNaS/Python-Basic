try:
    with open('test.txt','r') as my_file:
        content=my_file.read()
        print(content)
except FileNotFoundError:
    print('The file does not exist.')
    print('Made by Nabu')
try:
    my_list=[]
    print(my_list[0])

except IndexError as e:
    print(e)
