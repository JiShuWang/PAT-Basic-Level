# 时间复杂度：O(n)
# 解题思想：
# 1.将输入保存到列表中
# 2.使用reverse方法将列表变为逆序
Words = list(input().split())
Words.reverse()  # 将列表中的元素变为逆序
# 按要求格式输出
for i in range(len(Words) - 1):
    print(Words[i], end=" ")
print(Words[len(Words) - 1])
