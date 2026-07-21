s = input()
vow = "aeiou"
spaces,vowels,consonants,special=0,0,0,0
for i in s :
    if i == " " :
        spaces+=1
    elif i.isalpha() :
        a = i.lower()
        if a in vow :
            vowels+=1
        else :
            consonants += 1
    else :
        special +=1
print(vowels)
print(consonants)
print(special)
print(spaces)