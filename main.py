from datetime import datetime
from models.person import Person
from services.login import authenticate
from services.add_user import add_user
from services.add_product import add_product

def main_menu():
    while True:
        print("\nInventory & Sales Management System\n")
        print("1. Log in")
        print("2. Add New User")
        print("3. Exit")
        
        try:
            option = int(input("\nChoose an option: "))

            if option == 1:
                employee = authenticate()
                if employee.role == "Manager":
                    print(f"\n--Welcome Back {employee.first_name} --\n")
                    manager_menu()
                
                else:
                    print(f"\n-- Welcome Back {employee.first_name} --\n")
                    cashier_menu()

            
            elif option == 2:
                add_user()
            
            elif option == 3:
                print("\nExiting! Bye....")
                return
            
            else:
                print("\nInvalid Option. Choose a better option.")
        
        except ValueError as e:
            print(f"Invalid input! Error that occured: {e}")

def manager_menu():
    while True:
        print("\n1. Add Product")
        print("2. Edit Product")
        print("3. Remove Product")
        print("4. View Products")
        print("5. View Sales")
        print("6. Return to Main Menu")

        try:
            option = int(input("\nChoose an Option: "))

            if option == 1:
                add_product()
            
            elif option == 2:
                print("Edit product coming soon!")
            
            elif option == 3:
                print("Remove product coming soon!")
            
            elif option == 4:
                print("View products coming soon!")

            elif option == 5:
                print("Past Sales coming soon!")
            
            elif option == 6:
                print("Back to Main Menu.")
                return 

            else:
                print("\nInvalid option. Select a Valid Option:..")

        except ValueError as e:
            print(f"\nAn Input Error occured: {e}")


def cashier_menu():
    while True:
        print("1. View Products")
        print("2. Make a Purchase")
        print("3. Return to Main menu")
    
        try:
            option = int(input("\nChoose an option: "))

            if option == 1:
                print("View Products coming soon!")
            
            elif option == 2:
                print("Make Purchase feature coming soon!")
            
            elif option == 3:
                print("Return to Main Menu..")
                return
            
            else:
                print("\nInvalid Input. Choose valid input:..")
        except ValueError as e:
            print(f"\nAn Input Error occured: {e}")

main_menu()