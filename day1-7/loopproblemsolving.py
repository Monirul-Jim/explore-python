# 1 multiplication table by user given number
# a = int(input("Enter Your Number : "))
# for i in range(1, 11):
#     print(a, " X ", i, " = ", a*i)
# 2 python factorial number
# a = int(input("Enter Your Number : "))
# factorial = 1
# for i in range(1, a+1):
#     factorial = factorial*i
# print(factorial)
# 2 make fibonacci series
# a = 0
# b = 1
# for i in range(10):
#     print(a, end=" ")
#     result = a+b
#     a = b
#     b = result
# 2 find the armstrong number
# a = int(input("Enter A Number : "))
# number_length = len(str(a))
# temp = a
# sum = 0
# while temp > 0:
#     last_digit = temp % 10
#     sum = sum+last_digit**number_length
#     temp //= 10
# if sum == a:
#     print("armstrong number")
# else:
#     print("Not armstrong number")
# 3 reverse number
# a = int(input("enter the number : "))
# reverse_number = 0
# while a > 0:
#     last_digit = a % 10
#     reverse_number = reverse_number*10 + last_digit
#     a //= 10
# print(reverse_number)
a = int(input("Enter a Number : "))
reverse_number = 0
while a > 0:
    last_digit = a % 10
    reverse_number = reverse_number*10+last_digit
    a //= 10
print(reverse_number)
