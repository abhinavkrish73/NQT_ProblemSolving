n = int(input())
b = ""
b1 = ""
while n!=0 :
    b = str(n%2) + b
    n = n//2
for i in b :
    if i == '1' :
        i = '0'
        b1 += i
    else :
        i = '1'
        b1 += i
d = 0
p = 0
for i in b1[::-1]:
    d += int(i) * (2**p)
    p += 1
print(d)