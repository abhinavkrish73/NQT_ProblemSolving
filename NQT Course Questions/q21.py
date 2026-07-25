t = int(input())
n = int(input())
students=[]
for i in range(n):
    parts=input().split()
    marks = parts[0]
    name = parts[1]
    students.append([marks,name])
students.sort(reverse=True)
for i in range(t) :
    name = students[i][1]
    marks = students[i][0]
    print(name + ": " + str(marks))
