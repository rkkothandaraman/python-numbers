N=input()
count=0
Newlist=[str(n) for n in str(N)]
Q=[int(d) for d in str(N)]
sum=Q[0]+Q[1]
strsum=str(sum)
for i in range(len(N)-1):
    B=N[i]+N[i+1]
    Newlist.append(B)
if(strsum in B):
    print(1)
else:
    print(0)
