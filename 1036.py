# 时间复杂度：O(N^2)
# 解题思想：
# 1.先求出行数和列数
# 2.循环输出字符，首行、末行输出整行，其它行只输出首列、末列，中间用空格补齐

SideLength, Character = input().split()  # 输入边长及字符
SideLength = int(SideLength)  # 将字符型转为整型

ColumnLength = SideLength  # 列数，等于边长
RowLength = float(SideLength) * 0.5

# 四舍五入算法
if RowLength - int(RowLength) >= 0.5:  # 小数值大于等于0.5
    RowLength += 1
RowLength = int(RowLength)

for i in range(RowLength):  # 按行输出
    if i == 0 or i == RowLength - 1:  # 首行或末行
        for j in range(ColumnLength):  # 输出整行
            print(Character, end='')
    else:
        print(Character, end='')
        print((ColumnLength - 2) * ' ', end='')  # 补足中间的空格
        print(Character, end='')
    print()  # 换行
