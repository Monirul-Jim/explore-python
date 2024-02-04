def with_print(a, b):
    print(a+b)


with_print(2, 4)


def with_return(a, b):
    return a+b


result = with_return(3, 4)
result += 5
print(with_return(3, 4)*4)
