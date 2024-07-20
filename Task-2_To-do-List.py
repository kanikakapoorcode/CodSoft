#TO-DO-LIST 
#Command line version

todo_list = []

def add_task() :
    task = input("Enter your task : ")
    todo_list.append(task)
    print(f"Task '{task}' added to the List.")
    
def view_task() :
    print("  To-Do-list :  ")
    for i , task in enumerate(todo_list,1) :
      print(f"{i}.{task}")
    
def update_task() :
    task_number = int(input("Enter the task Number you want to Update : "))
    new_task = input("Enter the New Task : ")
    todo_list[task_number-1] = new_task
    print(f"Task {task_number} updated to '{new_task}' !")
    
def delete_task() :
    task_number = int(input("Enter the task Number to delete: "))
    del todo_list[task_number-1]
    print(f"Task {task_number} deleted!!")
print("***************************************************************************************\n")    
print("-----------------------------Welcome to the To-Do-List --------------------------------\n")
print("***************************************************************************************\n\n")

print("***************************************************************************************\n")        
print("--------------------------Please follow the given steps Below -------------------------\n")
print("***************************************************************************************\n")    
while True :
    print("1.Add Task----->")
    print("2.View Task----->")
    print("3.Update Task----->")
    print("4.Delete Task----->")
    print("5.Quit")
    choice = input("Enter your Choice : ")
    
    if choice == "1"   :
        add_task()
    elif choice == "2" :
        view_task()
    elif choice == "3" :
        update_task()
    elif choice == "4" :
        delete_task()
    elif choice == "5" :
        print("Thank You!! For Using To-Do-List")
        break
    else :
        print("Invalid Choice!!, Try Again !")