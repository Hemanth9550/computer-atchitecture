a=int(input("enter the number1:"))
b=int(input("enter the number 2:"))
c=4
f=0
ch=int(input("1.add,2.sub,3.mul,4.div:"))
if(ch==1):
    res=a+b
elif(ch==2):
    res=a-b
elif(ch==3):
    res=a*b
elif(ch==4):
    if(b==0):
        print("denominator cannot be zero")
        print("wrong ibput")
        f=1
    else:
        res=a/b
else:
    print("wrong input")
    f=1
if(f==0):
    print("the cycle vallue is:",c)
    ins=int(input("enter the no instructions:"))
    print("performance measure :",ins/c)
    print("res=",res)
