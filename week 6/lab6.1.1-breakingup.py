#student management

students = []
def display_menu():
    print("menu")
    print("\t(a) add")
    print("\t(v) view")
    print("\t(q) quit")
    choice = input("Please select (a/v/q) : ")
    return choice

def get_modules():
    modules = []
    module_name = input("Please enter the module name (blank to quit)")
    while (module_name != ""):
        module = {}
        module["name"] = module_name
        module["grade"] = int(input("enter grade"))
        modules.append(module)

        module_name = input("Please enter the module name (blank to quit)")
    return modules

def do_add(students):
    student ={}
    student["name"] = input("Please enter name: ")
    student["modules"] = get_modules()
    students.append(student)

def do_view(students):
    for student in students:
        print(student["name"])
        for module in student["modules"]:
            print ("\t", module["name"], "\t:", module["grade"])

choice = display_menu()
while choice != "q":
    if choice == "a":
        do_add(students)
    elif choice == "v":
        do_view(students)
    else:
        print("invalid choice")

    choice = display_menu()

print("Goodbye")