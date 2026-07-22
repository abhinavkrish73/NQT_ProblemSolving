s = input()
o = input()
result=""
dic = {}
for i in s :
    if i not in dic :
        dic[i]=1
    else :
        dic[i]+=1
for i in o :
    if i in dic :
        result+= i*dic[i]
print(result)