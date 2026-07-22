s = input()
for i in s :
    if ord(i)>=ord('A') and ord(i)<=ord('Z') :
        exit
p = int(input())
dic={}
result=""
for i in s :
    if i not in dic :
        dic[i]=1
    else :
        dic[i]+=1
for key in dic :
    if dic[key] >= p :
        result+=key
print(min(result))