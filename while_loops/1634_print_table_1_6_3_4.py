num=int(input('enter the value:-'))
rev=0
tem=num
while(tem>0):
    x=tem%10
    rev=rev*10+x
    tem//=10
while(rev>0):
    y=rev%10
    rev//=10
    i=1
    while(i<=10):
        print(y,"*",i,"=",i*y)
        i+=1
    print("")
