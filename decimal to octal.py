n=int(input("Nmber:"))
m=1
sum=0
while(n>0):
    r=n%8
    sum+=r*m
    m=m*10
    n=n//8
print("the octal value is :",sum)
