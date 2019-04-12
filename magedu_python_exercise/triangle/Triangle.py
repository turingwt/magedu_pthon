n = 6
triangle = [[1]]
for i in range(1, 6):
    pre = triangle[i-1] + [0]
    cur = []
    for j in range(i+1):
        cur.append(pre[j-1] + pre[j])
    triangle.append(cur)
print(triangle)

