from students import add_student,view_student,update_student,delete_student,search_student

def menu():
    while True:
        print("student DB ")
        print("1. Add Student")
        print("2. view student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")

        your_choice=input("Enter your Choice:")
        
        if your_choice == "1":
            std_name= input("Enter name:")
            std_age=input("Enter age:")
            gender=input("Enter Gender:")
            phone=input("Enter Phone number:")
            add_student( std_name,std_age,gender,phone)
            print("Student data added successfully")
        elif your_choice == "2":
            view_student()
        elif your_choice == "3":
            std_id=int(input("Enter student id to update:"))
            
            std_name= input("Enter name:")
            std_age=input("Enter age:")
            gender=input("Enter Gender:")
            phone=input("Enter Phone number:")

            fields_to_update={
                "std_name": std_name,
                "std_age": std_age,
                "gender": gender,
                "phone": phone
            }
            update_student(std_id,**fields_to_update)

        elif your_choice == "4":
            std_id=int(input("Enter student id to delete:"))
            delete_student(std_id)
        elif your_choice == "5":
            keyword = input("Enter name or phone number to search:")
            search_student(keyword)
        elif your_choice == "6":
            break
        else:
            print("❌ Invalid choice! Please try again.")       


            
if __name__ == "__main__":
    menu()
            