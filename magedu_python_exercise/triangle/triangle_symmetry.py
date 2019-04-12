triangle = [[1], [1, 1]]
for i in range(2, 6):
    pre = triangle[i-1]
    cur = [1] * (i + 1)
    for j in range(1, i):
        if j < (((i + 1) / 2)):
            cur[j] = (pre[j-1] + pre[j])
        else:
            cur[j] = cur[int(i/2-(j-i/2))]
    triangle.append(cur)
print(triangle)

