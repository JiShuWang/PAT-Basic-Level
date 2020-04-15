# 时间复杂度：O(N)
# 解题思想：
# 1.使用三个列表分别存放三个信息
# 2.因为三个信息在列表的下标是一一对应的关系，所以可以使用index方法
# 3.例如a[1]=1，b[1]='A'，则A[b.index['A']]=1

NOS = int(input())  # 输入考生个数
ID = [0 for i in range(NOS)]  # 存放准考证号
TestSeat = [0 for i in range(NOS)]  # 存放试机座位号
ExamSeat = [0 for i in range(NOS)]  # 存放考试座位号

for i in range(NOS):
    ID[i], TestSeat[i], ExamSeat[i] = map(int, input().split())

NOSS = int(input())  # 输入查询个数
SearchTestSeat = list(map(int, input().split()))  # 存放需要查询的试机座位号

for i in range(NOSS):
    print(ID[TestSeat.index(SearchTestSeat[i])], ExamSeat[TestSeat.index(SearchTestSeat[i])])
