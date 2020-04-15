# 时间复杂度：O(N)
# 解题思想：
# 1.使用in关键字判断，count方法计数

N = input()
for i in range(10):
    if str(i) in N:
        print(str(i) + ':' + str(N.count(str(i))))
