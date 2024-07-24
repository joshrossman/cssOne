tasks_list=[]
tasks_complete=[]
def add_task():
    title=input("What is the title of your task?")
    my_task=input("What is your task?")
    tasks_list.append(title+"***"+my_task)
    tasks_complete.append(False)
 
def view_tasks(my_var):
    print("\033[1mTo-Do List (Tasks crossed out if marked complete):\033[0m")
    counter=0
    for i in range(len(tasks_list)):
        counter+=1
        hold_task=tasks_list[i].split("***")
        if tasks_complete[i]==False:
            print(f"{counter}. {hold_task[0]}:{hold_task[1]}")  
        elif tasks_complete[i]==True:
            str=f"{counter}.{hold_task[0]}: {hold_task[1]}"
            print("\033[9m{}\033[0m".format(str))     
            
    """
    for i in range(len(tasks_list)):
        if tasks_complete[i]==True:
            counter+=1
            hold_task=tasks_list[i].split("***")
            
            #print()
    """
    if my_var==True:
        input("Press any key to continue")
def mark_to_remove(): 
    while True:
        try: 
            view_tasks(False)
            completed=input("Which item would you like to remove. (Please submit the number only)")    
            tasks_list.pop(int(completed)-1)
            tasks_complete.pop(int(completed)-1) 
            break
        except TypeError:
            print("Please choose a number")
        except IndexError:
            print("Not a valid choice!")
        except ValueError:
            print("Please choose a number from the list!")
        
       

def mark_done(): 
    while True:
        try: 
            view_tasks(False)
            completed=input("Which item would you like to mark done. (Please submit the number only)")    
            tasks_complete[int(completed)-1]=True
            print("hello")
            break
        except TypeError:
            print("Please choose a number")
        except ValueError:
            print("Please choose a number from the list!")
        

while True:
    choice=input("Welcome to the TO-DO List App!\nMenu:\n1.Add a task\n2.View tasks\n3.Mark a task as complete\n4.Delete a task\n5.Quit\n")
    if choice=="1":
        add_task()
    if choice=="2":
        view_tasks(True)
    if choice=="3":
        if len(tasks_list)!=0:
            mark_done()
        else:
            print("Nothing currently in your list to mark done.")
    if choice =="4":
        if len(tasks_list)!=0:
            mark_to_remove()
        else:
            print("Nothing currently in your list to remove.")
    if choice=="5":
        break
    elif choice!="4" and choice!="3":
        print("Not a valid input! Please input a number between 1 and 5.")
