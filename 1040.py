# 时间复杂度：O(N)
# 解题思想：
# 如果使用多层循环来进行判断，会导致超时，因此需要思考一个优化算法
# 1.例如PPPPAAAATTTT，对于每个A来说有4个P，对于每个T来说有16个PA，因此可以构成16*4个PAT
# 2.遍历字符串，每找到一个T就记录一次，每找到一个A就累加T，每找到一个P就累加AT

String = input()  # 输入字符串

P = 0
PA = 0
PAT = 0

for i in range(0, len(String)):
    if String[i] == 'P':
        P += 1
    elif String[i] == 'A':
        PA += P
    elif String[i] == 'T':
        PAT += PA
print(PAT % 1000000007)
