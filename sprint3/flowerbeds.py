k = [[7, 8], [7, 8], [2,3], [6,10]]
# k = [[2, 3], [5, 6], [3, 4], [3, 4]]
k.sort()
res = []
for i in range(len(k) - 1):
    if k[i][1] < k[i + 1][0]:
        res.append(k[i])
    if k[i][1] > k[i + 1][0]:
        res.append(k[i])
    if 
    


print(res)

# k = [input().strip().split() for _ in range(4)]
# k = ''.join(map(input() for _ in range(4)))
# print(k)
