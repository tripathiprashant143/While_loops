a=int(input('enetr the value:-'))
i=2
sum=0
if(a%2==0):
    while(a>=i):
        print(a,end="")
        sum=sum+a
        if(a>i):
            print("+",end="")
        a-=2
    print("=",sum)
else:
    while(a>=i-1):
        print(a,end="")
        sum=sum+a
        if(a>i):
            print("+",end="")
        a-=2
    print("=",sum)



# or

num = int(input('enter the value :- '))
i = 1
sum=0
if num % 2 != 0:
    while num>=i:
        print(num, end="")
        sum=sum+num
        if(num>i):
            print("+",end="")
        num -= 2
    print("=",sum)
else:
    print('only you can give the odd numbers!!!!')