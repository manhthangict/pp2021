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


class Marks:
    def __init__(self, mid, nid, mark):
        self._mid = mid
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

def student_num():
    student = int(input("Enter students in class: "))
    return student


# Add student

def add_student():
    print("STUDENT INFO")
    name = input("Enter Student's name: ")
    id = input("Enter Student's ID: ")
    dob = input("Enter Student's DoB: ")
    st_u = {
        'id': id,
        'name': name,
        'dob': dob
    }
    Student.append(st_u)
    StudentID.append(id)


# Add number of course
def course_num():
    course = int(input("Enter total number of course: "))
    return


# Add course
def add_course():
    print("COURSE")
    cname = input("Enter Course's name: ")
    cid = input("Enter Course's ID: ")
    cc = input("Enter Course's Credit:")
    cr_o = {
        'cid': cid,
        'cname': cname,
        'cc': cc
    }
    Course.append(cr_o)
    CourseID.append(cid)


# Create mark for students
def create_mark():
    g = 1
    tu = len(Student)
    while g <= tu:
        g += 1
        mid = input("Enter the Student ID: ")
        if mid in Student:
            for i in range(0, len(CourseID)):
                nid = input("Enter the Course ID: ")
                if nid in CourseID:
                    mark = float(input("Enter Student Mark: "))
                    kk = {
                        'mid': mid,
                        'nid': nid,
                        'mark': mark
                    }
                else:
                    print("Student ID NOT FOUND !!")
                    break
                Mark.append(kk)
        else:
            print("Course ID NOT FOUND !!")
            break


def show_list_student():
    print("STUDENT LIST")
    for i in range(0, len(Student)):
        print(f"name:{Student[i]['name']}")
        print(f"ID:{Student[i]['id']}")
        print(f"DoB:{Student[i]['dob']}")


def show_list_course():
    print("COURSE LIST")
    for i in range(0, len(Course)):
        print(f"name : {Course[i]['name']}")
        print(f"ID:{Course[i]['id']} ")


def show_mark():
    print("MARK LIST")
    for i in range(0, len(Mark)):
        print(f"ID-Student: {Mark[i]['a']}")
        print(f"ID-course: {Mark[i]['b']}")
        print(f" mark:{Mark[i]['mark']}")
