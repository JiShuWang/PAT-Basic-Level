# 时间复杂度：O(N^2)
# 解题思想：
# 1.首先存放输入的数字并进行升序排序
# 2.使用双层循环，外循环每次遍历的数就是最小值，内循环每次遍历的数就是最大值
# 3.根据最大值<=最小值*p进行判断，如果满足则内循环继续，否则内循环结束
# 4.为了避免超时，当所剩的数字已经不可能满足条件时就结束外循环

NON, p = map(int, input().split())
Number = list(map(int, input().split()))  # 存放题目所给的数字

Number.sort(reverse=False)  # 按升序进行排序

Most = 0  # 最多可以有Most个数字组成完美数列
for i in range(len(Number)):  # 列表从左往右遍历，产生最小值
    if Most >= len(Number) - i:  # 剩余数字个数不可能比Most大
        break
    for j in range(i + Most, len(Number)):  # 列表从i+Most开始遍历，产生最大值
        if Number[i] * p < Number[j]:  # 此时，最小值*p<最大值，继续往右也不可能再满足条件
            break
        Most = j - i + 1  # 替换Most

print(Most)
