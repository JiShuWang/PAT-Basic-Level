import math

Start, End = map(int, input().split())
PrimeJudge = True  # 标记该数是否为素数，默认为是
PrimeCount = 0  # 记录当前素数的位置
PrimeNumber = list()  # 存储素数的列表
PrintCount = 0  # 控制输出的计数
for i in range(2, 200000):
    PrimeJudge = True  # 每次判断一个数就重置标记
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            PrimeJudge = False
            break
    if PrimeJudge == True:
        PrimeCount += 1
        if Start <= PrimeCount <= End:
            PrimeNumber.append(i)
    if PrimeCount > End:
        break
for i in range(len(PrimeNumber)):
    PrintCount += 1
    if i == len(PrimeNumber) - 1:
        print(PrimeNumber[len(PrimeNumber) - 1])
    elif PrintCount < 10:
        print(PrimeNumber[i], end=" ")
    else:
        print(PrimeNumber[i])
        PrintCount = 0
