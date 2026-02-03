num=int(input('enter the value:-'))
h=0
s_h=0
while(num>0):
    x=num%10
    num//=10
    if(x>h):
        s_h=h
        h=x
    elif(x>s_h and x!=h):
        s_h=x
print(h,"this is the largest value")
print(s_h, "this is the second largest value")