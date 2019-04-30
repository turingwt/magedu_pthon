mart = [[1, 2, 3], [4, 5, 6]]
tm = [[0 for i in range(len(mart))] for i in range(len(mart[0]))]
for i in range(len(mart)):
    for j in range(len(mart[i])):
        tm[j][i] = mart[i][j]
print(tm)
