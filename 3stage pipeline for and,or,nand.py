a=int(input("Enter number 1:"))
b=int(input("enter the number 2:"))
c=4
rand=a&b
ror=a|b
rnand=~rand
print("the cycle value is",c)
ins=int(input("enter the no of instructions"))
print("the performance measure:",ins/c)
print("result and=",rand)
print("result or=",ror)
print("result nand=",rnand)
