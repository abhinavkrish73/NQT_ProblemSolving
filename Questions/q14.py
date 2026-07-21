n = int(input())
binary = []
while n!=0 :
    dig = n%2
    binary.append(dig)
    n = n//2
print(binary)
binarys = " ".join(map(str,binary))
binarys = binarys[::-1]
print(binarys)