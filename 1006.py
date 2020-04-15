# 时间复杂度：O(n)
# 解题思想：
# 1.百位数字=Number//100
# 2.十位数字=Number%100//10
# 3.个位数字=Number%100%10
# 4.python字符串乘法以及//、/、%的区别
Number = int(input())
String = (Number // 100) * 'B' + (Number % 100) // 10 * 'S'  # 百位、十位操作
for i in range(1, Number % 100 % 10 + 1):  # 个位操作
    String += str(i)
print(String)
