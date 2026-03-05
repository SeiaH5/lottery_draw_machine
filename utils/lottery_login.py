users = {
    "josiah": "12345"
}

def front_panel():
    while True:
        print("\n\033[1mWELCOME TO \033[36mLOTTERY DRAW MACHINE\033[0m")
        print(f"""{"="*20}
[1] log-in
[2] register

[0] exit
{"="*20}\n""")
        user_panel = input("Select: ")
        print("\n"*30)
        if user_panel == "1":
            status = user_login()
            if status == "success":
                print(f"\n\033[1m\033[32mLogin successful!\033[0m{"\n"*3}")
                break
            else:
                continue
        elif user_panel == "2":
            user_register()
        elif user_panel == "0":
            exit()
        else:
            print("Please select valid option.\n")

def user_login():
    print(f"{"="*15}\nLOGIN\n{"="*15}\n")
    print("[0] Go Back\n")
    while True:
        name = input("Username: ")
        if name == "0":
            print(f"{"\n"*30}")
            return
        password = input("Password: ")
        if password == "0":
            print(f"{"\n"*30}")
            return
        if name in users and users[name] == password:
            return "success"
        else:
            print("\033[31mInvalid username or password.\033[0m\n")

def user_register():
    print(f"{"="*15}\nREGISTER\n{"="*15}\n")
    print("[0] Go Back\n")
    while True:
        name = input("Create username: ")
        if name == "0":
            print(f"{"\n"*30}")
            return
        if name in users:
            print("Username already exists.\n")
        else:
            break
    password = input("Create password: ")
    if password == "0":
        print(f"{"\n"*30}")
        return
    while True:
        enter_password = input("Re-enter password: ")
        if enter_password == "0":
            print(f"{"\n"*30}")
            return
        if enter_password == password:
            break
        else:
            print("\033[31mPasswords do not match.\033[0m")
    users[name] = password
    print("\n\033[1m\033[32mRegistration successful!\033[0m")
    print(f"{"\n"*3}")
