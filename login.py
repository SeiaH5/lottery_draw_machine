username = {
    "josiah": "12345"
}

def front_panel():
    while True:
        print("""-----
[1]log-in
[2]register

[0]exit
-----   """)
        user_panel = int(input(""))
        if user_panel == 1:
            user_login()
            break
        elif user_panel == 2:
            user_register()
            break
        elif user_panel == 0:
            continue 
        else:
            print("Please select valid option.")

def user_login():
    username = [1, 2, 3]
    print("login")
    
def user_register():
    print("register")