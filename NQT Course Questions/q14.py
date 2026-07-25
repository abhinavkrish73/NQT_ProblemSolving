n = int(input())
names = []
age = []
grade = []
gender = []
names20 = []
tot=0
avg=0.0
c=0
for i in range(n):
    parts = input().split()
    names.append(parts[0])
    age.append(int(parts[1]))
    grade.append(parts[2])
    gender.append(parts[3])
for i in range(n):
    if age[i]>20 :
        names20.append(names[i])
    if gender[i] == 'Female' :
        tot += ord(grade[i])
        c+=1
avg = tot/c
print(names20)
print(avg)