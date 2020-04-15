# 时间复杂度：O(logN)
# 解题思想：
# 1.用列表存放输入数字的每一位
# 2.分别用升序、降序得到最大数、最小数
# 要注意很多的点，对输入要补足4位，对输出也要补足4位，是一道非常细节的题，要完全AC，需要多注意
OriginNumber = int(input())  # 输入最初的数字，此时为字符串类型，不用转为整型
Judge = False

while not Judge:  # not Judge等同于Judge!=True等同于Judge==False
    OriginNumber = str((4 - len(str(OriginNumber))) * '0' + str(OriginNumber))  # Point1,先将该数补为4位，例如：2，补为0002
    NumberList = list()  # 建立一个列表来存放该数字的每一位，每次循环重置
    for i in range(len(OriginNumber)):
        NumberList.append(int(OriginNumber[i]))  # 将该数字的每一位添加到列表中，转换为整型方便后续排序

    MaxNumber, MinNumber = '', ''  # 存放该数字可组合成的最大数、最小数，每次循环重置
    # reverse=True为降序，reverse=False为升序
    # 找到最大数，例如6767，列表为[6,7,6,7]，排序后为[7,7,6,6]，将列表元素逐一合并最后转为整型，即可获得最大数为7766
    NumberList.sort(reverse=True)
    for i in range(len(NumberList)):
        MaxNumber += str(NumberList[i])
    MaxNumber = int(MaxNumber)
    # 找到最小数，例如6767，列表为[6,7,6,7]，排序后为[6,6,7,7]，将列表元素逐一合并最后转为整型，即可获得最小数为6677
    NumberList.sort(reverse=False)
    for i in range(len(NumberList)):
        MinNumber += str(NumberList[i])
    MinNumber = int(MinNumber)

    # Point2,题目要求，每个数字按4位输出，例如288，需要输出为0288，因此要补足前位的0
    OriginNumber = MaxNumber - MinNumber
    if OriginNumber == 0:  # Point3,特例：该数字的每一位都相等
        print(str((4 - len(str(MaxNumber))) * '0' + str(MaxNumber)) + ' - ' + str(
            (4 - len(str(MinNumber))) * '0' + str(MinNumber)) + ' = 0000')
        Judge = True
    else:  # 继续运算
        if OriginNumber == 6174:  # 到达数字黑洞
            Judge = True
        print(str((4 - len(str(MaxNumber))) * '0' + str(MaxNumber)) + ' - ' + str(
            (4 - len(str(MinNumber))) * '0' + str(MinNumber)) + ' = ' + str(
            (4 - len(str(OriginNumber))) * '0' + str(OriginNumber)))
