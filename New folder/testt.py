import logging
logging.basicConfig(filename='testt.log',filemode='w',  level=logging.INFO)

'''logging.debug('This is a debug message.')
logging.info('This is an informational message.')
logging.error('This is an error message.')
'''
a=10
b=0

try:
    temp=a/b
    print(temp)
except ZeroDivisionError as e:
    logging.exception(e)
    
    '''


    import logging
    
from habijabi import add,is_even
#logging.basicConfig(filename='test.log',level=logging.INFO)
logging.basicConfig(filename='test.log', format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
                    level=logging.INFO)


logging.info('We are calling our add function.')
temp=add(12,78)
print(temp)
logging.info('add function executed, task completed.')
logging.info('We are calling our is_even function.')
temp=is_even(2)
print(temp)
logging.info('is_even function executed, task completed.')'''
