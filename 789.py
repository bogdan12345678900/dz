a = [[1, 2], [3, 4], [5, 6]]
a1 = []
for i in range(len(a[0])):
    row = []
    for j in range(len(a)):
        row.append(a[j][i])
    a1.append(row)
print("Трансформований список:", a1)
