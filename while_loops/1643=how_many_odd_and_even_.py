num=int(input('enter the value:-'))
rev=0
c=0
i=0
sum=0
sum2=0
while(num>0):
    x=num%10
    rev=rev*10+x
    num//=10
    if(x%2==0):
        print(x,':-is even number')
        sum=sum+x
        c+=1
    else:
        print(x,':-is odd number')
        i+=1
        sum2=sum2+x
print('the sum of even value is :-',sum)
print('the sum of even value is :-',sum2)
print('total even number is:-',c)
print('total odd number is:-',i)