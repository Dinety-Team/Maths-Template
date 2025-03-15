import math
def bif(a):
    return math.log(2 * a) + 2 * a + a ** 2 + 3
a = float(input('二分法下界'))
b = float(input('二分法上界'))
v = float(input('精确度'))
while abs(a-b) >= v:
    c = (a + b) / 2
    if (bif(a) * bif(c)) < 0:
        b = c
        continue
    elif (bif(c)) == 0:
        a = c
        break
    else:
        a = c 
        continue
x = a
print('x =',a)