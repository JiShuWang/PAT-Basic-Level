# 时间复杂度：O(N)
# 解题思想：
# 1.判断所能生成的沙漏的最大层数
# 2.按顺序输出沙漏
# 3.对每一行进行左缩进，也就是实现“居中”，满足题目要求的格式

NOA, Symbol = input().split()  # 输入符号个数、符号
NOA = int(NOA)  # 将字符型转为整型

MaxLayer = 1  # 沙漏的层数
NOA -= 1  # 减去最中间那一层

# 计算最多有几层
while NOA - 2 * (MaxLayer + 2) >= 0:  # 所剩符号数可以再延伸2层
    NOA -= 2 * (MaxLayer + 2)
    MaxLayer += 2

NowLayer = MaxLayer  # 沙漏上半部
while NowLayer >= 3:
    String = (MaxLayer - NowLayer) // 2 * ' ' + NowLayer * Symbol  # 将每一层都进行左缩进，实现居中
    print(String)
    NowLayer -= 2

print((MaxLayer - NowLayer) // 2 * ' ' + Symbol)  # 沙漏中部，左缩进，实现居中

NowLayer = 3  # 沙漏下半部
while NowLayer <= MaxLayer:
    String = (MaxLayer - NowLayer) // 2 * ' ' + NowLayer * Symbol  # 将每一层都进行左缩进，实现居中
    print(String)
    NowLayer += 2

print(NOA)  # 输出剩余符号数
