# 时间复杂度：O(N)
# 解题思想：
# 1.创建两个列表分别存放卖的珠子、买的珠子
# 2.遍历买的珠子，判断该珠子是否存在于卖的珠子中
# 3.若存在，则在两个列表中都将该珠子替换为*，不能直接替换为空，会导致循环错误
# 4.遍历结束后，再将两个列表的*都替换为空
# 5.此时，若买的珠子长度为0，则卖的珠子的长度就是多余的珠子个数
# 6.若买的珠子长度不为0，则买的珠子的长度就是缺少的珠子个数

SellBead = input()  # 卖的珠子
BuyBead = input()  # 买的珠子

for i in range(len(BuyBead)):  # 遍历买的珠子
    if BuyBead[i] in SellBead:  # 该珠子，卖家也有
        SellBead = SellBead.replace(BuyBead[i], '*', 1)  # 暂时替换为*
        BuyBead = BuyBead.replace(BuyBead[i], '*', 1)  # 暂时替换为*
SellBead = SellBead.replace(' ', '')  # 再将*替换为空
BuyBead = BuyBead.replace(' ', '')  # 再将*替换为空

if len(BuyBead) == 0:  # 珠子买齐了
    print("Yes", len(SellBead))
else:  # 珠子没买齐
    print("No", len(BuyBead))
