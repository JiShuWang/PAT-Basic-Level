# labmda函数：https://www.cnblogs.com/lovewhale1997/p/11424429.html
# %.2f %x的用法：https://blog.csdn.net/imredboy/article/details/99189030

# 时间复杂度：O(N)
# 解题思想：
# 1.贪心算法的思想，根据月饼的单价进行降序排序
# 2.对排序好的月饼进行逐个判断
# 3.注意输入时不能用int，需要用float
# 4.使用lambda函数、%.2f等用法

NOM, Requirement = map(int, input().split())  # 输入月饼种类数、总需求量(万吨)
Stock = list(map(float, input().split()))  # 各个月饼的库存(万吨)
Price = list(map(float, input().split()))  # 各个月饼的总售价(亿)
MoonCake = [[0, 0, 0] for i in range(NOM)]  # 创建月饼列表，存放各个月饼的总库存、总售价、售价/库存的比值
SaleCount = 0  # 最终卖出的总价

for i in range(NOM):
    MoonCake[i] = [Stock[i], Price[i], Price[i] / Stock[i]]

MoonCake.sort(key=lambda x: x[2], reverse=True)  # 使用labmda函数作为降序排序参数
# 在sort方法的key中使用labmda x:x[2]等同于使用MoonCake列表的第二个元素进行排序

i = 0
while Requirement > 0 and i < NOM:  # 仍有需求且月饼仍有库存
    if Requirement > MoonCake[i][0]:  # 当前需求>当前月饼总库存
        Requirement -= MoonCake[i][0]
        SaleCount += MoonCake[i][1]
        i += 1
    elif Requirement <= MoonCake[i][0]:  # 当前需求<=当前月饼总库存
        SaleCount += Requirement * MoonCake[i][2]
        Requirement = 0

print('%.2f' % SaleCount)
