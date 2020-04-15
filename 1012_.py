# 时间复杂度：O(N)
# 解题思想：
# 1.逐个判断，添加到对应列表
# 2.对列表长度进行判断，进行后续操作
Number = list(map(int, input().split()))

A1 = list()
A2 = list()
A3 = list()
A4 = list()
A5 = list()
for content in Number[1:]:
    value = content % 5
    if value == 0 and content % 2 == 0:
        A1.append(content)
    elif value == 1:
        A2.append(content)
    elif value == 2:
        A3.append(content)
    elif value == 3:
        A4.append(content)
    elif value == 4:
        A5.append(content)

if len(A1) != 0:
    A1 = sum(A1)
else:
    A1 = 'N'

if len(A2) != 0:
    StaggeredSum = 0
    for i in range(len(A2)):
        StaggeredSum += ((-1) ** i) * A2[i]
    A2 = StaggeredSum
else:
    A2 = 'N'

if len(A3) != 0:
    A3 = len(A3)
else:
    A3 = 'N'

if len(A4) != 0:
    A4 = round(sum(A4) / len(A4), 1)
else:
    A4 = 'N'

if len(A5) != 0:
    A5 = max(A5)
else:
    A5 = 'N'

print(A1, A2, A3, A4, A5)
