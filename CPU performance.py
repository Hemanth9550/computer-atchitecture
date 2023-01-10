p=int(input("enter no of processors:"))
ct=[]
for i in range(p):
    cpi=float(input("enter the cycle per instructions:"))
    cr=float(input("enter the clock rate in GHZ:"))
    a=1000*(cpi/cr)
    ct.append(a)
print("the processor has lowest execution time:",min(ct))
