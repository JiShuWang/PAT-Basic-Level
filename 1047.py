# 时间复杂度：O(N)
# 解题思想：
# 1.与1042题相似，不再赘述，请移步查看

NOP = int(input())  # 输入参赛队员人数
TeamID = list()  # 记录每个队伍的编号
TeamScore = list()  # 记录每个队伍的总成绩

for i in range(NOP):
    ID, PersonalScore = input().split()  # 输入编号、个人成绩
    ID = str(ID)
    if ID[:ID.find('-')] not in TeamID:  # 该该队伍编号首次出现
        TeamID.append(ID[:ID.find('-')])
        TeamScore.append(int(PersonalScore))
    else:  # 该队伍编号出现过
        TeamScore[TeamID.index(ID[:ID.find('-')])] += int(PersonalScore)

# TeamID与TeamScore是一一对应的关系，因此下标也相同
print(TeamID[TeamScore.index(max(TeamScore))], max(TeamScore))
