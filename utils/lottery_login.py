import lottery_database

current_user=None

def front_panel():
    while True:
        print("\n\033[1mWELCOME TO \033[36mLOTTERY DRAW MACHINE\033[0m")
        print(f"""{"="*20}
[1] log-in
[2] register

[0] exit
{"="*20}\n""")
        user_panel=input("Select: ")
        print("\n"*30)
        if user_panel=="1":
            status=user_login()
            if status=="success":
                print(f"\n\033[1m\033[32mLogin successful!\033[0m{"\n"*3}")
                break
        elif user_panel=="2":
            user_register()
        elif user_panel=="0":
            exit()
        else:
            print("Please select valid option.\n")

def user_login():
    global current_user
    print(f"{"="*15}\nLOGIN\n{"="*15}\n")
    print("[0] Go Back\n")
    while True:
        name=input("Username: ")
        if name=="0":
            print("\n"*30)
            return
        password=input("Password: ")
        if password=="0":
            print("\n"*30)
            return
        user=lottery_database.login_user(name,password)
        if user:
            current_user=name
            return "success"
        else:
            print("\033[31mInvalid username or password.\033[0m\n")

def user_register():
    print(f"{"="*15}\nREGISTER\n{"="*15}\n")
    print("[0] Go Back\n")
    while True:
        name=input("Create username: ")
        if name=="0":
            print("\n"*30)
            return
        password=input("Create password: ")
        if password=="0":
            print("\n"*30)
            return
        success=lottery_database.register_user(name,password)
        if success:
            print("\n\033[1m\033[32mRegistration successful!\033[0m")
            print("\n"*3)
            return
        else:
            print("Username already exists.\n")