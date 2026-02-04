sp=int(input('enter the starting point:-'))
ep=int(input('enter the ending point:-'))
a=ep-1
if(ep%2!=0):
    while(ep>=sp):
        print(ep)
        ep-=2
else:
    while(a>=sp):
        print(a)
        a-=2