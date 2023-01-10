n=int(input("enter the decimal"))
sum=0
m=1
while n>0:
    r=n%2
    n=n//2
    sum+=r*m
    m=m*10
print("binary",sum)
