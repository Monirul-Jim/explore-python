a = [17, 2, 3, 4, 5, 16, 10]
temp = a[0]
a[0] = a[-1]
a[-1] = temp
print(a)
