my_file=open("D:/python exercise/test.txt",'w+')
my_file.write("Hi nabila!")
#my_file.close()
#my_file=open("D:/python exercise/test.txt",'r')
my_file.seek(0)
content=my_file.read()
print(content)
my_file.close()


'''import iterator
series=iterator.fib(100)
for item in series :
     print(item)'''

'''from iterator import fib
series = fib(200)

for item in series:
    print(item)'''

'''from iterator import*

series=fib(300)
for item in series:
    print(item)'''

import sound.effects.echo

sound.effects.echo.echofilter(input,output,delay=0.7,atten=4)

from sound.effects import echo
echo.echofilter(input,output,delay=0.7,atten=4)

from sound.effects.echo import echofilter
echofilter(input,output,delay=.7,atten=4)




    

    
