n = int(input())
m = int(input())
prime = []
finalprime = []
s,num=0,0
for i in range(n,m+1) :
    if i<2 :
        continue
    flag = 0
    for j in range(2,i//2+1) :
        if i%j == 0 :
            flag = 1
            break
    if flag == 0 :
        prime.append(i)
for i in prime :
    num = i
    s = 0
    while (num!=0) :
        dig = num%10
        s+=dig
        num=num//10
    if s<2 :
        continue
    flag = 0
    for j in range(2,s//2+1):
        if s%j == 0 :
            flag = 1
            break
    if flag == 0 :
        finalprime.append(i)
print(finalprime)
    