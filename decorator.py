def divide(a,b):
    return a/b

result = divide(3,7)
print(result)

def edge_divide(func):

    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)

    return inner

divide = edge_divide(divide)

decorator_result = divide(3,7)

print(decorator_result)
