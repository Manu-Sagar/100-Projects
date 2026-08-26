class Student:
    def __init__(self,name,marks):
        self.__name=name
        self.__marks=marks
        self.__total=0
        self.__percentage=0
        self.__grade=""
        self.__status=""
    def claculate_total(self):
        self.__total=sum(self.__marks)
    def calculate_percentage(self,No_of_sub):
        self.__percentage=(self.__total/(No_of_sub*100))*100
    def calculate_grade(self):
        if self.__percentage>=90:
            self.__grade="A+"
        elif self.__percentage>=80:
            self.__grade="A"
        elif self.__percentage>=70:
            self.__grade="B+"
        elif self.__percentage>=60:
            self.__grade="B"
        elif self.__percentage>=50:
            self.__grade="C"
        else:
            self.__grade="F"
    def determine_status(self):
        if self.__percentage>=50:
            self.__status="Pass"
        else:
            self.__status="Fail"
    def display_student(self):
        print(f"Name:{self.__name}")
        print(f"Marks:{self.__marks}")
        print(f"Total:{self.__total}")
        print(f"Percentage:{self.__percentage:.2f}%")
        print(f"Grade:{self.__grade}")
        print(f"Status:{self.__status}")
    def get_name(self):
        return self.__name
def get_student_details(No_of_sub):
    name=get_valid_name()
    marks=[]
    for i in range(No_of_sub):
        mark=get_valid_mark(i+1)
        marks.append(mark)

    student=Student(name,marks)
    student.claculate_total()
    student.calculate_percentage(No_of_sub)
    student.calculate_grade()
    student.determine_status()

    return student
def get_number_of_students():
    while True:
        try:
            no_of_students=int(input("Enter Number of Students"))
            if no_of_students>0:
                return no_of_students
            else:
                print("Print The Number greater than O")
        except ValueError:
            print("Please Enter the Valid number")
def get_number_of_sub():
    while True:
        try:
            No_of_sub=int(input("Enter Number of Subjects:"))

            if No_of_sub>0:
                return No_of_sub
            else:
                print("Number of Subjects must be greater than 0")
        except ValueError:
            print("Enter Valid Number")
def get_valid_mark(sub_no):
    while True:
        try:
            mark=float(input(f"Enter marks of subject {sub_no}:"))
            if 0<=mark<=100:
                return mark
            else:
                print("Enter the Mark between  0 and 100")
        except ValueError:
            print("Enter A valid mark")

def get_valid_name():
    while True:
        name=input("Enter the Student name:").strip()

        if name:
            return name
        else:
            print("Name Cannot be empty")
def create_students(no_of_students,no_of_sub):
    students=[]
    for i in range(no_of_students):
        print(f"Enter details of student {i+1}")
        student=get_student_details(no_of_sub)
        students.append(student)
    return students
def display_all_students(students):
    if not students:
        print("No students Found")
        return
    print("---All Students---")
    for student in students:
        student.display_student()
        print()
def search_student(students):
    if not students:
        print("No students Found")
        return
    search_name=input("Enter student name to Search:")
    for student in students:
        if student.get_name().lower()==search_name.lower():
            student.display_student()
            return
    print("Student Not Found")
def display_menu():
    print("====Student Management System====")
    print("1.Search Student")
    print("2.Display All Students")
    print("Exit")
def main():
    no_of_students=get_number_of_students()
    no_of_sub=get_number_of_sub()

    students=create_students(no_of_students,no_of_sub)
    while True:
        display_menu()
        choice=int(input("Enter your Choice:"))

        if choice==1:
            search_student(students)
        elif choice==2:
            display_all_students(students)
        elif choice==3:
            print("Thank you for using Student Management Students")
            break
        else:
            print("Invalid Choice")
if __name__ == "__main__":
    main()