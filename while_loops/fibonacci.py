num=int(input("enter the number:-"))
a=0
b=1
i=0
while(i<num):
    print(a,end="")
    c=a+b
    a=b
    b=c
    i+=1