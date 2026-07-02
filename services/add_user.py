
def add_user():
    print("Add New User!")
    print("1. Add Employee")
    print("2. Add Customer")
    
    try:
        option = int(input("Choose an Option: "))

        if option == 1:
            print("\nAdd New Employee\n")
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            phone = str(input("Enter Phone Number: "))
            email = str(input("Enter Email Address: "))
            role = input("Enter Empoyee Role ['Manager', 'Cashier']: ")
            salary = input("Enter Salary")
            hire_date = input("Enter Hire Date in the format [YYYY-MM-DD]: ")
            password = str(input("Enter password: "))
    except ValueError as e:
        print(f"\nInvalid input! An error occured: {e}")