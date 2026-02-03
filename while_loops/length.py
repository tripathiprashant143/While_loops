num=int(input('enter the value:-'))
i=0
rev=0
while(num>0):
    x=num%10
    rev=rev*10+x
    num//=10
    i+=1
print('length is :-',i)