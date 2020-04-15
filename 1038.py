# 时间复杂度：两个算法均O(N)
# 解题思想：
# 1.Python直接使用count方法进行查询
# 但使用Python会导致最后一个测试点超时
# 一开始认为超时是因为Python性能的缘故，因此尝试了Java、C语言使用双层循环计数的方法，但是仍然超时
# 2.突然想到一个办法，何不直接创建一个100长度的数组，每输入一个成绩就将对应下标的元素值+1
# 这样就省去了查询的时间，直接输出查询的成绩对应下标的数组元素即可
# 使用这个方法大大提高了效率！

NOS = int(input())  # 输入成绩个数,Number Of Students
Score = list(map(int, input().split()))  # 存放学生成绩
Query = list(map(int, input().split()))  # 存放查询次数、具体查询的成绩
NOQ = Query[0]  # 将查询次数单独存放，便于后续操作，Number Of Queries
Query.pop(0)  # 将查询次数从列表从删除，只保留具体查询的成绩，便于后续操作

for i in range(NOQ - 1):  # 为了保证输出没有多余的空格，只查询n-1个成绩
    print(Score.count(Query[i]), end=' ')
print(Score.count(Query[len(Query) - 1]))  # 查询第n个成绩

'''
#include<stdio.h>

int main(void){
    int Frequency[100];//创建一个数组，存放0-100分每个成绩的个数

    for(int i=0;i<100;i++)
    {
        Frequency[i]=0;//数组初始化，将每个成绩的个数默认为0
    }

	int NOS;//成绩个数
    scanf("%d",&NOS);
	int Score;
	for(int i=0;i<NOS;i++)
	{
		scanf("%d",&Score);//输入成绩
        Frequency[Score]++;//将成绩对应下标的数组元素+1，例如76分，则Frequency[76]++
	}
	int NOQ;//查询成绩的个数
    scanf("%d",&NOQ);
	int Query[NOQ];
	for(int i=0;i<NOQ;i++)
	{
		scanf("%d",&Query[i]);//输入查询的成绩
	}
	for(int i=0;i<NOQ-1;i++)//输出前n-1个成绩对应的次数
	{
		printf("%d ",Frequency[Query[i]]);
	}
	printf("%d",Frequency[Query[NOQ-1]]);//输出第n个成绩对应的次数
}

'''
