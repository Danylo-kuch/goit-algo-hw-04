def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} was succesfully added!"

def change_contacts_phone(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Your phone number was succesfully changed"
    else:
        return f"The name {name} was not found"
    
def show_contacts_phone(args, contacts):
    name = args[0]
    if name in contacts:
       return f"Here is the phone number from {name}: {contacts[name]}" 
    else:
        return f"the name {name} was not found"
    
def show_all_contacts():
    with open("goit-algo-hw-04\\Bot\\contacts.txt", "r") as f:
        lines = f.readlines()
        if not lines:
            print("No contacts found.")
        else:
            print("All contacts:")
            for line in lines:
                print(line.strip())

def save_contacts(contacts):
    with open("goit-algo-hw-04\\Bot\\contacts.txt", "w") as f:
        for name, phone in contacts.items():
            f.write(f"{name}: {phone}\n")


def main():
    contacts = {}
    print("Welcome to the assistant BOT created by Danylo Kucherenko!")
    while True:
        user_input = input("Enter the command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Okay. Good bye!")
            break

        elif command == "hello":
            print("Hi! How can I help you?")

        elif command == "add":
            if len(args) != 2:
                print("Usage: add <name> <phone>")
                continue
            firstly = add_contact(args, contacts)
            save_contacts(contacts)
            print(firstly)

        elif command == "change":
            if len(args) != 2:
                print("Usage: change <name> <new_phone>")
                continue
            changed = change_contacts_phone(args, contacts)
            save_contacts(contacts)
            print(changed)

        elif command == "phone":
            if len(args) != 1:
                print("Usage: phone <name>")
                continue
            phone = show_contacts_phone(args, contacts)
            print(phone)
        
        elif command == "all":
            show_all_contacts()


        else:
            print("Invalid command")

if __name__ == "__main__":
    main()