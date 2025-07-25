def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def load_contacts():
    contacts = {}
    path = "goit-algo-hw-04\\Bot\\contacts.txt"
    try:
        with open(path, "r") as f:
            for line in f:
                if ":" in line:
                    name, phone = line.strip().split(":", 1)
                    contacts[name.strip()] = phone.strip()
    except FileNotFoundError:
        return contacts
    return contacts

def add_contact(args, contacts):
    if len(args) != 2:
        return "Usage: add <name> <phone>"
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} was successfully added!"

def change_contacts_phone(args, contacts):
    if len(args) != 2:
                return "Usage: change <name> <new_phone>"
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Your phone number was succesfully changed"
    else:
        return f"The name {name} was not found"
    
def show_contacts_phone(args, contacts):
    if len(args) != 1:
                return "Usage: phone <name>"
    name = args[0]
    if name in contacts:
       return f"Here is the phone number from {name}: {contacts[name]}" 
    else:
        return f"the name {name} was not found"
    
def show_all_contacts():
    with open("goit-algo-hw-04\\Bot\\contacts.txt", "r") as f:
        lines = f.readlines()
        if not lines:
            return "No contacts found."
        else:
            result = "All contacts:\n"
            result += "\n".join(line.strip() for line in lines)
            return result

def save_contacts(contacts):
    with open("goit-algo-hw-04\\Bot\\contacts.txt", "w") as f:
        for name, phone in contacts.items():
            f.write(f"{name}: {phone}\n")


def main():
    contacts = load_contacts()
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
            firstly = add_contact(args, contacts)
            save_contacts(contacts)
            print(firstly)

        elif command == "change":
            changed = change_contacts_phone(args, contacts)
            save_contacts(contacts)
            print(changed)

        elif command == "phone":
            phone = show_contacts_phone(args, contacts)
            print(phone)
        
        elif command == "all":
            result = show_all_contacts()
            print(result)


        else:
            print("Invalid command")

if __name__ == "__main__":
    main()