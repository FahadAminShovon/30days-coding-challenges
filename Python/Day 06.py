n = int(input())

for i in range(0,n):
    strr = input()
    sz = len(strr)
    for j in range(0,sz,2):
        print(strr[j],end="")

    print(end=" ")

    if sz>1:
        for j in range(1,sz,2):
            print(strr[j],end="")

    print()
