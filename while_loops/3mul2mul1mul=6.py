a=int(input('enter the value:-'))
sum=1
while(a>0):
    print(a,end="")
    sum=sum*a
    if(a>1):
        print("*",end="")
    a-=1
print("=",sum)