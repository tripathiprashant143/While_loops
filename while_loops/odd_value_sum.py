a=int(input("enter the value:-"))
sum=0
i=1
if(a%2!=0):
    while(i<=a):
        if(i%2!=0):
            print(i,end="")
            sum=sum+i
            if(i<a):
                print("+",end="")
        i+=2
    print("=",sum)
else:
    while(i<=a):
        if(i%2!=0):
            print(i,end="")
            sum=sum+i
            if(i<a-1):
                print("+",end="")
        i+=2
    print("=",sum)

