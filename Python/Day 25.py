# Enter your code here. Read input from STDIN. Print output to STDOUT


def solve(n):
    if n ==1:
        print("Not prime")
        return
    i=2
    while(i*i<=n+1):
        if(n%i==0):
            print("Not prime")
            return
        i+=1
    print("Prime")

n = int(input())

for i in range(n):
    num = int(input())
    solve(num)
