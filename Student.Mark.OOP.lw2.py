import math
import numpy as np
import curses

Student = []
StudentName = []
StudentDoB = []
StudentID = []
Course = []
CourseID = []
CourseName = []
Mark = []

class Std:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        Student.append(self)
        StudentID.append(self.__id)

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob


class Cse:
    def __init__(self, cid, cname):
        self._cid = cid
        self._cname = cname

        Course.append(self)
        CourseID.append(self._cid)

    def get_id(self):
        return self._cid

    def get_name(self):
        return self.cname


class Markstd:
    def __init__(self, markid, nid, mark):
        self._markid = markid
        self._nid = nid
        self._mark = mark
        Mark.append(self)

    def get_mid(self):
        return self.mid

    def get_nid(self):
        return self.nid

    def get_mark(self):
        return self.mark

    def get_gpa(self):
        return self.gpa

def Nos():
    student = int(input("Enter students in class: "))
    if student < 0 or student == 0:
        print("Student invalid")
        return student
    else:
        return 0


def Adds():
    print("STUDENT INFO")
    name = input("Enter Student's name: ")
    id = input("Enter Student's ID: ")
    dob = input("Enter Student's DoB: ")
    std = {
        'id': id,
        'name': name,
        'dob': dob
    }
    Student.append(std)
    StudentID.append(id)


def Noc():
    course = int(input("Enter total number of course: "))
    if course < 0 or course == 0:
        print("Course invalid")
        return 0
    else:
        return course


# Add course
def Addc():
    print("COURSE")
    name = input("Enter Course's name: ")
    id = input("Enter Course's ID: ")
    cc = input("Enter Course's Credit:")
    cse = {
        'id': id,
        'name': name,
        'cc': cc
    }
    Course.append(cse)
    CourseID.append(cid)


# Create mark for students
def Markstd():
    rint("MARK OF STUDENT")
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
    print("STUDENT LIST")
    for i in range(0, len(Student)):
        print(f"name:{Student[i]['name']}")
        print(f"ID:{Student[i]['id']}")
        print(f"DoB:{Student[i]['dob']}")


def Course_list():
    print("COURSE LIST")
    for i in range(0, len(Course)):
        print(f"name : {Course[i]['name']}")
        print(f"ID:{Course[i]['id']} ")


def Mark_list():
    print("MARK LIST")
    for i in range(0, len(Mark)):
        print(f"ID-Student: {Mark[i]['a']}")
        print(f"ID-course: {Mark[i]['b']}")
        print(f" mark:{Mark[i]['mark']}")


Nos()
Adds()
Noc()
Addc()
Student_list()
Course_list()
Mark_list()