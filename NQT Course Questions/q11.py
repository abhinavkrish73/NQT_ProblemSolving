x = int(input())
y = int(input())

a = x
b = x

while(a%y!=0) :
    a+=1

while(b%y!=0) : 
    b-=1

if (a-x) < (x-b) :
    print(a)
else :
    print(b)