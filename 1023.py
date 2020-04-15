# 时间复杂度：O(N)
# 解题思想：
# 本题可以利用比较巧妙的解法
# 1.例如样例所给的2 2 0 0 0 3 0 0 1 0
# 2.先用列表存放[1,1,5,5,5,8]
# 3.再将0插入到第一个1后面，即[1,0,0,1,5,5,5,8]
# 4.再将每一位用字符串连接起来
# 5.最终把字符串转为整型

Number = list(map(int, input().split()))  # 存放0-9的数字的个数
NumberList = list()  # 存放1-9的数字

for i in range(1, 10):
    NumberList += [i for j in range(Number[i])]  # 添加j个数字i，例如有3个2，则将3个2都添加到NumberList中

NumberList = NumberList[0:1] + [0 for i in range(Number[0])] + NumberList[1:]  # 列表拼接，如果有0，在第一个数后面添加0

Min = ''
for i in range(len(NumberList)):
    Min += str(NumberList[i])  # 字符串连接

print(int(Min))
