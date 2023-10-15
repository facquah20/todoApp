from Todo_App import Todo_App
        
todo_app = Todo_App() #create a todo instance

def help_func():
    print("==================================================")
    print("Help Menu")
    print("Type 'add' to create a new task ")
    print("Type 'remove' to remove a task ")
    print ("Type 'viewDel' to view deleted tasks")
    print("Type 'viewCur' to view current tasks")
    print("Type 'update' to update the status of a task")
    print("Type 'save' to save your tasks to a file")
    print("Type 'help' to view the help menu again ")
    print("Type 'stop' to end program")
    print("=======================================================")

help_func()
#commands in the program
commands = {
    "ADD":'add',
    "REMOVE":'remove',
    "VIEW_DELETED":'viewDel',
    "VIEW_CURRENT":'viewCur',
    "UPDATE":'update',
    "HELP":'help',
    "STOP":'stop',
    "SAVE":'save'
}

is_program_running = True

while is_program_running:
    try:
        command = input(">>")
        if(command == commands["ADD"]):
            todo_app.add_task()
        elif command == commands["REMOVE"]:
            todo_app.remove_task()
        elif command == commands["VIEW_CURRENT"]:
            todo_app.view_current_tasks()
        elif command == commands["VIEW_DELETED"]:
            todo_app.view_deleted_tasks()
        elif command == commands["HELP"]:
         help_func()
        elif command == commands["UPDATE"]:
            todo_app.update_status_of_task()
        elif command == commands["SAVE"]:
            todo_app.save_tasks_to_file()
        elif command == commands["STOP"]:
            print('Program terminated')
            is_program_running = False
        else:
            print('command not recognised')
    except ValueError:
        print("You have to enter an integer not a letter or a character")
    except IndexError:
        print('You entered an id that does not match any task')
    except Exception as err:
        print(err)
        print('An exception was raised ')
