from datetime import datetime
from Todo import Task

class Todo_App():
    def __init__(self):
        self.tasks = []
        self.deleted_tasks = []
        self.total_task:int = 0

    def add_task(self):
        description = str(input("Provide a brief description of your task: "))
        date_created = datetime.now()
        due_date = str(input("Deadline to complete your task (dd/mm/yy): "))
        task = Task(description,due_date,date_created) #create an object of task
        self.tasks.append(task)
        self.total_task+=1
        print("Task added successfully")
    
    def is_id_valid(self,id:int):
        return (id <=self.total_task and id >= 0)

    def update_status_of_task(self):
       task_index = int(input('Enter the index of the task to update: '))
       if self.is_id_valid(task_index):
           status = str(input(" pending | inprogress | completed: "))
           self.tasks[task_index].status = status
           self.tasks[task_index].date_updated = datetime.now()
           print(f"Task with id of {task_index} was updated to {status}")
       else:
           print(f"Task of id {task_index} is invalid or does not exist")


    def remove_task(self):
        task_index = int(input('Enter index of task: '))
        if self.is_id_valid(task_index):
            self.add_to_deleted_task(self.tasks[task_index]) #add to deleted task

            del self.tasks[task_index]
            self.total_task=self.total_task-1

            print(f"task with index {task_index} deleted successfully")
        else:
            print(f"You entered an invalid id of {task_index}")

    def view_tasks(self,tasks):
        for i in range(len(tasks)):
            print("--------------------------------------")
            print(f"Task id : {i}")
            print(f"Description: {tasks[i].description}")
            print(f"Due date : {tasks[i].due_date}")
            print(f"Date created: {tasks[i].date_created}")
            print(f"Date updated: {tasks[i].date_updated}")
            print(f"status: {tasks[i].status}")
    
    def view_deleted_tasks(self):
        self.view_tasks(self.deleted_tasks)

    def view_current_tasks(self):
        self.view_tasks(self.tasks)
        
    def add_to_deleted_task(self,task:Task):
        self.deleted_tasks.append(task)
    
    def save_tasks_to_file(self):
        print("You are about to save your tasks to a file")
        file_name = str(input("Enter the name of your file: "))

        with open(f"todos/{file_name}.txt","w+",encoding='utf-8') as file:
            for i in range(len(self.tasks)):
                file.write("==============================================\n")
                file.write(f"Task id: {i}\n")
                file.write(f"Description: {self.tasks[i].description}\n")
                file.write(f"Date created: {self.tasks[i].date_created}\n")
                file.write(f"Date updated: {self.tasks[i].date_updated}\n")
                file.write(f"Status: {self.tasks[i].status}\n")
                file.write(f"Due date: {self.tasks[i].due_date}\n")
            print(f"Tasks successfully saved in {file_name}.txt")
