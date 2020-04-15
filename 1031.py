# 时间复杂度：O(N)，虽然是双层循环，但内循环为固定常数
# 解题思想：
# 1.使用列表和字典来存放权重、校验码的对应关系
# 2.首先判断前17位是否都是数字，使用isnumeric方法，如果是，则求出权重和并判断与校验码是否匹配
# 3.设置一个标记，在整个循环过程中，只要有一个身份证号不正确， 就改变标记，为最后的输出提供判断

NOI = int(input())
Weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 每一位号码对应的权重
CheckCode = {  # 利用字典来存放Z值与校验码的对应关系
    0: '1',
    1: '0',
    2: 'X',
    3: '9',
    4: '8',
    5: '7',
    6: '6',
    7: '5',
    8: '4',
    9: '3',
    10: '2'
}

Judge = True  # 所有身份证号是否都正确的标记，默认为是
for i in range(NOI):
    Identity = input()  # 输入身份证号
    Z = 0
    if Identity[:17].isnumeric() == True:  # 该身份证号的前17位全为数字
        for j in range(17):  # 求权重和
            Z += int(Identity[j]) * Weights[j]
        Z %= 11
        if CheckCode[Z] != Identity[17]:  # Z值对应校验码与身份证号最后一位不匹配
            print(Identity)
            Judge = False
    else:
        Judge = False
        print(Identity)

if Judge == True:  # 所有身份证号都正确
    print("All passed")
