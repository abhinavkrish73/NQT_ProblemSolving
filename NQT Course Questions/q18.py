n = int(input())
arr = list(map(int,input().split()))
arr2 = []
for i in arr :
    if i%3 == 0 and i%5 == 0 :
        arr2.append("ThreeFive")
    elif i%5 == 0 :
        arr2.append("Five")
    elif i%3 == 0 :
        arr2.append("Three")
    else :
        arr2.append(i)
print(arr2)