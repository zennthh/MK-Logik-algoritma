def login_web():
    data = {
        "user": {"123", "222"},
        "admin": {"321", "333"} 
    }

    while True:
        login_user = input("Ingin login sebagai apa:").lower()
        if login_user in ["user", "admin"]:
            print()
            print (f"==== Anda akan di tanyakan user id dan password sebagai: {login_user} ====")
            break
        else:
            print ("Masukan user id yang benar")

    if login_user == "user":
        while True:
            id = input(f"Masukan id yang benar sebagai {login_user}: ")
            if id in ["123"]:
                break
            else:
                print ("id tidak valid, Masukan id yang benar")

        while True:
            password = input(f"Masukan password yang benar sebagai {login_user}: ")
            if password in ["222"]:
                break
            else:
                print ("Password tidak valid, Masukan password yang benar")
        print(f"Selamat login anda sebagai {login_user} berhasil.")
    
    elif login_user == "admin":
        while True:
            id_staff = input(f"Masukan id yang benar sebagai {login_user}: ")
            if id_staff in ["321"]:
                break
            else:
                print ("id tidak valid, Masukan id yang benar")

        while True:
            password_staff = input(f"Masukan password yang benar sebagai {login_user}: ")
            if password_staff in ["333"]:
                break
            else:
                print ("Password tidak valid, Masukan password yang benar")
        print(f"Selamat login anda sebagai {login_user} berhasil.")
login_web()