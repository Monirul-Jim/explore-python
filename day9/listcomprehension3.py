# a = []
# for i in range(1, 20):
#     if i % 3 == 0:
#         a.append(i)
# print(a)
# a = []
# for i in range(1, 20):
#     if i % 3 == 0:
#         a.append(i)
#     if i % 5 == 0:
#         a.append(i)
# print(a)
# a = [i for i in range(1, 20) if i % 3 == 0]
# print(a)
# a = [i for i in range(1, 20) if i % 3 == 0 or i % 5 == 0]
# print(a)
b = ["Odd" if i % 2 == 0 else "Even" for i in range(20)]
print(b)
