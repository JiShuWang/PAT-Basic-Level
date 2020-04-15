# 时间复杂度：O(n)
# 解题思想：
# 1.利用字典实现A~G与Day的对应
# 2.先判断Day，再判断Hour
# 3.注意Hour和Min在小于10的情况下需要补足0，例如0时6分需要补足为00:06
# 4.Hour=列表索引的值
# 可进行的优化：字符匹配不用从头开始，可以从第一个符合条件的位置开始

String = list()
for i in range(4):
    String.append(input())

DayLetter = {'A': "MON", 'B': "TUE", 'C': "WED", 'D': "THU", 'E': "FRI", 'F': "SAT", 'G': "SUN"}
HourLetter = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
              'L', 'M', 'N']

# 进行前两对字符串匹配
MatchIndex = 0  # 用于记录满足条件的索引
for i in range(min(len(String[0]), len(String[1]))):
    if String[0][i] == String[1][i] and String[0][i] in DayLetter:
        Day = String[0][i]  # 第一个相同的大写字母
        MatchIndex = i + 1  # 判断Hour时在此基础上向前一位
        break
for j in range(MatchIndex, min(len(String[0]), len(String[1]))):
    if String[0][j] == String[1][j] and String[0][j] in HourLetter:
        HH = String[0][j]  # 第二个相同的字符
        break

# 进行后两对字符串匹配
for i in range(min(len(String[2]), len(String[3]))):
    if String[2][i] == String[3][i] and String[2][i].isalpha():
        MM = i  # 第一个相同的字母
        break

Day = DayLetter[Day]
HH = HourLetter.index(HH)
if HH < 10:
    HH = '0' + str(HH)
if MM < 10:
    MM = '0' + str(MM)
print(str(Day) + ' ' + str(HH) + ':' + str(MM))
