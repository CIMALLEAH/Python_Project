# Vacation Booking

import uuid

admin_username = "Micha"
admin_password = "507250"

vb_lib = {#Locations Library
    
    '1': {'loc': 'Boracay, Malay', 'p': 2500, 'd':'Guesthouse: 2  guests, 1 bedroom - Beachfront', 'available': True},
    '2': {'loc': 'Boracay, Malay', 'p': 3816, 'd':'Guesthouse: 6  guests, 1 bedroom - Beachfront', 'available': True},
    '3': {'loc': 'Boracay, Malay', 'p': 4421, 'd':'Guesthouse: 2  guests, 1 bedroom - Beachfront', 'available': True},
    '4': {'loc': 'El Nido', 'p': 2500, 'd':'Guesthouse: 2  guests, 1 bedroom - Beachfront', 'available': True},
    '5': {'loc': 'Mabini', 'p': 3496, 'd':'Guesthouse: 4  guests, 1 bedroom  - Beachfront', 'available': True},
    '6': {'loc': 'Lian', 'p': 13500, 'd':'Guesthouse: 8  guests, 2 bedroom - Beachfront', 'available': True},

}

users_list = { #Users
    
    "tester": {"password": "111111", "bookings": [], "booking_history": []},

}

av_b = list(vb_lib.keys())

def view_vb():  #All Vacation Locations
    print ("-"*55)
    print ("         Vacation Locations in the Philippines")
    print ("-"*55)
    for index, (name, det) in enumerate(vb_lib.items(), start=1):
        print (index, ".\n   Number: ",{name},"\n   Location: ", det['loc'], "\n   Price: Php {:.2f}".format(float(det['p'])), "\n  ", det['d'])
        print () 
    
def view_all_booked(): #Compiled Already Booked Loacations
    bookings_exist = False
    print ("-"*55)
    print("      Currently Booked Vacation Stays (All Users)")
    print ("-"*55)
    for username, user_details in users_list.items():
        bookings = user_details.get("bookings", [])
        if bookings:
            bookings_exist = True
            print ("-"*55)
            print(f"\nUser: {username}")
            for index, booking in enumerate(bookings, start=1):
                print(f"   {index}. Location: {booking['location']}")
                print(f"      Duration: {booking['duration']} days")
                print(f"\n      Total Cost: Php {booking['total_cost']:.2f}")
            print ("-"*55)
            print()

    if not bookings_exist:
        print("\nNo bookings found.")
        print ("-"*55)

def avail_vb(): #Available Locations
    print ("-"*55)
    print ("     Available Vacation Locations in the Philippines")
    print ("-"*55)
    av_bl = [key for key, value, in vb_lib.items() if value['available']]
    if av_bl:
        for index, name in enumerate(av_bl, start=1):
            det = vb_lib[name]
            print (index, ".\n   Number: ",{name},"\n   Location: ", det['loc'], "\n   Price: Php {:.2f}".format(float(det['p'])), "\n  ", det['d'])
            print () 
    else:
        print ("\n" + " "*16 + "NO AVAILABLE LOCATIONS")

def vb_h(admin, username):  # View Booking History
    if admin == "Micha":
        if username:
            booking_history = users_list.get(username, {}).get("booking_history", [])
            if not booking_history:
                print(f"No booking history found for user: {username}\n")

            else:
                print(f"\nBooking History for user {username}: \n")
                for i, booking in enumerate(booking_history, start=1):
                    print(f"{i}. Location: {booking['location']}, Duration: {booking['duration']} days,\n   Total Cost: Php {booking['total_cost']:.2f}")
                print()
        else:
            print("No username provided.\n")

    else:
        booking_history = users_list[username].get("booking_history", [])
        if not booking_history:
            print("No booking history.\n")
            
        else:
            print("\nYour Booking History:")
            for i, booking in enumerate(booking_history, start=1):
                print(f"{i}. Location: {booking['location']}, Duration: {booking['duration']} days,\n  Total Cost: Php {booking['total_cost']:.2f}")
            print()

    input("\nPress Enter to exit...")

def aview_userbh(): #Admin Viewing Users Booking History
    print ("-"*55)
    print ("                  User Booking History")
    print ("-"*55)
    username = input("\nEnter the Username of User: ")
    if username in users_list:
        vb_h(admin_username, username) 
        input("\nPress Enter to exits...")
        return admin_login_menu()
    else:
        print("\nUser not found.")
        input("\nPress Enter to exits...")
        return admin_login_menu()

