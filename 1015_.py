# labmda函数：https://www.cnblogs.com/lovewhale1997/p/11424429.html
# Top.sort(key=lambda score: score[1] + score[2], reverse=True)
# 时间复杂度：O(n^2)
# 解题思想：
# 1.创建四个列表来存放不同类别的学生
# 2.自定义函数来对四个列表进行题目要求的排序
# 3.将四个列表合并再覆盖掉最初的列表
# 存在的问题：使用Python会导致部分测试点超时，在网上查找了一下，就算使用快排也无法解决
def StudentSort(List):
    for i in range(len(List)):
        for j in range(i + 1, len(List)):
            if List[j][1] + List[j][2] > List[i][1] + List[i][2]:
                List[i], List[j] = List[j], List[i]  # 进行位置交换
            elif List[j][1] + List[j][2] == List[i][1] + List[i][2]:
                if List[j][1] > List[i][1]:
                    List[i], List[j] = List[j], List[i]  # 进行位置交换
                elif List[j][1] == List[i][1]:
                    if List[j][0] < List[i][0]:
                        List[i], List[j] = List[j], List[i]  # 进行位置交换


NOS, MinLine, PrimeLine = map(int, input().split())  # 输入学生数、最低分数线、优先分数线
Student = [[0, 0, 0] for i in range(NOS)]  # 创建学生列表，存放学号、德分、才分、总分

Top, Second, Third, Bottom = list(), list(), list(), list()
LineCount = 0  # 达到最低分数线的人数
for i in range(NOS):  # 输入学号、德分、才分
    Student[i] = list(map(int, input().split()))
    if Student[i][1] >= PrimeLine and Student[i][2] >= PrimeLine:
        Top.append(Student[i])  # 使用append方法添加学生信息到别的列表
        LineCount += 1
    elif Student[i][1] >= PrimeLine > Student[i][2] >= MinLine:
        Second.append(Student[i])
        LineCount += 1
    elif MinLine <= Student[i][2] <= Student[i][1] < PrimeLine:
        Third.append(Student[i])
        LineCount += 1
    elif Student[i][1] >= MinLine and Student[i][2] >= MinLine:
        Bottom.append(Student[i])
        LineCount += 1
StudentSort(Top), StudentSort(Second), StudentSort(Third), StudentSort(Bottom)
Student = Top + Second + Third + Bottom
print(LineCount)
for i in range(LineCount):
    print(Student[i][0], Student[i][1], Student[i][2])
