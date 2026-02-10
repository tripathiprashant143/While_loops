sp=int(input('enter the starting point:-'))
ep=int(input('enter the ending point:-'))
sum=1
for i in range(ep,sp-1,-1):
    print(i,end="")
    if(i>sp):
        print("*",end="")
    sum=sum*i
print("=",sum)