def view_auab(): #Users and Their Bookings
    print ("-"*55)
    print("All Users and Their Booking Status")
    print ("-"*55)
    total_currently_booked = 0
    for index, (username, user_details) in enumerate(users_list.items(), start=1):
        bookings = user_details.get("bookings", [])
        booking_status = "Has Bookings" if bookings else "No Bookings"
        print(f"{index}. User: {username} - {booking_status}")
        if bookings:
            total_currently_booked += len(bookings)
    print(f"\nTotal Currently Booked Vacation Stays: {total_currently_booked}\n")

def bv_s(username): #Book a Vacation 
    print ("-"*55)
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

            print ("\n Location: ",det['loc'],"\n Price: Php {:.2f}".format(float(det['p'])), "\n", det['d'])
            while True:
                ls = int(input("\n How long will the duration of your stay (in days) be? "))
                if ls <= 0:
                    print("Invalid input. Please enter a valid duration.")
                else:
                    break

            total_cost = round(float(det['p']) * ls, 2)
            print("\n Total Cost of your {} day/s Stay: Php {:.2f}".format(ls, total_cost)) 
            
            book = input("\n Book this Location? (Y/N): ").lower()
            if book == 'y':
                print ("\n Location Booked Successfully")

                booking_details = {
                    "location": det['loc'],
                    "duration": ls,
                    "total_cost": round(total_cost,2)
                    }
                users_list[username]["bookings"].append(booking_details)
                users_list[username]["booking_history"].append(booking_details.copy())
                det['available'] = False 

                while True:
                    book_again = input("\n Do you wish to Book another? (Y/N): ").lower()
                    if book_again == 'y':
                        bv_s(username)
                    elif book_again == 'n':
                        return_lm = input("\n Return to the main menu? (Y/N): ").lower()
                        if return_lm == 'y':
                            user_login_menu(username)
                        elif return_lm == 'n':
                            book_again
                    else:
                        print("\n Invalid input.")
            else:
                print("\n Booking canceled.")
                return
            
        else:
            print("\n Invalid choice. Please enter a valid number corresponding to a location.")
            return

