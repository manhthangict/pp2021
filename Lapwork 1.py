# create list of courses and list of students
stN: int = int(input("Number of students in list: "))
while stN < 0:
    print("Re-entered: ")
    studentA = int(input("Number of students in list: "))

coursesN = int(input("Enter number of courses: "))
while coursesN < 0:
    print("Re-entered: ")
    numberOC = int(input("Enter number of courses: "))
cName = []
cID = []
stName = []
stID = []
stDoB = []
stInformation = {}
print("")

# choose option to get information
def Option():
    print("1. Input information of student ")
    print("2. Input information of course ")
    print("3. Input mark ")
    print("4. Information of student ")
    print("5. Information of course ")
    print("6. Quit ")
    print("")
Option()
choose = int(input("Enter your choice: "))
print("")
while choose != 0:
    break_point = False

    if choose == 1:
        for i in range(0, stN):
            print("Information of student %d " % (i + 1))
            a = str(input("Student Name: "))
            b = str(input("Student ID: "))
            c = int(input("Student DoB: "))
            stName.append(a)
            stID.append(b)
            stDoB.append(c)
        print("DONE!!!")
        print("")
        Option()
        choose = int(input("Enter another choice: "))
        if 0 < choose and choose > 5:
            print("The End")
            break
    elif choose == 2:
        for i in range(0, coursesN):
            print("The order of course in courses: %d " % (i + 1))
            a = str(input("Enter course name: "))
            b = str(input("Enter course ID: "))
            cName.append(a)
            cID.append(b)
        print("DONE!!!")
        print("")
        Option()
        choose = int(input("Enter another choice: "))
        if 0 < choose and choose > 5:
            print("The End")
            break
    elif choose == 3:
        ID = str(input("Enter ID of student: "))
        st_cour_mang = {}
        check_stop = False
        for i in range(0, len(stID)):
            if stID[i] == ID:
                check_stop = True
                stcourse = int(input("How many course " + stID[i] + " is learning: "))
                while stcourse > len(cName) or stcourse < len(cName):
                    print("Re-entered: ")
                    stcourse = int(input("How many course " + stID[i] + " is learning: "))
                for j in range(0, stcourse):
                    name_course_curr = str(input("Enter course name: "))
                    for k in range(0, len(cName)):
                        if name_course_curr == cName[k]:
                            mark = int(input("Enter mark of " + name_course_curr + ": "))
                            st_cour_mang[name_course_curr] = mark
                            stInformation[ID] = st_cour_mang
                            check_stop = True
                    if not check_stop:
                        print("                Course name does not exist! ")
                        exit(128)
        if not check_stop:
            print("                Student ID does not exist! ")
            exit(100)
        Option()
        choose = int(input("Enter another choice: "))
        if 0 < choose and choose > 5:
            print("The End")
            break
    elif choose == 4:
        for i in range(0, len(stName)):
            print("Information of student %d " % (i + 1))
            print("Name: " + stName[i])
            print("ID: " + stID[i])
            print("DoB: " + str(stDoB[i]))
            print()
        choose = int(input("Enter your choice: "))
    elif choose == 5:
        for i in range(0, len(cName)):
            print("The order of course: %d " % (i + 1))
            print("Course name: " + cName[i])
            print("Course ID: " + cID[i])
        choose = int(input("Enter your choice: "))
    elif choose == 6:
        break
