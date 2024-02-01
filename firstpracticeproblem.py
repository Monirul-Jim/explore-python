# a = int(input("please enter first number : "))
# b = int(input("please enter second number : "))
# if a == b:
#     print("this is rectangle")
# else:
#     print(" this is squire")
a = int(input())
b = int(input())
c = int(input())
if a >= b:
    if a >= c:
        print(a, "A is the largest number")
    else:
        print(c, "C is the largest number")
else:
    if b >= c:
        print(b, "B is the largest number")
    else:
        print(c, "C is the largest number")
