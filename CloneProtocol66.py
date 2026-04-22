import os
import re


def select_folder():
    print("Which do you choose? ~#:")
    print("\t[1] ~ Change Drive\n\t[2] ~ WithIn Drive")
    
    try:
        select_option = int(input())
    except ValueError:
        print("Invalid input")
        return

    if select_option == 1:
        optionOne()
    elif select_option == 2:
        optionTwo()
    else:
        print("Invalid choice")


def optionOne():
    select_drive = input("Which Drive to Choose: ")
    changable_dr = select_drive + ":/"

    if not os.path.exists(changable_dr):
        print("Drive not found")
        return

    os.chdir(changable_dr)
    print(f"changed directory to {os.getcwd()}")
    optionTwo()


def optionTwo():
    print(f"> current directory {os.getcwd()}")
    print("Where to Navigate>>> ")

    try:
        select_file = int(input("\t[1] ~ Immediate Children Directory\n\t[2] ~ File\n\t[3] ~ Regex Finder\n\t[4] ~ List Entries\n"))
    except ValueError:
        print("Invalid input")
        return

    if select_file == 1:
        imchildir()
    elif select_file == 2:
        fildir()
    elif select_file == 3:
        regXf()
    elif select_file == 4:
        print(os.listdir(os.getcwd()))
        optionTwo()
    else:
        print("Invalid choice")


def imchildir():
    select_folder_name = input("Enter the Folder: ")

    if not os.path.isdir(select_folder_name):
        print("Folder not found")
        return

    os.chdir(select_folder_name)

    try:
        select_file_rec = int(input("\t[1] ~ Immediate Children Directory\n\t[2] ~ File\n\t[3] ~ Regex Finder\n\t[4] ~ List Entries\n"))
    except ValueError:
        print("Invalid input")
        return

    if select_file_rec == 1:
        imchildir()
    elif select_file_rec == 2:
        fildir()
    elif select_file_rec == 3:
        regXf()
    elif select_file_rec == 4:
        print(os.listdir(os.getcwd()))
        imchildir()
    else:
        print("Invalid choice")


def fildir():
    select_file_name = input("Enter the file to delete: ")

    if not os.path.isfile(select_file_name):
        print("File not found")
        return

    confirm = input(f"Delete '{select_file_name}'? (y/n): ")
    if confirm.lower() != "y":
        print("Cancelled")
        return

    try:
        os.remove(select_file_name)
        print(f"Deleted: {select_file_name}")
    except Exception as e:
        print(f"Error: {e}")


def regXf():
    extensions = input("Enter the extension(s) (comma separated): ")
    ext_list = [ext.strip() for ext in extensions.split(",")]

    pattern = rf"\.({'|'.join(ext_list)})$"
    regex = re.compile(pattern, re.IGNORECASE)

    deleted_count = 0
    yes_to_all = False  # new feature

    for filename in os.listdir(os.getcwd()):
        if regex.search(filename):
            file_path = os.path.join(os.getcwd(), filename)

            try:
                if os.path.isfile(file_path):

                    if not yes_to_all:
                        confirm = input(f"Delete '{filename}'? (y/n/a): ").lower()

                        if confirm == "a":
                            yes_to_all = True
                        elif confirm != "y":
                            continue

                    os.remove(file_path)
                    print(f"Deleted: {filename}")
                    deleted_count += 1

            except Exception as e:
                print(f"Error deleting {filename}: {e}")

    print(f"\nTask complete. Total files deleted: {deleted_count}")


print("[::: Welcome to Protocol66 :::]")
select_folder()
