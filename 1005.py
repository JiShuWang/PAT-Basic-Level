# 时间复杂度：O(nlogn)
# 解题思想：
# 1.判断数列中的数字是否属于可覆盖数字集合，如果属于则跳到下一个数字
# 2.如果不属于，则对该数进行卡拉兹变换，并将变换过程中的数字存入可覆盖数字集合
# 3.数列中所有数字都变换完成后，再逐个判断是否属于可覆盖数字集合
# 4.若不属于则添加到关键数字列表中
NON = int(input())
Coverable = set()  # 可覆盖数字的集合
KeyNumber = list()  # 关键数字的列表
Number = list(map(int, input().split()))
for i in range(NON):
    Temp = Number[i]  # 将需要进行卡拉兹判断的数使用一个临时变量代替
    if Temp in Coverable:  # 该数属于可覆盖数字：优化1
        continue
    else:  # 该数不属于可覆盖数字
        while Temp != 1:
            if Temp % 2 == 0:
                Temp //= 2
            else:
                Temp = (3 * Temp + 1) // 2
            if Temp in Coverable:  # 在变换过程中，出现可覆盖数字则不再变换：优化2
                break
            Coverable.add(Temp)  # 将卡拉兹变换后的数字添加到可覆盖数字集合中
for i in range(NON):
    if Number[i] not in Coverable:  # 该数字不属于可覆盖数字
        KeyNumber.append(Number[i])  # 将该数字添加到关键数字中
KeyNumber.sort(reverse=True)  # 从大到小排序
for i in range(len(KeyNumber) - 1):
    print(KeyNumber[i], end=" ")
print(KeyNumber[len(KeyNumber) - 1])
