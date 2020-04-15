# 时间复杂度：O(n)
# 解题思想：
# 1.先求和
# 2.创建拼音列表
# 3.每位数字与列表的索引正好吻合
# 4.从左往右依次输出
Number = input()
Count = 0
for i in range(len(Number)):
    Count += int(Number[i])
Count = str(Count)
List = ["ling", "yi", "er", "san", "si", "wu", "liu", "qi", "ba", "jiu"]
for i in range(len(Count) - 1):
    print(List[int(Count[i])], end=" ")  # 输出该数字在列表中对应的拼音
print(List[int(Count[len(Count) - 1])])
