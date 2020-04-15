# 时间复杂度：O(N)
# 解题思想：
# 1.将实际输入的文字中的坏键替换掉
# 2.针对坏键中的英文字母，将实际输入的文字中的该字母及其大写字母替换掉
# 3.如果坏键中有+键，则将实际输入的文字中的所有大写字母替换掉

DamageKey = list(input())  # 将每个坏键存放为列表元素
RealKey = input()  # 实际输入的文字

for i in range(len(DamageKey)):  # 遍历每个坏键元素
    RealKey = RealKey.replace(DamageKey[i], '')  # 将对应的坏键替换为空
    if str(DamageKey[i]).isalpha():  # 如果坏键是字母
        RealKey = RealKey.replace(str(DamageKey[i]).upper(), '')  # 将该字母的大写替换掉
        RealKey = RealKey.replace(str(DamageKey[i]).lower(), '')  # 将该字母的小写替换掉

if '+' in DamageKey:  # 上档键也是坏键
    for i in range(len(RealKey)):  # 逐个遍历实际输入的文字
        if str(RealKey[i]).isupper():  # 如果该文字是大写
            RealKey = RealKey.replace(str(RealKey[i]), '#')  # 将该文字暂时替换为#号，如果直接替换为空，会导致字符串长度改变，导致循环条件错误
RealKey = RealKey.replace('#', '')  # 再将#替换为空

print(RealKey)
