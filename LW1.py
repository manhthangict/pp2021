Student = []
StudentName = []
StudentDoB = []
StudentID = []
Course = []
CourseID = []
CourseName = []
Mark = []

# student in class
def Nos():
    student = int(input("Enter total number of student:"))
    if student == 0 or student < 0:
        print("Class invalid")
        return 0
    else:
        return student

# Add student information
def Addstd():
    print("STUDENTS IN THE CLASS")
    name = input("Enter Student's name: ")
    id = input("Enter Student's ID: ")
    dob = input("Enter Student's DoB: ")
    std = {
        'id': id,
        'name': name,
        'dob': dob,
        }
    StudentID.append(id)
    StudentName.append(name)
    StudentDoB.append(dob)
    Student.append(std)
    return std
    print("")


# Input number of course
def Noc():
    cn = int(input("Enter the number of course: "))
    if cn < 0 or cn == 0:
        print("Course invalid")
        return 0
    else:
        return cn


# Add Course
def Addc():
    print("COURSE")
    name = input("Enter course's name:")
    id = input("Enter course's ID: ")

    cse = {
        'name': name,
        'id': id
    }
    CourseName.append(name)
    CourseID.append(id)
    Course.append(cse)
    print("")


# Create mark for students
def Markstd():
    print("MARK OF STUDENT")
    a = 1
    student = len(Student)
    while a <= student:
        a += 1
        markname = input("Enter the Student Name: ")
        if markname in StudentName:
            for i in range(0, len(CourseName)):
                coursename = input("Enter the Course Name: ")
                if coursename in CourseName:
                    mark = float(input("Enter Student Mark: "))
                    mrk = {
                        'markname': markname,
                        'coursename': coursename,
                        'mark': mark
                    }
                else:
                    print("Student Name not found ")
                    break
                Mark.append(mrk)
        else:
            print("Course Name not found")
            break
    print("")


def Student_list():
    print("STDUDENT LIST")
    for i in range(0, len(Student)):
        print(f"ID: {Student[i]['id']}")
        print(f"Name: {Student[i]['name']}")
        print(f"DoB: {Student[i]['dob']}")
        print("")


def Course_list():
    print("COURSE LIST")
    for i in range(0, len(Course)):
        print(f"ID:{Course[i]['id']}")
        print(f"Name : {Course[i]['name']}")
        print("")


def Mark_list():
    print("MARK LIST")
    for i in range(0, len(Mark)):
        print(f"ID-course: {Mark[i]['b']}")
        print(f"ID-Student: {Mark[i]['a']}")
        print(f"mark:{Mark[i]['mark']}")
        print("")

