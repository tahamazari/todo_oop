class TodoList:
    def __init__(self):
        self.all_tasks = []
        self.current_date = '19/07/2019'

    def menu(self):
        while True:
            print("Choose from the following actions from below:")
            print("Press 1 to view your TODO List")
            print("Press 2 to add new task to your TODO List")
            print("Press 3 to update previous task")
            print("Press 4 to delete a task")
            print("Press 5 to passed due date")
            print("Press any other number to exit")

            action = int(input())

            if(action == 1):
                self.list_tasks()
            elif(action == 2):
                self.add_task()
            elif(action == 3):
                self.update_task()
            elif(action == 4):
                self.delete_task()
            elif(action == 5):
                self.is_due_date_over()
            else:
                exit()

    def list_tasks(self):
        if(len(self.all_tasks) == 0):
            print("You dont have any tasks in your list")
            return
        print(self.all_tasks)

    def add_task(self):
        self.show_tasks()
        task = {}

        print("Please type the title of your task")
        key = input()
        print("Please type down your task")
        value = input()
        print("Please type down the due date for your task")
        due_date = input()
        task['TITLE: ' + key] = ['TASK: ' + value, 'DueDate: ' + due_date]

        print("Do you want to choose a particular index to add to list?")
        print("Type 'y' for yes or any other key to append at last of list")
        select = input()
        if(select == 'y'):
            print("Type index")
            index = int(input())
            if(index >= len(self.all_tasks)):
                print("Index can't be greater than or equal to length of List\nCould not add task")
                return
            else:
                self.all_tasks.insert(index, task)
                print("New task with title " + key + " added")
                return

        else:
            self.all_tasks.append(task)
            print("New task with title " + key + " added")
            return

    def update_task(self):
        self.show_tasks()
        print("Please type in index of task you want to update")
        index = int(input())
        
        print("Please type in new title of your task")
        key = input()
        print("Type to update current task")
        value = input()
        print("Type the due date for your task")
        due_date = input()

        task = {}
        task['TITLE: ' + key] = ['TASK: ' + value, 'DueDate: ' + due_date]
        self.all_tasks[index] = task

    def delete_task(self):
        self.show_tasks()
        if(len(self.all_tasks) == 0):
            print("Your TODO List is empty! Can't delete anything")
        else: 
            print("Type index of task you want to delete")
            index = int(input())
            if(index >= len(self.all_tasks)):
                print("Index can't be greater than or equal to length of List")
                return
            else:
                self.all_tasks.pop(index)
                return

    def show_tasks(self):
        for i in range(0, len(self.all_tasks)):
            print(str(i) + '. ' + str(self.all_tasks[i]))

    def is_due_date_over(self):
        self.show_tasks()
        current_date = self.current_date.split('/')
        current_date = [ int(x) for x in current_date ]

        print("Choose the task index for which you want to check in format dd/mm/yyyy")
        task = int(input())
        task = self.all_tasks[task]
        task = list(task.values())
        task = task[0][1]
        task = task.split()
        task_date = task[1]
        task_date = task_date.split('/')
        task_date = [ int(x) for x in task_date ]

        if(task_date[2] < current_date[2]):
            print("Task Due date passed!")
            return
        elif(task_date[1] < current_date[1]):
            print("Task Due date passed!")
            return
        elif(task_date[0] < current_date[0]):
            print("Task Due date passed!")
            return
        else:
            print("You still have time to do your task")


todo = TodoList()
todo.menu()