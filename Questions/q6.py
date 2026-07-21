n = int(input())
if n%2 == 0 :
    exit
arr = []
for i in range(n):
    arr.append(int(input()))
ans=0
for x in arr :
    ans = ans^x
print(ans)
