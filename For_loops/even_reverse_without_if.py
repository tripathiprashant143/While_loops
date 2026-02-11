sp=int(input('enter the statring point:-'))
ep=int(input('enter the ending point:-'))
ep-=ep%2
num=ep
for i in range(num,sp-1,-2):
    print(i)