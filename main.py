from tkinter import *

task_window = Tk()


def say_hello():
    user_name = name_row_field.get()
    hello = f"Labas, {user_name}!"
    result_row["text"] = hello
    status_row["text"] = "Sukurta"


def clear_result_row():
    result_row["text"] = ""
    status_row["text"] = "Išvalyta"


def revert_changes():
    hello = f"Neveikia atkūrimas!"
    result_row["text"] = hello
    status_row["text"] = "Atkūrimas dar neįgyvendintas"


def close_window():
    task_window.destroy()


name_row = Label(task_window, text="Įveskite vardą")
name_row_field = Entry(task_window)
result_row = Label(task_window, text="")
status_row = Label(task_window, text="", bd=1, relief=SUNKEN, anchor=W)

button = Button(task_window, text="Patvirtinti", command=say_hello)

task_menu = Menu(task_window)
task_window.config(menu=task_menu)
submeniu = Menu(task_menu, tearoff=0)

task_menu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Išvalyti", command=clear_result_row)
submeniu.add_command(label="Atkurti paskutinį", command=revert_changes)
submeniu.add_separator()
submeniu.add_command(label="Išeiti", command=close_window)

name_row.grid(row=0, column=0, sticky=E)
name_row_field.grid(row=0, column=1)
button.grid(row=0, column=2)
result_row.grid(row=1, columnspan=3)
status_row.grid(row=2, columnspan=3, sticky=S)

task_window.bind("<Return>", lambda event: say_hello())
task_window.bind("<Escape>", lambda event: close_window())

task_window.mainloop()

# if __name__ == '__main__':
#    print_hi('PyCharm')
