import csv

def add_todo(file_name):
    print("Add todo")
    # Ask the title for the todo
    todo_name = input("Enter a todo: ")
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([todo_name, "False"])


    # Insert that value into the file - list.csv
    # While inserting - title = user entered
                        #completed = false

def remove_todo(file_name):
    print("Remove todo")

def mark_todo(file_name):
    print("Mark todo")

def view_todo(file_name):
    print("View todo")