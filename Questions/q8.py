s = input()
rev = ""
words = ""
words = s.split()
for i in words :
    revw = i[::-1]
    rev = rev + revw + " "
print(rev)