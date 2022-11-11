def evenfib(n):
    evensum,prev,next1=0,0,1
    fib=[0]
    while(next1<=n):
        fib.append(next1)
        if next1 % 2==0:
            evensum = evensum+next1
        prev,next1=next1,prev+next1
    print("The sum of even valued fib sequence",fib,"is",evensum)
n=10000
evenfib(n)
