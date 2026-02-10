sp=int(input('enter the starting point :-'))
ep=int(input('enter the ending point:-'))
sum=0
if(sp%2==0 and ep%2==0):
    for i in range(sp,ep+1,2):
        print(i,end="")
        if(i<ep):
            print("+",end="")
        sum=sum+i
    print("=",sum)
elif(sp%2!=0 and ep%2==0):
    for i in range(sp+1,ep+1,2):
        print(i,end="")
        if(i<ep):
            print("+",end="")
        sum=sum+i
    print("=",sum)
elif(sp%2==0 and ep%2!=0):
    for i in range(sp,ep+1,2):
        print(i,end="")
        if(i<ep-1):
            print("+",end="")
        sum=sum+i
    print("=",sum)
else:
    for i in range(sp+1,ep+1,2):
        print(i,end="")
        if(i<ep-1):
            print("+",end="")
        sum=sum+i
    print("=",sum)