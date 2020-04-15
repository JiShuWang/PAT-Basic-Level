# 时间复杂度：O(n)
# 解题思想：
# 1.使用列表存储三个字段的值
# 2.对成绩进行判断并保留列表索引
NOP = int(input())
Student = [["Name", "ID", "Score"] for i in range(NOP)]  # 创建姓名、学号、成绩的列表
MaxScore, MinScore, MaxIndex, MinIndex = 0, 100, 0, 0  # 初始化最高成绩和最低成绩、最高成绩和最低成绩对应的学生在列表中的索引
for i in range(NOP):
    Student[i] = list(map(str, input().split()))
    if int(Student[i][2]) > MaxScore:  # 出现更高成绩
        MaxScore = int(Student[i][2])
        MaxIndex = i
    if int(Student[i][2]) < MinScore:  # 出现更低成绩
        MinScore = int(Student[i][2])
        MinIndex = i
print(Student[MaxIndex][0], Student[MaxIndex][1])  # 输出最高成绩学生姓名和学号
print(Student[MinIndex][0], Student[MinIndex][1])  # 输出最低成绩学生姓名和学号
