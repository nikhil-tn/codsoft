class Course:
    def __init__(self, code, title, description, capacity, schedule):
        self.code = code
        self.title = title
        self.description = description
        self.capacity = capacity
        self.schedule = schedule
        self.registered_students = []

    def display_course_info(self):
        print(f"Course Code: {self.code}")
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Capacity: {self.capacity}")
        print(f"Schedule: {self.schedule}")
        print(f"Available Slots: {self.capacity - len(self.registered_students)}")
        print()

    def register_student(self, student_id):
        if len(self.registered_students) < self.capacity:
            self.registered_students.append(student_id)
            return True
        return False

    def remove_student(self, student_id):
        if student_id in self.registered_students:
            self.registered_students.remove(student_id)
            return True
        return False


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.registered_courses = []

    def display_student_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Registered Courses: {', '.join([course.code for course in self.registered_courses]) if self.registered_courses else 'None'}")
        print()


class CourseRegistrationSystem:
    def __init__(self):
        self.courses = {}
        self.students = {}

    def add_course(self, course):
        self.courses[course.code] = course

    def add_student(self, student):
        self.students[student.student_id] = student

    def display_courses(self):
        print("\nAvailable Courses:")
        for course in self.courses.values():
            course.display_course_info()

    def register_student_for_course(self, student_id, course_code):
        if student_id in self.students and course_code in self.courses:
            student = self.students[student_id]
            course = self.courses[course_code]
            if course.register_student(student_id):
                student.registered_courses.append(course)
                print(f"Student {student_id} successfully registered for course {course_code}.")
            else:
                print(f"Course {course_code} is full.")
        else:
            print("Invalid student ID or course code.")

    def remove_student_from_course(self, student_id, course_code):
        if student_id in self.students and course_code in self.courses:
            student = self.students[student_id]
            course = self.courses[course_code]
            if course.remove_student(student_id):
                student.registered_courses.remove(course)
                print(f"Student {student_id} successfully removed from course {course_code}.")
            else:
                print(f"Student {student_id} is not registered in course {course_code}.")
        else:
            print("Invalid student ID or course code.")


if __name__ == "__main__":
    system = CourseRegistrationSystem()

    course1 = Course("CS101", "Introduction to Computer Science", "Basic concepts of computer science.", 30, "Mon/Wed 10:00-11:30")
    course2 = Course("MATH101", "Calculus I", "Introduction to differential and integral calculus.", 25, "Tue/Thu 14:00-15:30")

    system.add_course(course1)
    system.add_course(course2)

    student1 = Student("S001", "Alice")
    student2 = Student("S002", "Bob")

    system.add_student(student1)
    system.add_student(student2)

    system.display_courses()

    system.register_student_for_course("S001", "CS101")
    system.register_student_for_course("S002", "MATH101")

    student1.display_student_info()
    student2.display_student_info()

    system.remove_student_from_course("S001", "CS101")

    student1.display_student_info()
    student2.display_student_info()

    system.display_courses()               
