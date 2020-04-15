#时间复杂度
Number = list(map(int, input().split()))
Coefficient, Index = list(), list()  # 存放多项式的系数、指数
for i in range(len(Number)):
    if i % 2 == 0:
        Coefficient.append(Number[i])
    else:
        Index.append(Number[i])
for i in range(len(Coefficient)):
    if Coefficient[i] != 0 and Index[i] != 0:
        Coefficient[i] *= Index[i]
        Index[i] -= 1
        print(Coefficient[i],end=" "+str(Index[i])+" ")
    elif Coefficient[i] == 0:
        Coefficient[i], Index[i] = 0, 0
        print(Coefficient[i], end=" "+str(Index[i])+" ")
