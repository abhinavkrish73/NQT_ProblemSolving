n = int(input())
count = 0
num = n
org = n
s = 0
while (n!=0) :
    dig = n % 10
    count+=1
    n = n//10
while (num!=0):
    dig = num % 10
    s += dig**count
    num = num//10
print(s)
if s == org :
    print("YES")
else :
    print("NO")