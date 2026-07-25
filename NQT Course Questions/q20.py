str1 = input()
dic = {}
for i in str1 :
    if i not in dic :
        dic[i]=1
    else :
        dic[i]+=1
x = dic['"'] % 2 == 0 
y = dic['#'] % 2 == 0 
if x==y and dic['"'] % 2 == dic['#'] % 2 :
    print("0")
elif dic['"'] > dic['#'] :
    print("1")
else :
    print("-1")