def b_bvs(username): #View and Edit Currently Booked Vacation Stays
    bookings = users_list[username]["bookings"]

    if not bookings:
        print(f"{username}, you have no current bookings.\n")
        input("\nPress Enter to exits...")
        return user_login_menu(username)
    
    while True:

        print("\nCurrently Booked Locations:")
        for i, booking in enumerate(bookings, start=1):
            print(f"{i}. Location: {booking['location']}, Duration: {booking['duration']} days,\n  Total Cost: Php {booking['total_cost']:.2f}")

    
        choice = input("\nDo you want to Cancel/Delete a Booked Location? (Y/N): ").lower()
        if choice == 'n':
            return user_login_menu(username)
        elif choice == 'y':
            try:
                booking_number = int(input("\nEnter the number of the booking you want to delete (0 to cancel): "))
                if booking_number == 0:
                    return
                elif 1 <= booking_number <= len(bookings):
                    cancelled_booking = bookings.pop(booking_number - 1)
                    av_b.append(cancelled_booking['location']) 
                    print("\nBooked Location Canceled/Deleted Successfully.")
                    input("\nPress Enter to exits...")
                    return user_login_menu(username)
                else:
                    print("Invalid number. Please enter a valid  number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

def add_loc(): #Add Locations
    print("-" * 55)
    print("\t\t      Add Location")
    print("-" * 55)
    loc_name = input("\nEnter the location name: ")
    price = input("Enter the price for this location (Php): ")
    description = input("Enter the description of this location (EXAMPLE: Guesthouse: 2  guests, 1 bedroom - Beachfront'): ")

    new_key = str(len(vb_lib) + 1)
    vb_lib[new_key] = {'loc': loc_name, 'p': round(float(price), 2), 'd': description, 'available': True}
    print("\nLocation added successfully.")
    input("\nPress Enter to exits...")
    return ad_1()

def del_loc(): #Delete Locations
    print("-" * 55)
    print("\t\t    Delete Location")
    view_vb()
    loc_key = input("Enter the number of the location to delete: ")
    
    if loc_key in vb_lib:
        if int(loc_key) >6:
            del vb_lib[loc_key]
            av_b.append(loc_key)
            print("\nLocation deleted successfully.")
            input("\nPress Enter to exits...")
            return ad_1()
        elif int(loc_key) == 0:
            input("\nPress Enter to exits...")
            return ad_1()
        else:
            print("\nInvalid location number.")
            input("\nTry Again...")
            return del_loc()
    else:
        print("\nThis Location is not allowed to be deleted.")
        input("\nTry Again...")
        return del_loc()

def change_price(): #Change Prices
    print("-" * 55)
    print("\t\t     Change Price")
    view_vb()
    loc_key = input("Enter the number of the location to change price: ")
    if loc_key in vb_lib:
        new_price = input("\nEnter the new price for this location (Php): ")
        vb_lib[loc_key]['p'] = round(float(new_price), 2)
        print("\nPrice changed successfully.")
        input("\nPress Enter to exits...")
        return ad_1()
    else:
        print("\nInvalid location number.")
        input("\nTry Again...")
        return change_price()

def del_user(username_del): #User Delete
    if username_del in users_list:
        del users_list[username_del]
        print(f"\nUser '{username_del}' deleted successfully.")
        input("\nPress Enter to exits...")
        return admin_login_menu()

    else:
        print("\nUser not found.")
        input("\nPress Enter to exits...")
        return admin_login_menu()

def ad_1(): #View and Edit Libraries
    view_vb()
    avail_vb()
    view_all_booked()
    print("\nLocation Editing Options:\n\n  1. Add New Location\n  2. Delete Location\n  3. Change Price For a Vacation Stay\n  4. Exit")
    edit = input("\nWhat would you like to do? ").lower()
    
    if edit == '1':
        add_loc()
    elif edit == '2':
        del_loc()
    elif edit == '3':
        change_price()
    elif edit == '4':
        return admin_login_menu()
    else:
        print("\nInvalid Input.")
        yn = input("\nWould you like to try again? (Y/N): ").lower()
        if yn == 'y':
            return ad_1
        elif yn == 'n':
            input("\nPress Enter to exit...")
            return admin_login_menu()
    
def register_user(): #Register User
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

            users_list[username] = {"password" : password, "bookings":[], "booking_history": []}  
            print("\nUser signed up successfully."f"\nWelcome to you, {username}!!!")
            input("\nPress Enter to continue...")
            return main_menu()
            
def admin_login(): #Admin Login
    print ("-"*55)
    print ("\t\t      Admin Login")
    print ("-"*55)

    ad_un_ip = input ("Enter Admin Username: ")
    ad_pw_ip = input ("Enter Admin Password: ")

    if ad_un_ip == admin_username and ad_pw_ip == admin_password:
        print ("\nAdmin Logged In Successfully!!!")
        input("\nPress Enter to exits...")
        return admin_login_menu()
    
    elif ad_un_ip != admin_username and ad_pw_ip == admin_password:
        print ("\nUsername is incorrect, please try again....")
        admin_login()
    
    elif ad_un_ip == admin_username and ad_pw_ip != admin_password:
        print ("\nPassword is incorrect, please try again....")
        admin_login()

    else:
        print ("\nAdmin Login DENIED!!!""\nExiting......\n")
        main_menu()

def admin_login_menu(): #Admin Menu
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
            ad_1()
        elif choice == "2": #change
            view_auab()
            username_del = input("Enter the username to delete: ")
            del_user(username_del)

        elif choice == "3":
            aview_userbh()

        elif choice == "4":
            logout()
        
        else:
            print ("-"*55)
            print ("\nInvalid Input")
            print ("Please Try Again!!\n")
            admin_login_menu()

def user_login(): #User Login
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

def user_login_menu(username): #User Menu
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
            bv_s(username)

        elif choice == "2": #change
            print ("-"*55)
            b_bvs(username)
        
        elif choice == "3":
            print("-" * 55)
            vb_h(admin_username, username)

        elif choice == "4":
            logout()
        
        else:
            print ("-"*55)
            print ("\nInvalid Input")
            print ("Please Try Again!!\n")
            print ("-"*55)
            user_login_menu(username)

def logout(): #Logout

    current_user = None

    print("\nYou have been successfully logged out.")
    print("Redirecting to the main menu...")
    main_menu() 

def main_menu(): #Main Menu
    while True:
        print ("="*55)
        print (" Welcome to the Philippines Vacation Booking System!!!")
        print ("="*55)
        print ("\n 1. Available Vacation Locations")
        print (" 2. Admin Login")
        print (" 3. User Login")
        print (" 4. Register User")
        print (" 5. Exit")

        choice = input ("\nEnter your choice: ")
    
        if choice == "1":
            avail_vb()
            input("\nPress Enter to exits...")
            return main_menu()
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
