N = int(input())
lis = list(map(int,input().split()))
print(lis)
for i in range(1,N+1):
    if i not in lis :
        print(i)
        break
