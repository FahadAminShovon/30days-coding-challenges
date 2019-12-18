# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT

a = list(map(int,input().split()))
b = list(map(int,input().split()))

if a[2]>b[2]:
    print(10000)
elif a[1]>b[1] and a[2]==b[2]:
    print((a[1]-b[1])*500)
elif a[0]>b[0]and a[1]==b[1] and a[2]==b[2]:
    print((a[0]-b[0])*15)
else:
    print(0)
