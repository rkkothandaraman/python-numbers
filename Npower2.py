def power2(N):
    if(N==0):
        return False
    while(N!=1):
        if(N%2!=0):
            return False
        N=N//2
    return True
        
N=int(input())
M=power2(N)
if(M):
    print("yes")
else:
    print("no")
