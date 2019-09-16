N=int(input())
list=[]
for i in range(1,N+1):
    if(N%i==0):
        list.append(i)
for i in range(len(list)):
    print(list[i], end=" ")
