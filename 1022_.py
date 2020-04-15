A, B, D = map(int, input().split())
Decimal, New = A + B, 0

while Decimal > 0:
    if Decimal >= D:
        Decimal -= D
        New += 10
    else:
        New += Decimal
        Decimal = 0
    if str(D) in str(New) and str(New)[0] != str(D):
        New += (10 - D) * 10 ** (len(str(New)) - 1 - str(New).index(str(D)))
    if str(D) in str(New) and str(New)[0] == str(D):
        New = int(str(New).replace(str(D), '10'))
print(New)
