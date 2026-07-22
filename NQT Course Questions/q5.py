print("Input String : ")
s = input()
print("Value : ")
v = int(input())
result = ""
for i in s :
    if i == "@" :
        result+="#"
    elif i >= "A" and i<="Z" :
        result+=chr((ord(i)-ord('A')+v)%26+ord('A'))
    elif i >= "a" and i<="z" :
        result+=chr((ord(i)-ord('a')+v)%26+ord('a'))
    elif i>="0" and i<="9" :
        result+=str((int(i)+v)%10)
    else :
        result+="@"
print(result)