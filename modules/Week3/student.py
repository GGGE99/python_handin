from functools import reduce
class Student:
    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def get_avg_grade(self):
        sum = 0
        n = 0
        for grade in self.data_sheet.courses:
            if not len(grade['Grade']) > 2:
                sum += int(grade['Grade'])
                n += 1
        return sum/n

    def get_progression(self, max = 150):
        points = reduce(lambda a,b: int(a) + int(b),[passed['Course'].ETCS for passed in self.data_sheet.courses if passed['Grade'].strip(' ') != 'None'])
        return points/max * 100


    def to_str(self):
        return f'{self.name}, {self.gender}, {self.data_sheet.to_str()}, {self.image_url}\n'

class DataSheet:
    def __init__(self, courses):
        self.courses = [{'Course':c, 'Grade': None} for c in courses]

    def set_grade(self, course, grade):
        next(sub for sub in self.courses if sub['Course'] == course)['Grade'] = grade

    def get_grades(self):
        return [c['Grade'] for c in self.courses]
    
    def to_str(self):
        res = ''
        for c in self.courses:
            res += f'{c["Course"].to_str()}, {c["Grade"]}'
        return res


class Course:
    def __init__(self, name, classroom, teacher, ETCS):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS

    def to_str(self):
        return f'"{self.name}, {self.classroom}, {self.teacher}, {self.ETCS}"'

import random

def get_name(first_names, last_names=None):
    f_name = first_names[random.randint(0, len(first_names) - 1)]
    l_name = ''
    if not last_names == None: l_name = ' ' + last_names[random.randint(0, len(last_names) - 1)]
    return f_name + l_name

def make_datasheet(courses, target):
    sum = 0
    selected_courses = []
    while sum < target:
        course = random.choice(courses)
        if not selected_courses.__contains__(course):
            sum += course.ETCS
            selected_courses.append(course)
    return DataSheet(selected_courses)

def make_students(number=1):
    with open ('./data/names.csv') as name_file: names = [n.strip() for n in name_file.readlines()]
    with open ('./data/courses.csv') as course_file: courses_names = [n.strip() for n in course_file.readlines()]
    with open ('./data/img.csv') as image_file: images = [n.strip() for n in image_file.readlines()]
    with open ('./data/last_names.csv') as last_names_file: last_names = [n.strip() for n in last_names_file.readlines()]
    with open ('./data/rooms.csv') as room_file: rooms = [n.strip() for n in room_file.readlines()]
    genders = ['Male', 'Female']
    ETCS = [5,10,15]
    grades = [2,4,7,10,12]

    courses = [Course(c, random.choice(rooms), get_name(names, last_names), random.choice(ETCS)) for c in courses_names]
    datasheets = [make_datasheet(courses, 150) for n in range(number)]
    students = [Student(random.choice(names), random.choice(genders), datasheets[i], random.choice(images)) for i in range(number)]

    for s in students:
        for c in s.data_sheet.courses:
            if random.choice([1, 2]) == 1:
                s.data_sheet.set_grade(c['Course'], random.choice(grades))
    with open ('./data/students.csv', 'w') as file:
        for student in students: file.write(student.to_str())

def read_students(r=True):
    students = []
    with open ('./data/students.csv') as file:
        students_info = file.readlines()
        for student_info in students_info:
            courses, grades = [], []
            arr = [s for s_part in student_info.split('"') for s in s_part.split(',') if len(s.strip(" ")) > 0]
            name, gender, img_url = arr[0],arr[1],arr[-1]
            arr = arr[2: -1]
            for i in range(len(arr) - 1): 
                if (i + 1) % 5 == 0:
                    courses.append(Course(arr[i-4],arr[i-3],arr[i-2],arr[i-1]))
                    grades.append(arr[i])
            
            student = Student(name, gender, DataSheet(courses), img_url)
            students.append(student)

            for c in courses:
                student.data_sheet.set_grade(c, grades[courses.index(c)])
            
    return sorted(students, key=lambda k: k.get_avg_grade(), reverse=r)


# stud = read_students()
# print(stud[0].data_sheet.get_grades())
# print(stud[0].get_avg_grade())

# make_students(10)