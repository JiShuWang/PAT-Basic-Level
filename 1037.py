# 时间复杂度：O(1)
# 解题思想：
# 1.将实付的钱、应付的钱都转为最小面值单位（纳特）
# 2.使用实付的钱-应付的钱，判断哈利需要找零还是补足
# 3.思考一个根据差值求出三个面值单位的算法

RealPrice, HarryMoney = input().split()  # 应付的钱、实付的钱
RealPrice = str(RealPrice)
HarryMoney = str(HarryMoney)

# 获取应付的钱对应的三个单位
RealGalleon = int(RealPrice[:RealPrice.find('.')])
RealSickle = int(RealPrice[RealPrice.find('.') + 1:RealPrice.rfind('.')])
RealKnut = int(RealPrice[RealPrice.rfind('.') + 1:])

# 获取实付的钱对应的三个单位
HarryGalleon = int(HarryMoney[:HarryMoney.find('.')])
HarrySickle = int(HarryMoney[HarryMoney.find('.') + 1:HarryMoney.rfind('.')])
HarryKnut = int(HarryMoney[HarryMoney.rfind('.') + 1:])

# 将应付的钱、实付的钱都换算为纳特（最小面值单位）
RealTotalKnut = RealKnut + RealSickle * 29 + RealGalleon * 17 * 29
HarryTotalKnut = HarryKnut + HarrySickle * 29 + HarryGalleon * 17 * 29

# 需要找零或者补足的钱
ChangeMoney = HarryTotalKnut - RealTotalKnut
if ChangeMoney >= 0:  # 哈利的钱足够，需要找零
    ChangeGalleon = int(ChangeMoney / (29 * 17))
    ChangeSickle = int(ChangeMoney % (29 * 17) / 29)
    ChangeKnut = int(ChangeMoney % (29 * 17) % 29)
else:  # 哈利的钱不够，需要补足
    ChangeGalleon = int(ChangeMoney / (29 * 17))
    ChangeSickle = int(ChangeMoney * -1 % (29 * 17) / 29)
    ChangeKnut = int(ChangeMoney * -1 % (29 * 17) % 29)
print(str(ChangeGalleon) + '.' + str(ChangeSickle) + '.' + str(ChangeKnut))
# 该算法的思想是：例如差值为1538纳特，对于2.6加隆只能舍为2加隆，而不能入为3加隆
# 1.则1538/(29*17)舍为3加隆，此时还剩59纳特
# 2.1538%(29*17)=59纳特，再59/29舍为2西可，此时还剩1纳特
# 3.最后得到1538纳特可以找零为3加隆，2西可，1纳特
# 4.补足的情况同理，只不过有%运算时，需要将ChangeMoney转为正数
