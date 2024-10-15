def analyze_grades(students_grades):
    
    total_grades = 0 # сумма всех баллов

    # проходимся по каждому студенту
    for student in students_grades:
        # из каждого элемента (кортежа) забираем балл студента
        name, grade = student
        
        total_grades += grade

    average_grade = total_grades / len(students_grades) # поиск ср. арф. балла
    
    above_average_students = [] # студенты, чьи баллы выше ср. арф.
    for student in students_grades:
        name, grade = student
        
        if grade > average_grade:
            # если балл выше ср. арф., добавляем имя студента в новый список
            above_average_students.append(name)

    count_above_average = len(above_average_students)

    return (above_average_students, average_grade, count_above_average)

# Тест 1
students_grades_1 = [("Nikita", 85), ("Oleg", 70), ("Tamara", 95), ("Svetlana", 80)]
print(analyze_grades(students_grades_1))

# Тест 2
students_grades_2 = [("Valentina", 60), ("Durak", 65), ("Bob", 70), ("Kopatich", 75)]
print(analyze_grades(students_grades_2))

# Тест 3
students_grades_3 = [("Крош", 100), ("Ёжик", 90), ("Змей Горыныч", 80), ("какой-то мужик", 70), ("чувак", 60)]
print(analyze_grades(students_grades_3)) 
