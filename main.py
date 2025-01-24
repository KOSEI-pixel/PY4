def add_birthday(birthdays, name, date):
    birthdays[name] = date

def get_birthday(birthdays, name):
    return birthdays.get(name, "Birthday not found")

def main():
    birthdays = {}
    
    while True:
        print("\nOptions:")
        print("1. Add a birthday")
        print("2. Get a birthday")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter the name: ")
            date = input("Enter the birthday (YYYY-MM-DD): ")
            add_birthday(birthdays, name, date)
            print(f"Birthday for {name} added.")
        
        elif choice == '2':
            name = input("Enter the name: ")
            print(f"{name}'s birthday is {get_birthday(birthdays, name)}")
        
        elif choice == '3':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()