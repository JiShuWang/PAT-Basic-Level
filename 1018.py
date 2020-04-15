# 时间复杂度：O(n)
# 解题思想：
# 1.多创建几个变量，在输入手势的同时记录下各个手势的获胜次数，否则最后一个测试点会超时
# 2.自定义一个方法来判断获胜最多的手势，并且注意字母序
def BestGesture(GestureB, GestureC, GestureJ):  # 判断获胜次数最多的手势，并且遵循字母序
    if GestureB >= GestureC and GestureB >= GestureJ:
        return 'B'
    elif GestureC > GestureB and GestureC >= GestureJ:
        return 'C'
    elif GestureJ > GestureB and GestureJ > GestureC:
        return 'J'


NOG = int(input())  # 输入游戏次数 Number of game
WinCountA, DrawCountA, LoseCountA = 0, 0, 0  # A赢、平、输的次数
AB, AC, AJ, BB, BC, BJ = 0, 0, 0, 0, 0, 0  # 记录A、B各个手势赢的次数

for i in range(NOG):
    A, B = input().split()
    if A == B:  # 平局
        DrawCountA += 1
    elif A == 'B':  # A：布
        if B == 'C':  # B：锤
            WinCountA += 1
            AB += 1
        else:  # B：刀
            LoseCountA += 1
            BJ += 1
    elif A == 'C':  # A:锤
        if B == 'B':  # B：布
            LoseCountA += 1
            BB += 1
        else:  # B：刀
            WinCountA += 1
            AC += 1
    else:  # A：刀
        if B == 'B':  # B：布
            WinCountA += 1
            AJ += 1
        else:  # B：锤
            LoseCountA += 1
            BC += 1

# 只需记录A胜平负的次数，就能得到B胜平负的次数
print(WinCountA, DrawCountA, LoseCountA)
print(LoseCountA, DrawCountA, WinCountA)
print(BestGesture(AB, AC, AJ), BestGesture(BB, BC, BJ))
