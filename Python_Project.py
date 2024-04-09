# Vacation Booking

import uuid

admin_username = "Micha"
admin_password = "507250"

vb_lib = {#DONE
    
    '1': {'loc': 'Boracay, Malay', 'p': 2500, 'd':'Guesthouse: 2  guests, 1 bedroom - Beachfront', 'available': True},
    '2': {'loc': 'Boracay, Malay', 'p': 3816, 'd':'Guesthouse: 6  guests, 1 bedroom - Beachfront', 'available': True},
    '3': {'loc': 'Boracay, Malay', 'p': 4421, 'd':'Guesthouse: 2  guests, 1 bedroom - Beachfront', 'available': True},
    '4': {'loc': 'El Nido', 'p': 2500, 'd':'Guesthouse: 2  guests, 1 bedroom - Beachfront', 'available': True},
    '5': {'loc': 'Mabini', 'p': 3496, 'd':'Guesthouse: 4  guests, 1 bedroom  - Beachfront', 'available': True},
    '6': {'loc': 'Lian', 'p': 13500, 'd':'Guesthouse: 8  guests, 2 bedroom - Beachfront', 'available': True},

}

users_list = { #DONE
    
    "tester": {"password": "111111", "bookings": [], "booking_history": []},

}

av_b = list(vb_lib.keys())

def view_vb():  #DONE
    print ("-"*55)
    print ("   Vacation Locations in the Philippines")
    print ("-"*55)
    for index, (name, det) in enumerate(vb_lib.items(), start=1):
        print (f"{index}.""\n   Location: "f"{det['loc']}""\n   Price: Php "f"{det['p']}"".00""\n   "f"{det['d']}") 
        print () 
    
def view_all_booked():
    print("Currently Booked Vacation Stays (All Users):")
    for username, user_details in users_list.items():
        bookings = user_details.get("bookings", [])
        if bookings:
            print(f"User: {username}")
            for index, booking in enumerate(bookings, start=1):
                print(f"   {index}. Location: {booking['location']}")
                print(f"      Duration: {booking['duration']} days")
                print(f"      Total Cost: Php {booking['total_cost']}.00")
            print()

def avail_vb(): #DONE
    print ("-"*55)
    print ("   Available Vacation Locations in the Philippines")
    print ("-"*55)
    av_bl = [key for key, value, in vb_lib.items() if value['available']]
    if av_bl:
        for index, name in enumerate(av_bl, start=1):
            det = vb_lib[name]
            print (f"{index}.""\n   Location: "f"{det['loc']}""\n   Price: Php "f"{det['p']}"".00""\n   "f"{det['d']}") 
            print () 
    else:
        print ("\n" + " "*16 + "NO AVAILABLE LOCATIONS")

    input("\nPress Enter to exits...")
    return main_menu()

def vb_h(username):
    booking_history = users_list[username]["booking_history"]

    if not booking_history:
        print("\n You have no booking history.\n")
    else:
        print("\nBooking History:")
        for i, booking in enumerate(booking_history, start=1):
            print(f"{i}. Location: {booking['location']}, Duration: {booking['duration']} days, "f"Total Cost: Php {booking['total_cost']}.00")
        print()

def aview_userbh():
    username = input("Enter the Username of User: ")
    if username in users_list:
        vb_h(username)
    else:
        print("User not found.")

def view_auab():
    print("All Users and Their Booking Status:")
    total_currently_booked = 0
    for username, user_details in users_list.items():
        bookings = user_details.get("bookings", [])
        booking_status = "Has Bookings" if bookings else "No Bookings"
        print(f"User: {username} - {booking_status}")
        if bookings:
            total_currently_booked += len(bookings)
    print(f"\nTotal Currently Booked Vacation Stays: {total_currently_booked}\n")

def bv_s(username):#DONE
    print ("             WHICH WOULD YOU LIKE TO BOOK?")
    avail_vb()

    while True:
        choice = input("\n Enter the number of which you wish to book: ")
        print ("-"*55)
        print ("Booking.....")

        choice = int(choice)
        if 1 <= choice <= len(av_b):
            loc = av_b[choice - 1]
            det = vb_lib[loc]

            if det is None:
                print("Invalid location choice. Please select a valid location.")
                return
            
            if not det['available']:
                print("\nLocation is not available for booking.")
                return

            print ("\n Location: ",det['loc'],"\n Price: Php ",det['p'],".00""\n",det['d'])
            while True:
                ls = int(input("\n How long will the duration of your stay (in days) be? "))
                if ls <= 0:
                    print("Invalid input. Please enter a valid duration.")
                else:
                    break

            total_cost = det['p']*ls
            print ("\n Total Cost of your ",ls,"day/s Stay: Php ",total_cost,".00") 
            
            book = input("\n Book this Location? (Y/N): ").lower()
            if book == 'y':
                print ("\n Location Booked Successfully")

                booking_details = {
                    "location": det['loc'],
                    "duration": ls,
                    "total_cost": total_cost
                    }
                users_list[username]["bookings"].append(booking_details)
                users_list[username]["booking_history"].append(booking_details)
                det['available'] = False 

                while True:
                    book_again = input("\n Do you wish to Book another? (Y/N): ").lower()
                    print ("-"*55)
                    if book_again == 'y':
                        bv_s(username)
                    elif book_again == 'n':
                        return_lm = input("\n Return to the main menu? (Y/N): ").lower()
                        if return_lm == 'y':
                            user_login_menu(username)
                        else:
                            print("\n Invalid input.")
                    else:
                        print("\n Invalid input.")
            else:
                print("\n Booking canceled.")
                return
            
        else:
            print("\n Invalid choice. Please enter a valid number corresponding to a location.")
            return

