'''try:
    my_file=open('test.txt','r')
    content=my_file.read()
    i=int(content.strip())
except IOError as e:
    errno,strerror = e.args
    print("I/O error({0}):{1}".format(errno,strerror))
except ValueError:
    print("No valid integer in line.")
except:
    print("Unexpected error!")'''
'''try:
    my_file=open('test.txt')
    content=my_file.read()
    i=int(content.stri())
except(IOError, ValueError):
    pass'''

'''try:
    a=5
    b=8
    print(a+b)

except ValueError as e:
    print(e)


else:
    print('There is no exception.')'''

'''try:
    with open('test.txt','r') as my_file:
        content=my_file.read()

except FileNotFoundError:
    print('The file does not exist.')
finally:
    print('To be or not to be that is the question')'''

try:
    raise NameError ('Hey! It is a custom error message.')
except NameError as e:
    print(e)
    
    
    
