n = int(input())
students = []
for _ in range(n):
  name, dd, mm, yy = map(str, input().split())
  dd = int(dd)
  mm = int(mm)
  yy = int(yy)
  student = [name, dd, mm, yy]
  students.append(student)
students.sort(key=lambda x: (x[3], x[2], x[1]))
print(students[-1][0])
print(students[0][0])