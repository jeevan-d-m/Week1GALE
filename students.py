class Subjects():
    def __init__(self, subject_name):
        self.subject_name = subject_name
        self.marks = {}

    def add_marks(self, semester_number, marks):
        self.marks[semester_number] = marks

    def get_marks(self, semester_number=None):
        return self.marks.get(semester_number, "No marks available")


class Semester():
    def __init__(self, semester_number, subjects: list):
        self.semester_number = semester_number
        self.subjects = subjects


class Student():
    def __init__(self, student_name, student_USN, student_semesters: list):
        self.student_name = student_name
        self.student_USN = student_USN
        self.student_semesters = student_semesters

    # def get_marks(self, sem):
    #     for semester in self.student_semesters:
    #         if semester.semester_number == sem:
    #             print(f"Semester {sem} Marks:")
    #             for subject in semester.subjects:
    #                 print(f"{subject.subject_name}: {subject.get_marks(sem)}")
    #             return
    #     print(f"No marks found for Semester {sem}")

    # def get_marks(self, subject, semester_number):
    #     return subject.marks.get(semester_number, "No marks")


    def get_score(self, sem=None):
        if sem == None:
            sem = self.student_semesters[-1].semester_number
        for semester in self.student_semesters:
            if semester.semester_number == sem:
                print(f"Semester {sem} Marks:")
                for subject in semester.subjects:
                    print(f"{subject.subject_name}: {subject.get_marks(sem)}")
                return
        print(f"No marks found for Semester {sem}")


kannada = Subjects("Kannada")
english = Subjects("English")
maths = Subjects("Maths")


kannada.add_marks(1, 80)
english.add_marks(1, 60)

kannada.add_marks(2, 85)
english.add_marks(2, 70)
maths.add_marks(2, 99)
maths.add_marks(3, 95)



sem1 = Semester(1, [kannada, english])
sem2 = Semester(2, [kannada, english, maths])
sem3 = Semester(3, [maths, kannada])


jeevan = Student("jeevan", "4vv21cs096", [sem1, sem2, sem3])
yashwanth = Student("yashwanth","4vv21cs100",[sem1,sem2,sem3])


jeevan.get_score(1)
print("\n")
jeevan.get_score(2)
print("\n")
jeevan.get_score()
print("\n")
# jeevan.get_score(4)