def b_bvs(username): #DONE
    
    bookings = users_list[username]["bookings"]

    if not bookings:
        print(f"\n {username}, you have no bookings.\n")
        return 
    
    print("\nCurrently Booked Locations:")
    for i, booking in enumerate(bookings, start=1):
            print(f"{i}. Location: {booking['location']}, Duration: {booking['duration']} days, Total Cost: Php {booking['total_cost']}.00")

    while True:
        choice = input("\nDo you want to Cancel/Delete a Booked Location? (Y/N): ").lower()
        if choice == 'n':
            return
        elif choice == 'y':
            while True:
                try:
                    booking_number = int(input("\nEnter the number of the booking you want to delete (0 to cancel): "))
                    if booking_number == 0:
                        return
                    elif 1 <= booking_number <= len(bookings):
                        del bookings[booking_number - 1]
                        cancelled_booking = bookings.pop(booking_number - 1)
                        av_b.append(cancelled_booking['location']) 
                        print("Booked Location Canceled/Deleted Successfully.")
                        return
                    else:
                        print("Invalid number. Please enter a valid  number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

def register_user(): #MAIN4
    print ("-"*55)
    print ("\t\t          Sign Up")
    print ("-"*55)

    global account_id
    account_id = str(uuid.uuid4())

    while True:
            username = input("Enter Username: ")
            
            if not username:
                return main_menu()

            if username in users_list:
                print("\nThis username already exists. Please enter  a new username.\n")
                continue

            password = input("Enter Password: ")
            if len(password) < 6:
                print("\nPassword is to short....")
                continue

            users_list[username] = {"password" : password, "bookings":[]}  
            print("\nUser signed up successfully."f"\nWelcome to you, {username}!!!")
            input("\nPress Enter to continue...")
            return main_menu()
            
def admin_login(): #MAIN2
    print ("-"*55)
    print ("\t\t      Admin Login")
    print ("-"*55)

    ad_un_ip = input ("Enter Admin Username: ")
    ad_pw_ip = input ("Enter Admin Password: ")

    if ad_un_ip == admin_username and ad_pw_ip == admin_password:
        print ("\nAdmin Logged In Successfully!!!")
        admin_login_menu()
    
    elif ad_un_ip != admin_username and ad_pw_ip == admin_password:
        print ("\nUsername is incorrect, please try again....")
        admin_login()
    
    elif ad_un_ip == admin_username and ad_pw_ip != admin_password:
        print ("\nPassword is incorrect, please try again....")
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
        print (" 1. View and Edit Libraries")
        print (" 2. View and Edit Users")
        print (" 3. View User Booking History")
        print (" 4. Log out")

        choice = input ("\nEnter your choice: ")

        if choice == "1": #add
            view_vb()
            avail_vb()
            view_all_booked()
        
        elif choice == "2": #change
            view_auab()

        elif choice == "3":
            aview_userbh()

        elif choice == "4":
            main_menu()
        
        else:
            print ("-"*55)
            print ("\nInvalid Input")
            print ("Please Try Again!!\n")
            admin_login_menu()

def user_login(): #MAIN3
    while True:
            print ("-"*55)
            print ("\t\t       User Login")
            print ("-"*55)
            username = input("Enter Username: ")
            password = input("Enter Password: ")

            if len(password) < 6:
                print("\nPassword is too short!!!")
                input("\nPress Enter to try again...")
                continue

            if users_list.get(username) and users_list[username]['password'] == password:
                print("\nLogin Successful")
                input("\nPress Enter to continue...")
                return user_login_menu(username)
            elif not username or username not in users_list:
                print("\nUser does not exist!!!")
                input("\nPress Enter to exits...")
                return main_menu()
            elif username in users_list and users_list[username]['password'] != password:
                print("\nInvalid account username or password.")
                input("\nPress Enter to try again...")
                return user_login()

def user_login_menu(username): #DONE
    while True:
        print ("-"*55)
        print ("\t\t        User Menu")
        print ("-"*55)
        print (f" Hello,{username}""!!""\n What would you like to do today?\n")
        print (" 1. Book a Vacation Stay")
        print (" 2. View and Edit Currently Booked Vacation Stays")
        print (" 3. View Booking History")
        print (" 4. Log out")

        choice = input ("\nEnter your choice: ")

        if choice == "1": #change
            print ("-"*55)
            bv_s(username)

        elif choice == "2": #change
            print ("-"*55)
            b_bvs(username)
        
        elif choice == "3":
            print("-" * 55)
            vb_h(username)

        elif choice == "4":
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
            print ("-"*55)
            break
        
        else:
            print ("\nInvalid Input")
            print ("Please Try Again!!\n\n")
            main_menu()

main_menu()
