# 时间复杂度：O(N)
# 解题思想：
# 1.为了避免超时，只能用单层循环
# 2.创建两个列表分别存放出现的字母及其出现次数，在遍历字符串的过程中逐步更新
# 3.找出出现次数最多且字母序最小的字母即可

String = input()  # 输入字符串
AlphaName = list()  # 存放字符串中出现过的英文字母
AlphaCount = list()  # 存放该英文字母出现过的次数

for i in range(len(String)):  # 遍历字符串
    if String[i].isalpha():  # 该字符是字母
        if String[i].lower() not in AlphaName:  # 该字母的小写第一次出现
            AlphaName.append(String[i].lower())  # 在AlphaName中添加该字母的小写
            AlphaCount.append(1)  # 在AlphaCount中添加1
        else:  # 该字母的小写出现过
            AlphaCount[AlphaName.index(String[i].lower())] += 1  # 该字母在AlphaCount中的出现次数+1

MaxCount = max(AlphaCount)  # 字母出现最多的次数
MinAlpha = 'z'  # 字母序最小的字母，默认为z，方便后续比较

for i in range(len(AlphaCount)):
    if AlphaCount[i] == MaxCount:  # 该字母出现次数为最多次
        if AlphaName[i] < MinAlpha:  # 该字母的字母序更小
            MinAlpha = AlphaName[i]

print(MinAlpha, MaxCount)
