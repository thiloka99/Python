if __name__ == '__main__':
    n = int(input("Enter the number of students' records: "))

    student_marks = {}
    for _ in range(n):
        name, *marks = input("Enter the name and marks separated by space: ").split()
        student_marks[name] = list(map(float, marks))

    query_name = input("Enter the name of the student to query: ")

    marks = student_marks[query_name]
    average = sum(marks) / len(marks)

    print(f"{average:.2f}")
   
