import tkinter

#create root window
root = tkinter.Tk()

#change root window background colour
root.configure(bg="blue")

#change the title
root.title("To-Do List")

#change size
root.geometry("250x600")

#create empty list
tasks = []

#create functions

def update_listbox():
    #clears current list
    clear_listbox()
    #populate the listbox
    for task in tasks:
        lb_tasks.insert("end", task)

def clear_listbox():
    lb_tasks.delete(0, "end")

def add_task():
    #add task
    task = txt_input.get()
    #make sure text is not empty
    if task !="":
        #append th list
        tasks.append(task)
        #update the list box
        update_listbox()
    else:
        lbl_display["text"] = "Enter a Task"
    txt_input.delete(0,"end")

def del_all():
    #changing it so it should be global
    global tasks
    #clear the task list
    tasks=[]
    #update the list box
    update_listbox()

def del_one():
    task = lb_tasks.get("active")
    if task in tasks:
        tasks.remove(task)
    # update the list box
    update_listbox()

def sort_asc():
    #sorting the list
    tasks.sort()
    # update the list box
    update_listbox()

def sort_dsc():
    # sorting the list
    tasks.sort()
    #reversing the list
    tasks.reverse()
    # update the list box
    update_listbox()

def no_task():
    #no of task
    no_task=len(tasks)
    #message format
    msg = "Number of tasks: %s" %no_task
    #display
    lbl_display["text"]=msg

lbl_title = tkinter.Label(root, text="To-Do-List", bg="white")
lbl_title.pack()

lbl_display = tkinter.Label(root, text="", bg="white")
lbl_display.pack()

txt_input = tkinter.Entry(root, width = 15)
txt_input.pack()

btn_add_task = tkinter.Button(root, text="Add task", fg="black", bg="white", command=add_task)
btn_add_task.pack()

btn_del_all = tkinter.Button(root, text="Delete all", fg="black", bg="white", command =del_all)
btn_del_all.pack()

btn_del_one = tkinter.Button(root, text="Delete", fg="black", bg="white", command=del_one)
btn_del_one.pack()

btn_sort_asc = tkinter.Button(root, text="Sort(ASC)", fg="black", bg="white", command=sort_asc)
btn_sort_asc.pack()

btn_sort_dsc = tkinter.Button(root, text="Sort(DSC)", fg="black", bg="white", command=sort_dsc)
btn_sort_dsc.pack()

btn_no_task = tkinter.Button(root, text="Number of Tasks", fg="black", bg="white", command=no_task)
btn_no_task.pack()

btn_exit = tkinter.Button(root, text="Exit", fg="black", bg="white", command=exit)
btn_exit.pack()

lb_tasks = tkinter.Listbox(root)
lb_tasks.pack()

#start the main events loop
root.mainloop()
