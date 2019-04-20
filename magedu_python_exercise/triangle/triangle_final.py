n = 7
row = [1] * n
for i in range(n):
    tmp = row[0]
    for j in range(i//2):
        val = row[j+1] + tmp
        tmp = row[j+1]
        row[j+1] = val
        if i != 2j:
            row[i-j-1] = val
    print(row[:i+1])
