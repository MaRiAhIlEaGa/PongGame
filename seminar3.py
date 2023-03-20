# Aplicatie pentru gestiunea studentilor dintr-o facultate
# Fiecare student are un id unic, un nume si nota
# Studentii vor fi retinuti intr-o lista

# Meniu
def print_options():
    print("1. Add student\n"
          "2. Print all students\n"
          "x. Exit")

###################################Operations##########################################################
def add_student(all_students, id, name, grade):
    # todo: de verificat id unic
    student = create_student(id, name, grade)
    all_students.append(student)


def ui_add_student(all_students):
    id = int(input("Id = "))
    name = input("Name = ")
    grade = int(input("Grade = "))
    add_student(all_students, id, name, grade)


def print_all_students(all_students):
    print(all_students)


def run_menu():
    options = {1: ui_add_student,
               2: print_all_students
               }
    all_students = []
    while True:
        print_options()
        opt = input("Option = ")
        if opt == "x":
            break
        opt = int(opt)
        options[opt](all_students)


def get_id(student):
    return student["id"]


def set_id(student, id):
    student["id"] = id


def get_name(student):
    return student["name"]


def set_name(student, name):
    student["name"] = name


def get_grade(student):
    return student["grade"]


def set_grade(student, grade):
    student["grade"] = grade


# F2: Add students
def create_student(id, name, grade):
    return {"id": id,
            "name": "name",
            "grade": grade
            }

######################################### tests ########################################

def test_add_student():
    #student[id] = 1
    #student[name] = s1
    #student[grade] = 10
    all_students = []
    add_student(all_students, 1, "s1", 10)
    assert (len(all_students) == 1)
    assert (get_id(all_students[0]) == 1)
    assert (get_name(all_students[0]) == "s1")
    assert (get_grade(all_students[0]) == 10)

test_add_student()
run_menu()
