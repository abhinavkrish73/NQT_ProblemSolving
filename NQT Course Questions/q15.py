str1 = input()
num = []
num2 = []
for i in str1.split() :
    if i.isdigit() :
        num.append(i)
print(num)
for i in num :
    if '9' not in i :
        num2.append(i)
print(num2)