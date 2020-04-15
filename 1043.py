# 时间复杂度:O(logN)
# 解题思想：
# 1.记录字符串中P、A、T、e、s、t的个数
# 2.使用while循环对字符串进行拼接，直至6个字母的计数都为0

String = input()
P = String.count('P')
A = String.count('A')
T = String.count('T')
e = String.count('e')
s = String.count('s')
t = String.count('t')

String = ""
while P > 0 or A > 0 or T > 0 or e > 0 or s > 0 or t > 0:
    if P > 0:
        String += 'P'
        P -= 1
    if A > 0:
        String += 'A'
        A -= 1
    if T > 0:
        String += 'T'
        T -= 1
    if e > 0:
        String += 'e'
        e -= 1
    if s > 0:
        String += 's'
        s -= 1
    if t > 0:
        String += 't'
        t -= 1
print(String)
