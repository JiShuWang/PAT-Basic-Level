# 时间复杂度：O(N^2)
# 解题思想：
# 1.只保留合法分数
# 2.去除一个最高分、最低分
# 3.四舍五入判断

NOG, FullPoint = map(int, input().split())  # 输入组数、满分
Score = list()  # 记录一行输入的分数

for i in range(NOG):
    Score = list(map(int, input().split()))  # 输入一行的分数
    G1 = Score[0]
    Score.pop(0)  # 将老师所给的分数删除，只留下其他组所给的分数
    GroupScore = list()  # 存放其他组所给的合法的分数

    for j in range(len(Score)):
        if 0 <= Score[j] <= FullPoint:  # 该分数合法
            GroupScore.append(Score[j])

    GroupScore.remove(max(GroupScore))  # 去除一个最高分
    GroupScore.remove(min(GroupScore))  # 去除一个最低分

    G2 = sum(GroupScore) / len(GroupScore)

    if (G1 + G2) / 2 - int((G1 + G2) / 2) >= 0.5:  # 入
        print(int((G1 + G2) / 2) + 1)
    else:  # 舍
        print(int((G1 + G2) / 2))
