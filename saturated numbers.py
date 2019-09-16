N=int(input())
Q=[int(d) for d in str(N)]
P=[1,2,3,4,5,6,7,8,9,0]
Z=[]
count=0
for i in Q:
    if i not in Z:
        Z.append(i)
        count+=1
if count==2:
    print ("Saturated")
else:
    print("Unsaturated")
