# 时间复杂度：O(N)
# 解题思想：
# 1.本质为求两集合的差集，但题目要求按发现的顺序进行输出，如果直接进行差集运算，差集的顺序会有不同
# 2.所以采用遍历的方法进行判断，题目又要求英文字母要转为大写输出，所以需要一个列表来存放转为大写后的字符

Full = list(input())  # 应该输入的文字
Part = set(list(input()))  # 实际输入的文字，用集合去重
Difference = list()  # 存放Full与Part的差集

for i in range(len(Full)):  # 遍历Full中的字符，判断是否存在于Part和差集中
    if Full[i] not in Part and str(Full[i]).upper() not in Difference:  # 该字符及其大写第一次出现
        Difference.append(str(Full[i]).upper())  # 存放该字符的大写

for i in range(len(Difference)):
    print(Difference[i], end='')
