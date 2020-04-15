# 时间复杂度：O(n)
# 解题思想：
# 1.使用Python中列表截取的方法
# 新列表=原列表末尾+原列表开头
# 例如NON=6,MoveDistance=2，则先截取Number[6-2:](索引4,5的元素)
# 再截取Number[:6-2])(索引0,1,2,3的元素)
NON, MoveDistance = map(int, input().split())
Number = list(map(int, input().split()))
Number = Number[NON - MoveDistance:] + Number[:NON - MoveDistance]
# 按要求格式输出
for i in range(NON - 1):
    print(Number[i], end=" ")
print(Number[NON - 1])
