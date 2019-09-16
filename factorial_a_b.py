def factorial(N):
    if (N==0):
        return 1
    else:
        Fact=1
        for i in range(N,1,-1):
            Fact=Fact*i
        return Fact
N,K=map(int,input().split())
if(N <= 10000 and K <= 10000 and N-K<=5):
    a=factorial(N)
    b=factorial(K)
    output=a/b
    print(int(output))
