def Tasks() :
    tasks = []
    
    print("------------WELCOME TO THE TO-DO-LIST APP------------------")
    
    total_Task = int(input("\nEnter the Number of Tasks to add : "))
    for i in range(1,total_Task+1):
        task_Name = int(input("Enter task {i}: "))
        tasks.append(task_Name)
        
    print("Today's Tasks are\n{tasks}:")
    while True :
        operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/"))
        
        if operation == 1 :
            new_Task = int(input("Enter the new task: "))
            tasks.append(new_Task)
            print("<------New Task {new_Task} Added------>")
            
        elif operation == 2 :
            update_Task = int(input("Enter the task to be updated: "))
            if update_Task in tasks :
                up = input("Enter the new Task: ")
                ind = tasks.index(update_Task)
                tasks[ind] = up
                print("<------Task {update_Task} Updated------>")
        elif operation == 3 :
            delete_Task = int(input("Enter the task to be deleted: "))
            tasks.remove(delete_Task)
            print("<------Task {delete_Task} Deleted------>")
            
        elif operation == 4 :
            print("Today's Tasks are\n{tasks}:")
            
        elif operation == 5 :
            print("Thank You for using the To-Do-List App")
            