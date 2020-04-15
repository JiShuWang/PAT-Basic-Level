# 时间复杂度：O(n)
# 解题思想：
# 1.利用Python动态类型的特性
# 2.即时判断，输入一行判断一行
NOJ = int(input())
for i in range(NOJ):
    A, B, C = map(int, input().split())
    if A + B > C:
        print("Case #"+str(i+1)+": true")
    else:
        print("Case #" + str(i + 1) + ": false")