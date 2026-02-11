sp=int(input('enter the starting point:-'))
ep=int(input('enter the ending point:-'))
sp+=sp%2
num=sp
for i in range(sp,ep+1,2):
    print(i)