from functions import*
def menu():
    print("\n--- MENU ---")
    print("1. Add student")
    print("2. Show students")
    print("3. seach student")
    print("4. update student")
    print ("5. delete student")
    print ("6. save in csv")
    print ("7. load")


   

    try:
        # Convert user input to integer
        return int(input("Choose an option: "))
    except ValueError:
        # Handle invalid input
        print("Invalid input")
        return 0


# Control variable for main loop
valid = 0

# Main program loop
while valid == 0:
    option = menu()

    # Call functions based on user option
    if option == 1:
        agg_students(students)

    elif option == 2:
        show_students(students)
    elif option == 3:
        search_product(students)
    elif option == 4:
        update_students(students)

    elif option == 5:
        delete_student(students)
    elif option == 6:
        save_csv(students)
    elif option == 7:
        load_csv(students)
        
    elif option == 9:
        # Exit program
        print("Goodbye")
        valid = 1


    else:
        # Handle invalid menu option
        print("Invalid option")