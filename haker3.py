
records = []

for in range(int(input())):
    name = input()
    score = float(input())
    records.append([name, score])

grades = set([record[1] for record in records])
second_lowest_grade = sorted(grades)[1]

students = [record[0] for record in records if record[1] == second_lowest_grade]
students.sort()

for student in students:
    print(student)
