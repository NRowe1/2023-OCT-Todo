from todo_funtions import add_todo, remove_todo, view_todo, mark_todo

file_name = "lists.csv"

try:
    # Open the file in read mode
    todo_file = open(file_name, "r")
    todo_file.close()
    print("In try block")
    # If it throws error, it means the file doesn't exist
    # If no error, it means the file exist
except FileNotFoundError:
    # Now, we know the file doesn't exist
    # Create the file
    todo_file = open(file_name, "w")
    # We can also inser the first line into the file
    todo_file.write("title,completed\n")
    todo_file.close()
    print("in except block")


print("Welcome to your TODO List")

def create_menu():
    print("1. Enter 1 to add item to your list")
    print("2. Enter 2 to remove item from your lists")
    print("3. Enter 3 to mark an item as completed")
    print("4. Enter 4 to view your todo lsit")
    print("5. Enter 5 to exit")
    choice = input("Enter your selection: ")
    return choice

# create_menu()

users_choice = ""

while users_choice != "5":
    users_choice = create_menu()
    if (users_choice == "1"):
        add_todo(file_name)
    elif (users_choice == "2"):
        remove_todo(file_name)
    elif (users_choice == "3"):
        mark_todo(file_name)
    elif (users_choice == "4"):
        view_todo(file_name)
    elif (users_choice == "5"):
        continue
    else:
        print("Invalid Input")


print("Thank you for using todo list")