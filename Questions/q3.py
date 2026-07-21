arr = list(map(int, input().split()))
print(arr)
dum=[]
k=0
for i in range(len(arr)) :
    if arr[i] != 0 :
        dum.append(arr[i])
while len(arr)!=len(dum) :
    dum.append(0)
for i in range(len(arr)):
    arr[i]=dum[i]
print(arr)