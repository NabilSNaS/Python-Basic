'''class revrnge:
    def __init__(self,n):
                 
        self.n=n
        self.i=n
    def __iter__(self):
                return self
    def __next__(self):
        if self.n>=0:
            if self.i==self.n:
                self.n=self.n-1
                return self.i
            else:
                self.i=self.n
                self.n=self.n-1
                return self.i
        else:
            raise StopIteration
for temp in revrnge(5):
    print(temp)'''

'''def revrange(n):
    while n>=0:
        yield n
        n=n-1
for temp in revrange(5):
 print(temp)'''

'''class MyClass:
#A custom class for nothing

    def  __init__(self,var):
        self.var=var
    def __del__(self):
        del self.var'''

def fib(n):
    series=[]
    a,b=0,1
    while b<n:
        series.append(b)
        a,b=b,a+b
    return series
if __name__=="__main__":
    temp=fib(100)
    print(temp)

'''def my_function():
    #do something
def your_function():
    #do something
def main():
    #call all functions here
    my_function()
    #play with them
    your_function()
if __name__=="__main__":
    #now call main function
    main()'''


'''my_package/
my_package/__init__.py
my_package/iterator.py
my_package/err.py
my_package/error.py
my_package/s.py'''





    
       

