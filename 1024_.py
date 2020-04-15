String = input()
Number = float(String[:String.find('E')])  # -1.2E+10中的-1.2部分
Index = int(String[String.find('E') + 1:])  # -1.2E+10中的10^10部分
Length = String.find('E') - String.find('.') - int(String[String.find('E') + 1:])  # 计算后应该满足的小数位长度

NewNumber = Number * 10 ** Index
NewLength = len(str(NewNumber)) - str(NewNumber).find('.')  # 此时的小数位长度
# print(NewNumber, Length, NewLength)
if NewLength < Length:
    NewNumber = str(NewNumber) + (Length - NewLength) * '0'
elif NewLength > Length:
    NewNumber = int(str(NewNumber)[:str(NewNumber).find('.')])
print(NewNumber)
