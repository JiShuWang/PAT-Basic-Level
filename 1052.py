# 时间复杂度：O(N)，双层循环，但是内循环最大为常数4
# 解题思想：
# 1.创建一个函数来去除括号，获取具体表情
# 2.对输入的序号进行判断

def GetEmoj():
    List = list()
    String = input()
    for i in range(len(String)):
        if String[i] == '[':
            for j in range(i + 1, len(String)):
                if String[j] == ']':
                    List.append(String[i + 1:j])
                    break
    return List


Hand = GetEmoj()
Eye = GetEmoj()
Mouth = GetEmoj()

NOR = int(input())  # 输入请求数
for i in range(NOR):
    String = ""
    Choose = list(map(int, input().split()))  # 输入五个表情的选择
    if Choose[0] > len(Hand) or Choose[4] > len(Hand) or Choose[1] > len(Eye) or Choose[3] > len(Eye) or Choose[
        2] > len(Mouth):  # 某个序号对应的表情不存在
        String = "Are you kidding me? @\/@"
    else:
        String = Hand[Choose[0] - 1] + '(' + Eye[Choose[1] - 1] + Mouth[Choose[2] - 1] + Eye[Choose[3] - 1] + ')' + \
                 Hand[Choose[4] - 1]
    print(String)
