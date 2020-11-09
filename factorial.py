print("Code to calculate factorial")

x = int(input("Enter a number\n"))

def facto(var):
    multi = 1
    for i in range(1, var+1):
        multi *= i
    print("factorial of {} is {} ".format(str(var), str(multi)))

facto(x)

# Using recursion
def fact(arg):
    if arg == 0:
        return 1
    else:
        return arg * fact(arg-1)

val = fact(x)
print("factorial of {} is {}".format(x,val))
