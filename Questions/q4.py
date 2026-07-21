q = int(input())
tt = []
for i in range(q) :
    tt.append(int(input()))
for i in tt :
    n = (i*(i-1)//2)
    print(n)