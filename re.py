'''import re
my_string="hafija.pstu.cse@gmail.com,hafija14@cse.pstu.ac.bd"
temp=my_string.split(',')
for phrase in temp:
    result=re.search("([\w\.-]+)@([\w\.-]+)",phrase)
    print(result.group())'''

'''import re
my_string="hafija.pstu.cse@gmail.com,hafija14@cse.pstu.ac.bd"
temp=my_string.split(',')
for phrase in temp:
    result=re.match("([\w\.-]+)@([\w\.-]+)",phrase)
    print(result)'''

'''import re
my_string="purple alice@google.com,blah monkey bob@abc.com blah dishwasher"
temp=my_string.split(',')
for phrase in temp:
    result=re.match("([\w\.-]+)@([\w\.-]+)",phrase)
    print(result)'''


