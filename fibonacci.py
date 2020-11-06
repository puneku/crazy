# Printing Fibonacci series : 0 1 1 2 3 5 8 13 ...
# Taking user input : number of Fibonacci series term

n = int(input("Enter a number\n"))

def fibonacci(n):
    ft = 0 
    st = 1
    print(ft)
    print(st)
    for i in range(2,n):
        mt = ft + st
        print(mt)
        ft = st 
        st = mt
    
    
fibonacci(n)
