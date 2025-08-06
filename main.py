def add_pass(user, password):
    with open('passes.txt', 'a') as file:
        file.write(f"{user} => {password}\n")

def view_passwords():
    try:
        with open('passes.txt', 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("No password file found.")

while True:
    mode = input("Choose a mode: [a] Add password, [v] View passwords, [q] Quit: ").strip().lower()

    if mode == "a":
        user = input("Enter the username: ").strip()
        password = input("Enter the password: ").strip()
        if not user or not password:
            print("Username and password cannot be empty!")
            continue
        add_pass(user, password)

    elif mode == "v":
        view_passwords()

    elif mode == "q":
        print("see you round")
        break

    else:
        print("invalid mode")
