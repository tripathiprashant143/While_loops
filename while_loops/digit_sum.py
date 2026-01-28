num=int(input("enter the value:-"))
sum=0
reverse=0
while(num>0):
    x=num%10
    reverse=reverse*10+x
    num//=10
    sum=sum+x
print(sum)
