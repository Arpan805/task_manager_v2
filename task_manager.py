import os
import json

"""
Unique ID → DONE ✅
Deletion By ID → DONE ✅
Complete by ID → DONE ✅
JSON persistence (load_data(), save_data()) → DONE ✅
Invalid menu input → DONE ✅
Keyword search → Not DONE ❌
"""

# Unique Id Done
def unique_id_generation():
    highest = 0
    for task in tasks:
        ext_number = int(task["id"][1:])
        if ext_number >= highest:
            highest = ext_number
    next_id = highest + 1
    return next_id
             

def save_data():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    

def load_data():
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
    return tasks


# Add Function Complete
def add_task():
    # "Every ID should be unique" -- Done
    next = unique_id_generation()
    task = {
        "id" : f"A{next}",
        "title" : input("Enter the Task-Title : "),
        "status" : "[ Incomplete ]"
    }
    # Append the dictionary in the List
    tasks.append(task)

# View Function Complete
def view_tasks():
    if len(tasks) == 0:
        return print("\nThe List is Empty......!!!")
    else :
        print("\n","="*20," Tasks ","="*20,"\n")
        print(f"{'ID':<15}{'Title':<20}{'Status':>15}")
        print("-"*50)
        for task in tasks:     
            print(f"{task["id"]:<15}{task["title"]:<20}{task["status"]:>15}")


# Completion Function complete
def complete_task():
    tas = input("Enter the task Task ID to complete: ")
    for task in tasks:
        # "Tasks are completed by task ID"--Done
        if task["id"].lower() == tas.lower():
            task["status"] = "[ Complete ]"
            return
    return print(f"Task ID : {tas.upper()} Not found.....")

# Deletion function complete
def delete_task():
    ID = input("Enter the Task ID to Delete: ")
    for i in range(len(tasks)):
        if tasks[i]["id"].lower() == ID.lower():
            del tasks[i]
            return
    return print(f"Task ID : {ID.upper()} Not found.....")


# Search Function complete
def search_task():
    title = input("Enter the task Title to complete: ")
    for task in tasks:
        if task["title"].lower() == title.lower():
            print("\n","="*20," Task ","="*20,"\n")
            print(f"{'ID':<15}{'Title':<20}{'Status':>15}")
            print("-"*50)
            print(f"{task["id"]:<15}{task["title"]:<20}{task["status"]:>15}")
            return
    return print(f"Task title {title} Not found.....")

# Main function complete
def main():
    # Here the menu of operations that can user perform
    while True:
        print("""\n============= Task Manager =============
        1. Add Task
        2. View Tasks
        3. Complete Task
        4. Delete Task
        5. Search Task
        6. Exit\n""")

        try:
            choice = int(input("Enter your Choice : "))
        except ValueError:
            print("Invalid Choice...!!!")
        else:
            match choice:
                case 1:
                    add_task()
                    save_data()
                case 2:
                    view_tasks()
                case 3:
                    complete_task()
                    save_data()
                case 4:
                    delete_task()
                    save_data()
                case 5:
                    search_task()
                case 6:
                    break


if __name__ == "__main__":
    if os.path.exists("tasks.json"):
        tasks = load_data()
    else:
        tasks = []
    main()