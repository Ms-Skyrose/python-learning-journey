import os
import json


file_name = "Practice Student database.json"
def load_data():
    if os.path.exists(file_name):
        try:
            with open(file_name, "r") as x:
               students = json.load(x)
               return students if isinstance(students, dict) else {}
        except:
            return {}
    else:
        return {}   
    
    
def save_data(student):
    with open(file_name, "w") as x:
        json.dump(student, x, indent = 4)


def add_data(*, name, age, student_class = "primary one"):
    students = load_data()

    student_ID =  str(len(students) + 1)

    students[student_ID] = {
        "name": name,
        "age": age,
        "student_class": student_class
    }
    save_data(students)


def del_data():
    students = load_data()
    print(students)


    if not students:
        print("The database is empty")

    for student_ID, student in students.items():
        print(f"{student_ID}. {student['name']} {student['age']}")
    
    choice = input("Enter the number of the student you want to delete")
    if choice in students:
        del students[choice]
        save_data(students)   
        print(f"Student with ID {choice} has been deleted") 
    else:
        print(f"Invalid selected Student ID")
        

        

def main():
    while True:
       print("\nManage your record here")
       print("1. See student databse") 
       print("2. Add your details")
       print("3. Delete your details")
       print("4. Exit")
       print("Pls click 'Escape' key to exit at any moment")
       choice = int(input("choose an option"))
       
       if choice == 1:
           print(load_data())

           print()
           input("Press Enter to continue.....")
       elif choice == 2:
            name = input("Enter your name")
            age = input("Enter your age")
            student_class = input("Enter your class")

            add_data(name = name, age = age, student_class = student_class)
       elif choice == 3:
            del_data()
       elif choice == 4:
            print("Thanks for using this database system")
            break
       else:
            print("Please enter a valid number between a number 1 and 4. Thanks!")

if __name__ == "__main__":
    main()

           




           