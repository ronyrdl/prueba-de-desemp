from errores import *
students = []
"""
here in this functions the user can agree new student with validation inputs 
for example age in number not letters etc
"""
def agg_students (students):
    id= errores("enter id of student: ",int)
    while id < 0:
        print("Price cannot be negative")
        id= errores("Enter the id: ", int)
    name= errores("enter the name of students: ")
    age= errores("enter the age of students: ",int)
    while age < 0:
        print("Price cannot be negative")
        age= errores("Enter the age: ", int)
    course=errores("enter the course: ",int)
    while course< 0:
                print("Price cannot be negative")
                course= errores("Enter the course: ", int)
    valid = False
    while valid == False:
          status= errores("the students is active? yes/no: ")
          if status=="yes":
              print("ok the student is active")
              status="active"
              valid=True
          elif status=="no":
              print("ok, the student is not active")
              status="inactive"
              valid= True
          else:
               print("its incorrect input, please enter yes or no")

    
     
    student= {
        "id":id,
        "name":name,
        "age":age,
        "course":course,
        "status":status
     }
    students.append(student)
    print (f"student {name} add successly!!!!!")
    """
    here in show students the program when the user registrer first in option one, if not register, dont
    show the list
    """
def show_students(students):
    if len(students)==0:
        print("you don't registrer the student please, registrer in option 1")
        return
    for student in students: 
         print("--- student list---")   
         print(f"Student_id: {student['id']}\n name: {student['name']}\n age: {student['age']}\n course {student['course']}\n status: {student['status']}\n")
         print("-------------------")

"""
in seach, the user can seach a student with your id, if the student 
exits the user can see the information from this student
"""
def search_product(students):
    if len(students) == 0:
        print("you don't registrer the student please, register in option 1")
        return

    id = errores("Enter id of the student to search: ",int)

    
    for student in students:
        if student["id"] == id:
            print("Student found: ")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Course: {student['course']}")
            print(f"Status: {student['status']}")
            return

    print("Student not found")

"""
in update, the user can seach a student with your id, and also change 
the information for this user, for example the name, course, etc
"""

def update_students(students):
    if len(students)==0:
        print("you don't registrer the student please, registrer in option 1")
        return
    id=errores("please enter the id of the student: ",int)
    exist = False
      
    for student in students:
        if student["id"] == id:
            exist = True
            new_name= errores("enter the new name: ")
            new_age = errores ("enter the new age: ",int)
            while new_age < 0:
                print("Price cannot be negative")
                new_age= errores("Enter the age: ", int)
            new_course=errores("enter the new course: ",int)
            while new_course< 0:
                print("Price cannot be negative")
                new_course= errores("Enter the course: ", int)
            valid = False
            while valid == False:
                new_status= errores("the students is active? yes/no: ")
                if new_status=="yes":
                    print("ok the student is active")
                    new_status="active"
                    valid=True
                elif new_status=="no":
                    print("ok, the student is not active")
                    new_status="inactive"
                valid= True
            else:
               print("its incorrect input, please enter yes or no")

            student["name"] = new_name
            student["age"] = new_age
            student["course"] = new_course
            student["status"] = new_status
            print("Product updated student successfully")
    if not exist:
        print("Student not found")


"""
in delet, the user can seach a student with your id, if the student 
exits the user can remove all information from this student
"""
    
def delete_student(students):
    if len(students)==0:
        print("you don't registrer the student please, registrer in option 1")
        return
    id=errores("please enter the id of the student: ",int)
    exist = False
    
    for student in students:
        if student["id"]== id:
            students.remove(student)
            exist = True
            print("Student deleted successfully")
            break

    if not exist:
        print("Student not found")
    
"""
here, the user can save the information for students in a archive 
.csv or overwrite and add a new student
"""

def save_csv(students, path="students.csv"):
    if len(students) == 0:
         print("you don't registrer the student please, registrer in option 1")
         return

    try:
        with open(path, "w", encoding="utf-8") as file:
                file.write("id,name,age,course,status\n")
                for student in students:
                    line = f"{student['id']},{student['name']},{student['age']},{student['course']},{student['status']}\n"
                    file.write(line)

        print(f"The student uptdate in {path}")

    except Exception as e:
        print(f"Error saving file{e}")
"""
here, the user can load archive if the archive exist in the program and
see the information of students in show students
"""

def load_csv(students, path="students.csv"):
   
    try:
        with open(path, "r", encoding="utf-8") as file:
            next(file)  
            for line in file:
                line = line.strip() 
                if not line:
                    continue

                id, name,age,course,status = line.split(",")
                exists = False
                for student in students:
                    if (student["id"] == id and
                        student["name"] == name and
                        student ["age"]==age and
                        student["course"]==course and
                        student ["status"]==status):
                        exists = True
                        break
                if not exists:
                 students.append({
                        "id":id,
                        "name": name,
                        "age":age,
                        "course":course,
                        "status":status
                    })

        print(f"Inventory loaded from: {path}")

    except FileNotFoundError:
        print(f"No file found at {path}, starting with empty students.")

    except Exception as e:
        print(f"Error loading CSV: {e}")


        


        
         