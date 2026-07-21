s = input()
words = s.split()
news = ""
for i in words :
    a=i.lower()
    news+=a
if news == news[::-1] :
    print("YES")