# 1 find which is squire and which is rectangle
# a = int(input("please enter first number : "))
# b = int(input("please enter second number : "))
# if a == b:
#     print("this is rectangle")
# else:
#     print(" this is squire")


# 2  find the largest number from user given number
# this is first approach
# a = int(input())
# b = int(input())
# c = int(input())
# if a >= b:
#     if a >= c:
#         print(a, "A is the largest number")
#     else:
#         print(c, "C is the largest number")
# else:
#     if b >= c:
#         print(b, "B is the largest number")
#     else:
#         print(c, "C is the largest number")
# this is second approach
# if a >= b and b >= c:
#     print(a, "a is the largest number")
# elif b >= c:
#     print(c, "c is the largest number")
# else:
#     print(c, "c is the largest")

# 3 find if the number is even or odd
# a = int(input("Enter some number:  "))
# if a % 2 == 0:
#     print(a, "A is even number")
# else:
#     print(a, "A is  odd number")


# 4 find the mark of a student and give Grade
# marks = int(input("Enter Your Mark : "))
# if marks > 90:
#     print("Your grade is A grade")
# elif marks > 80 and marks <= 90:
#     print("your mark is B grade")
# elif marks >= 60 and marks <= 80:
#     print("Your grade is C grade")
# else:
#     print("Your grade is D")


# 4 find the leap year
year = int(input("Enter a year : "))
if year % 400 == 0 and year % 100 == 0:
    print("this is leap year")
elif year % 4 == 0 and year != 0:
    print("leap year")
else:
    print("not leap year")
