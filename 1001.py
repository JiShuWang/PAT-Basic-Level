# 时间复杂度：O(logN)
# 解题思想：
# 1.while循环
Number = int(input())
Count = 0
while Number != 1:
    if Number % 2 == 0:
        Number /= 2
    else:
        Number = (3 * Number + 1) / 2
    Count += 1  # Number!=1时都需要砍一刀
print(Count)
