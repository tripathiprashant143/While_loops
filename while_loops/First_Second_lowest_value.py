num=int(input('enter the number :-'))
l=9
s_l=9
while(num>0):
    x=num%10
    num//=10
    if(x<l):
        s_l=l
        l=x
    elif(x<s_l and x!=l):
        s_l=x
print(l,'this is the first lowest value in the data')
print(s_l,'this is the second lowest value in the data')