# 时间复杂度：O(n)
# 解题思想：
# 1.注意没有PA、PB的情况
A, DA, B, DB = input().split()
PA, PB = '', ''  # 存放结果

# 寻找PA、PB
for i in range(len(A)):
    if A[i] == DA:
        PA += DA
for i in range(len(B)):
    if B[i] == DB:
        PB += DB

# 判断PA、PB是否有值
if len(PA) == 0:  # 没有值则置为0
    PA = 0
else:
    PA = int(PA)
if len(PB) == 0:
    PB = 0
else:
    PB = int(PB)

print(PA + PB)
