# Import necessary modules
import hashlib
import getpass
import random
import string

# Define a dictionary to store the users
users = {
    "admin": {"password": hashlib.sha256("admin123".encode()).hexdigest(), "level": 3, "profile": {"name": "Admin", "email": "admin@example.com"}},
    "moderator": {"password": hashlib.sha256("mod123".encode()).hexdigest(), "level": 2, "profile": {"name": "Moderator", "email": "moderator@example.com"}},
    "user": {"password": hashlib.sha256("user123".encode()).hexdigest(), "level": 1, "profile": {"name": "User", "email": "user@example.com"}}
}

def register_user():
    # Register a new user
    username = input("Enter a new username: ")
    password = getpass.getpass("Enter a new password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    users[username] = {"password": hashed_password, "level": 1, "profile": {"name": name, "email": email}}
    print("User registered successfully!")

def login(username, password):
    # Check if the username exists
    if username in users:
        # Check if the password matches
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if users[username]["password"] == hashed_password:
            # Return the level of the user
            return users[username]["level"]
        else:
            print("Invalid password")
            return None
    else:
        print("Username not found")
        return None

def change_password(username):
    # Change the password for a user
    old_password = getpass.getpass("Enter your current password: ")
    hashed_old_password = hashlib.sha256(old_password.encode()).hexdigest()
    if users[username]["password"] == hashed_old_password:
        new_password = getpass.getpass("Enter a new password: ")
        hashed_new_password = hashlib.sha256(new_password.encode()).hexdigest()
        users[username]["password"] = hashed_new_password
        print("Password changed successfully!")
    else:
        print("Invalid current password")

def reset_password(username):
    # Reset the password for a user
    print("Resetting password...")
    new_password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(12))
    hashed_new_password = hashlib.sha256(new_password.encode()).hexdigest()
    users[username]["password"] = hashed_new_password
    print("New password:", new_password)

def view_profile(username):
    # View the profile of a user
    print("Profile:")
    print("Name:", users[username]["profile"]["name"])
    print("Email:", users[username]["profile"]["email"])

def edit_profile(username):
    # Edit the profile of a user
    name = input("Enter your new name: ")
    email = input("Enter your new email: ")
    users[username]["profile"]["name"] = name
    users[username]["profile"]["email"] = email
    print("Profile updated successfully!")

def delete_account(username):
    # Delete the account of a user
    if username in users:
        del users[username]
        print("Account deleted successfully!")
    else:
        print("Username not found")

def main():
    print("Welcome to the three-level password system!")
    while True:
        print("1. Login")
        print("2. Register")
        print("3. Change Password")
        print("4. Reset Password")
        print("5. View Profile")
        print("6. Edit Profile")
        print("7. Delete Account")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")
            level = login(username, password)

            if level == 3:
                print("You are an admin!")
                # Admin-level access
                print("You have access to all features")
                while True:
                    print("1. Manage Users")
                    print("2. Manage Profiles")
                    print("3. Back to Main Menu")
                    admin_choice = input("Enter your choice: ")
                    if admin_choice == "1":
                        print("Manage Users:")
                        print("1. List all users")
                        print("2. Search for a user")
                        print("3. Back to Admin Menu")
                        manage_users_choice = input("Enter your choice: ")
                        if manage_users_choice == "1":
                            print("List of all users:")
                            for user in users:
                                print(user)
                        elif manage_users_choice == "2":
                            search_username = input("Enter the username to search: ")
                            if search_username in users:
                                print("User found!")
                                print("Username:", search_username)
                                print("Name:", users[search_username]["profile"]["name"])
                                print("Email:", users[search_username]["profile"]["email"])
                            else:
                                print("User not found")
                        elif manage_users_choice == "3":
                            break
                        else:
                            print("Invalid choice. Please try again.")
                    elif admin_choice == "2":
                        print("Manage Profiles:")
                        print("1. List all profiles")
                        print("2. Search for a profile")
                        print("3. Back to Admin Menu")
                        manage_profiles_choice = input("Enter your choice: ")
                        if manage_profiles_choice == "1":
                            print("List of all profiles:")
                            for user in users:
                                print("Username:", user)
                                print("Name:", users[user]["profile"]["name"])
                                print("Email:", users[user]["profile"]["email"])
                        elif manage_profiles_choice == "2":
                            search_username = input("Enter the username to search: ")
                            if search_username in users:
                                print("User found!")
                                print("Username:", search_username)
                                print("Name:", users[search_username]["profile"]["name"])
                                print("Email:", users[search_username]["profile"]["email"])
                            else:
                                print("User not found")
                        elif manage_profiles_choice == "3":
                            break
                        else:
                            print("Invalid choice. Please try again.")
                    elif admin_choice == "3":
                        break
                    else:
                        print("Invalid choice. Please try again.")
            elif level == 2:
                print("You are a moderator!")
                # Moderator-level access
                print("You have access to some features")
                while True:
                    print("1. Manage Profiles")
                    print("2. Back to Main Menu")
                    moderator_choice = input("Enter your choice: ")
                    if moderator_choice == "1":
                        print("Manage Profiles:")
                        print("1. List all profiles")
                        print("2. Search for a profile")
                        print("3. Back to Moderator Menu")
                        manage_profiles_choice = input("Enter your choice: ")
                        if manage_profiles_choice == "1":
                            print("List of all profiles:")
                            for user in users:
                                print("Username:", user)
                                print("Name:", users[user]["profile"]["name"])
                                print("Email:", users[user]["profile"]["email"])
                        elif manage_profiles_choice == "2":
                            search_username = input("Enter the username to search: ")
                            if search_username in users:
                                print("User found!")
                                print("Username:", search_username)
                                print("Name:", users[search_username]["profile"]["name"])
                                print("Email:", users[search_username]["profile"]["email"])
                            else:
                                print("User not found")
                        elif manage_profiles_choice == "3":
                            break
                        else:
                            print("Invalid choice. Please try again.")
                    elif moderator_choice == "2":
                        break
                    else:
                        print("Invalid choice. Please try again.")
            elif level == 1:
                print("You are a user!")
                # User-level access
                print("You have access to limited features")
                while True:
                    print("1. View Profile")
                    print("2. Edit Profile")
                    print("3. Delete Account")
                    print("4. Back to Main Menu")
                    user_choice = input("Enter your choice: ")
                    if user_choice == "1":
                        view_profile(username)
                    elif user_choice == "2":
                        edit_profile(username)
                    elif user_choice == "3":
                        delete_account(username)
                    elif user_choice == "4":
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid login credentials")
        elif choice == "2":
            register_user()
        elif choice == "3":
            username = input("Enter your username: ")
            change_password(username)
        elif choice == "4":
            username = input("Enter your username: ")
            reset_password(username)
        elif choice == "5":
            username = input("Enter your username: ")
            view_profile(username)
        elif choice == "6":
            username = input("Enter your username: ")
            edit_profile(username)
        elif choice == "7":
            username = input("Enter your username: ")
            delete_account(username)
        elif choice == "8":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()