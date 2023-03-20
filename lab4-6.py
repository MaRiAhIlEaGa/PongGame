############################################ domain ################################################################

def get_real_part():
    return complex_number["real_part"]


def set_real_part():
    complex_number["real_part"] = real_part


def get_imaginary_part():
    return complex_number["imaginary_part"]


def set_imaginary_part():
    complex_number["imaginary_part"] = imaginary_part


def create_number_complex(real_part, imaginary_part):
    return {"real_part": real_part, "imaginary_part": imaginary_part}


################################################### Operations ########################################################


def add_element_in_list(all_complex_numbers, real_part, imaginary_part):
    complex_number = create_number_complex(real_part, imaginary_part)
    all_complex_numbers.append(complex_number)


def add_complex_number_specified_position(all_complex_numbers, real_part, imaginary_part, position):
    complex_number = create_number_complex(real_part, imaginary_part)
    all_complex_numbers[position] = complex_number


def delete_number_specified_position(all_complex_numbers, position):
    all_complex_numbers.remove(all_complex_numbers[position])


def delete_sequence(all_complex_numbers, start_position, final_position):
    del all_complex_numbers[start_position:final_position]


####################################################### ui ###########################################################
def print_options():
    print("1. Adauga element in lista\n"
          "2. Adauga element in lista pe o pozitie specificata\n"
          "3. Stergere element de pe o pozitie data\n"
          "4. Stergere elemente de pe un interval de pozitii\n"
          "5. Print all elements\n"
          "x. Exit")


def ui_add_complex_numbers(all_complex_numbers):
    real_part = int(input("Introduceti partea reala: "))
    imaginary_part = int(input("Introduceti partea imaginara: "))
    add_element_in_list(all_complex_numbers, real_part, imaginary_part)


def ui_add_complex_number_specified_position(all_complex_numbers):
    real_part = int(input("Introduceti partea reala: "))
    imaginary_part = int(input("Introduceti partea imaginara: "))
    position = int(input(("Introduceti pozitia pe care doriti sa fie introdus elementul complex: ")))
    add_complex_number_specified_position(all_complex_numbers, real_part, imaginary_part, position)


def ui_delete_number_specified_position(all_complex_numbers):
    position = int(input(("Introduceti pozitia de pe care doriti sa stergeti elementul: ")))
    delete_number_specified_position(all_complex_numbers, position)


def ui_delete_sequence(all_complex_numbers):
    start_position = int(input(("Introduceti pozitia de la care doriti sa incepeti stergerea: ")))
    final_position = int(input(("Introduceti pozitia pana la care doriti sa stergeti elemente: ")))
    delete_sequence(all_complex_numbers, start_position, final_position)


def ui_print_all_element(all_complex_numbers):
    print(all_complex_numbers)


def run_menu():
    options = {1: ui_add_complex_numbers,
               2: ui_add_complex_number_specified_position,
               3: ui_delete_number_specified_position,
               4: ui_delete_sequence,
               5: ui_print_all_element}
    all_complex_numbers = []
    while True:
        print_options()
        opt = input("Optiunea : ")
        if opt == "x":
            break
        opt = int(opt)
        options[opt](all_complex_numbers)


if __name__ == "__main__":
    run_menu()
