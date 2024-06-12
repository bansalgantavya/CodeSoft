# TO DO List
# In this code, we're keeping things straightforward with basic Python—no rocket science needed! 🚀

# Here's the deal: We have a list called listdo where all the operations take place.
#  Our while loop will keep running until you type the magic word: 'exit'. 
# Before you leave, don't forget to save your changes!

# Here’s how you can manage your tasks:
# Add a task: Use the add command followed by the task.
# Remove a task: Use the remove command followed by the task.
# Save your list: Just type the save command.
# View your list: Type the show command to see your to-do list.
# We hope you enjoy using this code and working on the project. 
# And hey, don’t forget to give a star this repo!
# 
a=0
listdo=[]
print('''Hey! Welcome to our todolist powered by CODESOFT
    Commands Overview:
Add a Task: add
Remove a Task: remove
Save the List: save
Show the To-Do List: show
Exit the Program: exit (Make sure to save changes before exiting!)''')
while(a!='exit'):
    a=input("Enter your operation or do 'save' and 'exit' to quit: ")
    if a=='add':
        task=input("Enter your task: ")
        listdo.append(task)
    elif a=='remove':
        task=input("Enter your task: ")
        listdo.remove(task)
    elif a=='show':
        for i in listdo:
            print(i)
    elif a=='exit':
        if(input("confirm exit?? enter 'y' else 'n': ")=='y'):
            break
    elif a=='save':
        with open('todo.txt', 'w') as f:
            for item in listdo:
                f.write("%s\n" % item)

    else:
        print("Invalid input")