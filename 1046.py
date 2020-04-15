# 时间复杂度：O(N)
# 解题思想：
# 1.只记录不同输或不同赢的情况，因为题目要求的是喝的杯数而不是输的次数

LoseA, LoseB = 0, 0  # 记录甲、乙喝的杯数
NOB = int(input())  # 输入划拳轮数

for i in range(NOB):
    ASay, ADraw, BSay, BDraw = map(int, input().split())
    if ADraw == (ASay + BSay) != BDraw:  # 甲赢、乙输
        LoseB += 1
    elif BDraw == (ASay + BSay) != ADraw:  # 甲输、乙赢
        LoseA += 1
print(LoseA, LoseB)
