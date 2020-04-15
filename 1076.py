# 时间复杂度：O(N)
# 解题思想：
# 1.使用字典存放选项与密码的对应关系
# 2.找出T所在的位置-2，就是正确的选项

Answer = {
    'A': '1',
    'B': '2',
    'C': '3',
    'D': '4'
}
NOC = int(input())  # 输入选择题个数
Password = ''

for i in range(NOC):
    Option = input()
    Password += Answer[Option[Option.find('T') - 2]]
print(Password)
