# transpose matrix conversation
matrix = [[2, 3], [4, 5], [6, 7], [8, 9]]
a = []
for row in range(2):
    b = []
    for col in matrix:
        b.append(col[row])
    a.append(b)
print(a)
# result = [[col[row] for col in matrix] for row in range(2)]
result = [[col[row] for col in matrix] for row in range(2)]
print(result, "result")
