class Human:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}

    def get_avr_grade(self):
        if len(sum(list(self.grades.values()), [])) == 0:
            return 'Оценок нет'
        else:
            return sum(sum(list(self.grades.values()), [])) / len(sum(list(self.grades.values()), []))

    def __lt__(self, other):
        if not isinstance(other, Human):
            return
        if self.get_avr_grade() > other.get_avr_grade():
            return f'У {self.name} {self.surname} средняя оценка лучше чем у {other.name} {other.surname}'
        else:
            return f'У {self.name} {self.surname} средняя оценка хуже чем у {other.name} {other.surname}'


class Student(Human):
    lst_student = []

    def __init__(self, name, surname, gender):
        super().__init__(name, surname)
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        Student.lst_student.append(self)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:' \
              f' {self.get_avr_grade()}\nКурсы в процессе изучения: ' \
              f'{", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res


class Mentor(Human):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_avr_grade()}'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


def get_avr_gr_students(lst_students, course_name):
    grades = [0]
    for st in lst_students:
        for course in st.grades.keys():
            if course != course_name:
                pass
            else:
                grades += st.grades[course_name]
    res = sum(grades) / len(lst_students)
    return res


def get_avr_gr_lecturers(lst_lecturers, course_name):
    grades = [0]
    for lc in lst_lecturers:
        for course in lc.grades.keys():
            if course != course_name:
                pass
            else:
                grades += lc.grades[course_name]
    res = sum(grades) / len(lst_lecturers)
    return res



student1 = Student('Ivan', 'Fomin', 'male')
student2 = Student('Nikita', 'Ivanov', 'male')

lecturer1 = Lecturer('Petr', 'Petrov')
lecturer2 = Lecturer('Sergei', 'Sergeev')

reviewer1 = Reviewer('Igor', 'Resh')
reviewer2 = Reviewer('Aleksei', 'Alekseev')

lst_students = [student1, student2]
lst_lecturers = [lecturer1, lecturer2]

student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Java']
student1.finished_courses += ['C++']

student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['C++']

lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['Java']

lecturer2.courses_attached += ['Python']
lecturer2.courses_attached += ['C++']

reviewer1.courses_attached += ['Python']
reviewer2.courses_attached += ['C++']

reviewer1.rate_hw(student1, 'Python', 2)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Python', 8)

reviewer1.rate_hw(student2, 'Python', 10)
reviewer1.rate_hw(student2, 'Python', 5)
reviewer1.rate_hw(student2, 'Python', 6)

student2.rate_lecture(lecturer2, 'Python', 9)
student2.rate_lecture(lecturer2, 'Python', 6)
student2.rate_lecture(lecturer2, 'Python', 9)

student2.rate_lecture(lecturer1, 'Python', 9)
student2.rate_lecture(lecturer1, 'Python', 6)
student2.rate_lecture(lecturer1, 'Python', 9)

print(reviewer1)
print()
print(lecturer2)
print()
print(student1)
print()
print(student1 > student2)
print()
print(lecturer1 > lecturer2)
print()
print(get_avr_gr_students(lst_students, 'Python'))
print(get_avr_gr_lecturers(lst_lecturers, 'Python'))
