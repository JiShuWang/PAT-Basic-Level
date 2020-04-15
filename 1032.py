# 时间复杂度：O(N^2)
# 解题思想：
# 1.思考题目，会发现学校编号和列表下标可以有一一对应的关系，这样就不必每次都判断该编号是否出现过
# 2.使用动态扩展列表的方法，每当学校编号大于列表长度时，就根据差值扩展列表
# 3.输入的时候直接将Score赋给Number下标-1的元素即可
# 也许因为Python性能的缘故，最后一个测试点超时，在网上查阅了很多代码，依然无法解决，最后选择使用C语言来解决超时问题

NOP = int(input())
School = list()

for i in range(NOP):
    Number, Score = map(int, input().split())
    if Number >= len(School) + 1:  # 学校编号大于当前列表长度，注意学校编号-1=列表下标
        for j in range(Number - len(School)):  # 根据学校编号与列表长度的差值动态扩展列表，例如出现了编号4，此时列表长度为2，就需要扩展4-2=2个长度
            School.append(0)
        School[Number - 1] += Score
    else:
        School[Number - 1] += Score

# 因为题目明确了答案唯一，所以利用max方法找出列表的最大值，再利用index方法找出最大值对应的下标，该下标+1就是学校编号
print(School.index(max(School)) + 1, max(School))

'''
#include <stdio.h>
int main()
{
    int School[100000];
    for (int i=0;i < 100000;i++)
    {
        School[i] = 0;
    }
    int NOP;
    scanf("%d", & NOP);
    for (int i=0;i < NOP;i++)
    {
        int Number;
        int Score;
        scanf("%d %d", & Number, & Score);
        School[Number-1] += Score;
    }
    int Max=0;
    int MaxID;
    for (int i=0;i < 100000;i++)
    {
        if (School[i] > Max)
        {
            Max = School[i];
            MaxID = i;
        }
    }
    printf("%d %d", MaxID+1, Max);
    return 0;
}
'''
