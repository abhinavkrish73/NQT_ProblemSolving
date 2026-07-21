arr = list(map(int,input().split()))
max1,max2=0,0
for i in arr :
    if i > max1 :
        max2 = max1
        max1 = i
    elif i > max2 and i != max1 :
        max2 = i
print(max2)