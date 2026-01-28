num = int(input('enter the value:- '))
temp = num
rev = 0
i = 0
while num > 0:
    x = num % 10
    num //= 10
    i += 1
a = i
b = 0
num = temp 
while num > 0:
    y = num % 10
    num //= 10
    b += y ** a
if b == temp:
    print('this is armstrong number!!!')
else:
    print('this is not armstrong number!!!')
