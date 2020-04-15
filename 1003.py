# 时间复杂度：最好O(n)，最差O(n^2)
# 解题思想：
# 1.首先判断条件1
# 2.对条件2和条件3进行合并判断
# 3.条件3是递归定义，但是也有简单的规律可循
# 4.根据条件3的定义，发现条件3的规律如下：
# xPATx
# xPAATxx
# xPAAATxxx
# xPAAAATxxxx
# xPAAAAATxxxxx
# ······
# 可以发现P与T之间A的个数与T右边x的个数一致，而P左边的x永远只有一个
# 因此x*(P与T之间A的个数)=T右边x的个数
# 在Python中，可以对字符串进行乘法运算，3*'A'="AAA"
NOS = int(input())
List = list()
for i in range(NOS):
    Judge = True  # 条件1标记
    String = input()
    if 'P' in String and 'A' in String and 'T' in String:  # 判断是否有P、A、T
        for j in range(len(String)):
            if String[j] != 'P' and String[j] != 'A' and String[j] != 'T':  # 判断是否仅有P、A、T
                Judge = False
                break
    else:
        Judge = False
    if Judge == True:  # 满足条件1
        a = String[:String.find('P')]  # 截取P左边的字符串
        b = String[String.find('P') + 1:String.rfind('T')]  # 截取P与T之间的字符串
        c = String[String.rfind('T') + 1:]  # 截取T右边的字符串
        if (a == c and b == 'A') or (len(b) * a == c):  # 满足条件2或条件3
            print("YES")
        else:  # 不满足条件2和条件3
            print("NO")
    else:  # 不满足条件1
        print("NO")
