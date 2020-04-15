# 时间复杂度:O(NlogN)
# 解题思想：
# 1.使用常规的素数判断方法对每个数进行判断
# 2.每找到一个素数，就与上一个素数进行比对，如果差值为2则为一个素数对
# 使用Python会导致最后一个测试点超时，使用C语言可以解决这个问题
import math

Number = int(input())  # 输入边界
PrimeNumber = [2, 3]  # 存放起始的两个素数
Count = 0  # 素数对的个数

for i in range(Number + 1):
    PrimeJudge = True  # 标记该数是否为素数，默认为是
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:  # 该数能被1、自己以外的第三个数整除
            PrimeJudge = False
            break
    if PrimeJudge == True:  # 该数为素数
        if i - 2 == PrimeNumber:  # 且与上一个素数相差2
            Count += 1
        PrimeNumber = i  # 更新为当前素数
print(Count)

'''''
#include<stdio.h>
#include<math.h>
int main(void)
{
	int number;
	scanf("%d",&number);
	int primenumber = 2;
	int primejudge = 1;
	int count = 0;
	for(int i=2;i<number+1;i++)
	{
		primejudge = 1;
		for(int j=2;j<sqrt(i)+1;j++)
		{
			if(i%j==0)
			{
				primejudge = 0;
				break;
			}
		}
		if(primejudge == 1)
		{
			if(i-2==primenumber)
			{
				count++;
				//printf("%d,%d\n",i,primenumber);
			}
			primenumber = i;
		}
	}
	printf("%d",count);
	return 0;
}

'''''
