from database import Database
from user import User
from device import Device

def CLI():
    db = Database("bolt://18.212.60.3:7687", "neo4j", "leave-overloads-directive")
    user_model = User(db)
    device_model = Device(db)

    while True:
        print("------ Menu ------")
        print("1. Create User")
        print("2. Get User")
        print("3. Update User")
        print("4. Delete User")
        print("5. Log In")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            cpf = input("Enter CPF: ")
            user_model.create(name, email, password, cpf)
            print("User created successfully.")

        elif choice == "2":
            cpf = input("Enter CPF: ")
            user = user_model.get(cpf)
            if user:
                print(f"Name: {user[0]['u']['name']}, Email: {user[0]['u']['email']}")
            else:
                print("User not found.")

        elif choice == "3":
            cpf = input("Enter CPF: ")
            name = input("Enter new name (press Enter to skip): ")
            email = input("Enter new email (press Enter to skip): ")
            password = input("Enter new password (press Enter to skip): ")
            user = user_model.update(cpf, name, email, password)
            if user:
                print("User updated successfully.")
            else:
                print("User not found.")

        elif choice == "4":
            cpf = input("Enter CPF: ")
            user = user_model.delete(cpf)
            if user:
                print("User deleted successfully.")
            else:
                print("User not found.")

        elif choice == "5":
            email = input("Enter email: ")
            password = input("Enter password: ")
            user = user_model.get_user_by_email(email)
            if user and user["password"] == password:
                logged_in_user_cpf = user["cpf"]
                print("Login successful.")
            else:
                print("Invalid email or password.")

            if logged_in_user_cpf:
                while True:
                    print("\n------ Device CRUD Menu ------")
                    print("1. Create Device")
                    print("2. Get Device")
                    print("3. Update Device")
                    print("4. Delete Device")
                    print("5. Share Device between Users")
                    print("6. Get Devices from User")
                    print("7. Log Out")

                    device_choice = input("Enter your choice (1-7): ")

                    if device_choice == "1":
                        name = input("Enter device name: ")
                        mac = input("Enter device MAC: ")
                        device_model.create(logged_in_user_cpf, name, mac)
                        print("Device created successfully.")

                    elif device_choice == "2":
                        mac = input("Enter device MAC: ")
                        device = device_model.get(mac)
                        if device:
                            print(f"Name: {device[0]['d']['name']}, MAC: {device[0]['d']['mac']}")
                        else:
                            print("Device not found.")

                    elif device_choice == "3":
                        mac = input("Enter device MAC: ")
                        name = input("Enter new device name (press Enter to skip): ")
                        device = device_model.update(mac, name)
                        if device:
                            print("Device updated successfully.")
                        else:
                            print("Device not found.")

                    elif device_choice == "4":
                        mac = input("Enter device MAC: ")
                        device = device_model.delete(mac)
                        if device:
                            print("Device deleted successfully.")
                        else:
                            print("Device not found.")

                    elif device_choice == "5":
                        device_id = int(input("Enter device MAC: "))
                        source_cpf = logged_in_user_cpf
                        target_cpf = input("Enter target user CPF: ")
                        print(source_cpf, target_cpf, device_id)
                        device_model.share_device_between_users(device_id, source_cpf, target_cpf)
                        print("Device shared successfully.")

                    elif device_choice == "6":
                        devices = device_model.get_devices_from_user(logged_in_user_cpf)
                        print("Devices from user:")
                        if devices:
                            for device in devices:
                                print(f"Device: {device['d']['name']}, MAC: {device['d']['mac']}")
                        else:
                            print("No devices found.")

                    elif device_choice == "7":
                        break

                    else:
                        print("Invalid choice. Please try again.")

            else:
                print("User not found.")

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")

CLI()