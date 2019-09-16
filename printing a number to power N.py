N=int(input())
product=0
N1=(str(m) for m in str(N))
N2=(int(x) for x in N1)
P=len(str(N))
for i in N2:
    product+=(i**P)
print(product)
    
