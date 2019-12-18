phoneBook = {}

num = int(input())

for i in range (0,num):
    name = input()
    temp=name.split()
    phoneBook[temp[0]]=temp[1]
    
    
for i in range(0,num):
    name = input()
    temp = phoneBook.get(name)
    if phoneBook.get(name):
        print (name,"=",temp,sep="")
    else:
        print("Not found")
