def validate_args(expected_arg_count, command_example):
    def decorator(func):
        def wrapper(*args):
            if len(args[0]) != expected_arg_count:
                return f"Invalid command format. Please use '{command_example}'."
            return func(*args)
        return wrapper
    return decorator

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, ' '.join(*args)

@validate_args(2, 'add [name] [phone]')
def add_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    else:
        return("Invalid command format. Please use 'add [name] [phone]'.")

@validate_args(2, 'change [name] [phone]')
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

@validate_args(1, 'phone [name]')
def show_phone(args, contacts):
    name = args[0]

    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = user_input.split()
        command = command.strip().lower()

        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            print(add_contact(args, contacts))
        elif command.startswith("change"):
            print(change_contact(args, contacts))
        elif command.startswith("phone"):
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command in ["close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
