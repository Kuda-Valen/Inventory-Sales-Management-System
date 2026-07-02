from datetime import datetime
from models.person import Person
from services.login import authenticate
from services.add_user import add_user

def main_menu():
    while True:
        print("\nInventory & Sales Management System\n")
        print("1. Log in")
        print("2. Add New User")
        print("3. Exit")
        
        try:
            option = int(input("\nChoose an option: "))

            if option == 1:
                authenticate()
            
            elif option == 2:
                add_user()
            
            elif option == 3:
                print("\nExiting! Bye....")
                return
            
            else:
                print("\nInvalid Option. Choose a better option.")
        
        except ValueError as e:
            print(f"Invalid input! Error that occured: {e}")