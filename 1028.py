# 时间复杂度：O(N)
# 解题思想：
# 1.利用字符串大小进行合理性判断
# 2.对列表进行lambda排序
# 3.列表长度，列表第一个元素，列表最后一个元素分别对应有效生日个数，最年长居民，最年轻居民
# 部分时候提交到OJ仍会超时，与Python的效率有关

NOP = int(input())  # 输入人数
OldestName, YoungestName = "", ""
Oldest, Youngest = "20140906", "18140906"
Effective = 0

for i in range(NOP):
    Information = input().split()
    # 直接利用字符串大小进行比较，如果对年、月、日逐一判断，过于复杂
    # 判断该生日是否合理，将合理的生日添加到列表中
    if "1814/09/06" <= Information[1] <= "2014/09/06":  # 该生日合理
        if Information[1] < Oldest:
            Oldest, OldestName = Information[1], Information[0]
        if Information[1] > Youngest:
            Youngest, YoungestName = Information[1], Information[0]
        Effective += 1
if Effective == 0:  # 测试点3：当有效生日的个数等于0时，只需要输出0
    print(0)
else:  # 如果不进行判断，当有效生日个数等于0时，会多输出两个空格
    print(Effective, OldestName, YoungestName)
