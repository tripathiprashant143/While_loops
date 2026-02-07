num=int(input('enter the value:-'))
i=3
while(i<=num):
    if(num%i==0):
        print("this is not prime number:-",num)
        i+=1
        break;
    else:
        print("this is prime number:-",num)
        break; 