n = int(input())
arr = input().split()
s = "".join(arr)
for i in range(n):
    for j in range(i+1,n+1):
        print(s[i:j], end=" ")