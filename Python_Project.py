# Vacation Booking


admin_username = "Micha"
admin_password = "507250"

vb_lib = {#DONE
    
    '1.': {'loc': 'Boracay, Malay', 'p': '2,500', 'd':'Guesthouse: 2  guests, 1 bedroom - Sea View'},
    '2.': {'loc': 'Boracay, Malay', 'p': '3,816', 'd':'Guesthouse: 6  guests, 1 bedroom - Beachfront'},
    '3.': {'loc': 'Boracay, Malay', 'p': '4,421', 'd':'Guesthouse: 2  guests, 1 bedroom - Beachfront'},
    '4.': {'loc': 'El Nido', 'p': '2,500', 'd':'Guesthouse: 2  guests, 1 bedroom - Beachfront'},
    '5.': {'loc': 'Mabini', 'p': '3,496', 'd':'Guesthouse: 4  guests, 1 bedroom  - Beachfront'},
    '6.': {'loc': 'Lian', 'p': '13,500', 'd':'Guesthouse: 8  guests, 2 bedroom - Beachfront'}

}

users_list = { #DONE

}

def view_vb():  #DONE
    for name, det in vb_lib.items():
        print (" "f"{name}""\n Location: "f"{det['loc']}""\n Price: Php "f"{det['p']}"".00""\n "f"{det['d']}") 
        print ()
        
def avail_vb(): #DONE sorta
        print ("   Available Vacation Locations in the Philippines")
        print ("-"*55)
        view_vb()

def register_user(): #MAIN4
    print ("\t\t          Sign Up")
    print ("-"*55)

    while True:
        try:
            username = input("Enter Username: ")
            
            if not username:
                main_menu()

            if username in users_list:
                print("\nThis username already exists. Please enter  a new username.\n")
                continue
            while True:
                try: 
                    password = input("Enter Password: ")
                    if len(password) < 6:
                        print("\nPassword is to short....")
                        continue
                    if len(password) >= 6:
                        users_list[username] = {"password" : password}  
                        print("\nUser signed up successfully."f"\nWelcome to you, {username}!!!")
                        main_menu()
                    else:
                        print("\nInvalid input.\n")
                        continue 
                except ValueError:
                    register_user()
        except ValueError:
            register_user()
            
def admin_login(): #MAIN2
    print ("\t\t      Admin Login")
    print ("-"*55)

    ad_un_ip = input ("Enter Admin Username: ")
    ad_pw_ip = input ("Enter Admin Password: ")

    if ad_un_ip == admin_username and ad_pw_ip == admin_password:
        print ("\nAdmin Logged In Successfully!!!")
        print ("-"*55)
        admin_login_menu()
    
    elif ad_un_ip != admin_username and ad_pw_ip == admin_password:
        print ("\nUsername is incorrect, please try again....")
        print ("-"*55)
        admin_login()
    
    elif ad_un_ip == admin_username and ad_pw_ip != admin_password:
        print ("\nPassword is incorrect, please try again....")
        print ("-"*55)
        admin_login()

    else:
        print ("\nAdmin Login DENIED!!!""\nExiting......\n")
        main_menu()

def admin_login_menu(): #Incomplete choices
    while True:
        print ("-"*55)
        print ("\t\t       Admin Menu")
        print ("-"*55)
        print (" Admin, what would you like to do today?\n")
        print (" 1. View Libraries")
        print (" 2. View Users")
        print (" 3. Log out")

        choice = input ("\nEnter your choice: ")

        if choice == "1": #add
            print ("-"*55)
            avail_vb()
        
        elif choice == "2": #change
            print ("-"*55)
            print (users_list)

        elif choice == "3":
            main_menu()
        
        else:
            print ("-"*55)
            print ("\nInvalid Input")
            print ("Please Try Again!!\n")
            print ("-"*55)
            admin_login_menu()

def user_login(): #MAIN3
    print ("\t\t       User Login")

    while True:
            print ("-"*55)
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            if users_list.get(username) and users_list[username]['password'] == password:
                print("\nLogin Successful")
                user_login_menu(username)
            elif not username:
                print("\nUser does not exist!!!")
                main_menu()
            else:
                print("\nInvalid account username or password")
                main_menu()

def user_login_menu(username): #INC
    while True:
        print ("-"*55)
        print ("\t\t        User Menu")
        print ("-"*55)
        print (f" Hello,{username}""\n What would you like to do today?\n")
        view_vb()
        print (" 1. Book a Vacation Stay")
        print (" 2. Currently Booked Vacation Stays")
        print (" 3. Log out")

        choice = input ("\nEnter your choice: ")

        if choice == "1": #change
            print ("-"*55)
            view_vb()
        
        elif choice == "2": #change
            print ("-"*55)
            pass

        elif choice == "3":
            main_menu()
        
        else:
            print ("-"*55)
            print ("\nInvalid Input")
            print ("Please Try Again!!\n")
            print ("-"*55)
            user_login_menu()

def main_menu(): #MAIN
    while True:
        print ("="*55)
        print (" Welcome to the Philippines Vacation Booking System!!!")
        print ("="*55)
        print (" 1. Available Vacation Locations")
        print (" 2. Admin Login")
        print (" 3. User Login")
        print (" 4. Register User")
        print (" 5. Exit")

        choice = input ("\nEnter your choice: ")
        print ("-"*55)
    
        if choice == "1":
            avail_vb()
            
        
        elif choice == "2":
            admin_login()

        elif choice == "3":
            user_login()
        
        elif choice == "4":
            register_user()

        elif choice == "5":
            print ("\nExiting Philippines Vacation Booking System!!!")
            print ("Have A Nice Day!!!:D\n")
            break
        
        else:
            print ("\nInvalid Input")
            print ("Please Try Again!!\n\n")
            main_menu()

main_menu()
