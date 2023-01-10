a=int(input("enter number1:"))
b=int(input("number2:"))
c=3
f=0
ch=int(input("1.Add,2.Sub,3.Mul,4.Div"))
if ch==1:
    print("performing addition operation")
    res=a+b
elif ch==2:
    print("performing subtraction operation")
    res=a-b
elif ch==3:
    print("performing multiplication operation")
    res=a*b
elif ch==4:
    print("performing division operation")
    if(b==0):
        print("denominator cannot be zero")
        print("wrong input")
        f=1
    else:
        res=a/b
else:
    print("wrong input")
    f=1
if(f==0):
    print("the cycle value is:",c)
    ins=int(input("enter no of instructions"))
    print("performance measure:",ins/c)
