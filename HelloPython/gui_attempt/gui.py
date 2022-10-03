from tkinter import *
from tkinter import messagebox as mb
import tkinter
import functions as f


def get_entry_add():
    last_name = l_n.get()
    print(last_name)
    name = n.get()
    tel = t.get()
    description = d.get()
    f.add_contact(last_name, name, tel, description)
    l_n.delete(0, END)
    n.delete(0, END)
    t.delete(0, END)
    d.delete(0, END)
    mb.showinfo("Success!", "New contact added")

def select_to_change():
    select = box.curselection()
    print(select)

def select_to_delete():
    select = box.curselection()

def clear_all():
    if len(lbl_what_to_find) != 0: 
        lbl_what_to_find.pop().grid_forget()

    if len(lbl_ln) != 0: 
        lbl_ln.pop().grid_forget()
        lbl_n.pop().grid_forget()
        lbl_t.pop().grid_forget()
        lbl_d.pop().grid_forget()

    if len(ent_ln) != 0: 
        ent_ln.pop().grid_forget()
        ent_n.pop().grid_forget()
        ent_t.pop().grid_forget()
        ent_d.pop().grid_forget()


    if len(btn_find) != 0: 
        btn_find.pop().grid_forget()
    if len(btn_add) != 0: 
        btn_add.pop().grid_forget()

    
def get_entry_find():
    to_find = t_f.get()
    result = f.find_contact(to_find)
    if result == 0:
        t_f.delete(0, END)
        mb.showinfo("Fail", "No matches found")
    else:
        t_f.delete(0, END)
        box.grid(column=2, row=4, columnspan=2, rowspan=3)
        scrollbar = Scrollbar(window, command=box.yview)
        scrollbar.grid(column=3, row=4, sticky=N+E+S)
        box.config(yscrollcommand=scrollbar.set)
        contacts = []
        for key, value in result.items():
            contacts.append(value)
        for i in contacts:
            box.insert(END, i)
        Button(window, text="Change contact", command=select_to_change()).grid(column=4, row=4, sticky = N)
        Button(window, text="Delete contact", command=select_to_delete()).grid(column=4, row=4)


def add_clicked():
    # удаляем все, что ранее было создано на странице:
    clear_all()

    # создаем и запоминаем лэйблы для страницы Add contact:

    lbl1 = Label(window, text = 'Last name: ')
    lbl2 = Label(window, text = 'Name: ')
    lbl3 = Label(window, text = 'Phone number: ')
    lbl4 = Label(window, text = 'Description: ')

    lbl1.grid(row=1, column=1)
    lbl2.grid(row=2, column=1)
    lbl3.grid(row=3, column=1)
    lbl4.grid(row=4, column=1)

    lbl_ln.append(lbl1)
    lbl_n.append(lbl2)
    lbl_t.append(lbl3)
    lbl_d.append(lbl4)

    # заканчиваем создание виджетов Entry из тела программы (добавляя менеджер геометрии) и запоминаем их:

    l_n.grid(row=1, column=2)
    n.grid(row=2, column=2)
    t.grid(row=3, column=2)
    d.grid(row=4, column=2)

    ent_ln.append(l_n)
    ent_n.append(n)
    ent_t.append(t)
    ent_d.append(d)

    # создаем кнопку Add и запоминаем ее:
    btn = Button(window, text = "Add", height=1, width=10, command = get_entry_add)
    btn.grid(column=2, row=5)
    btn_add.append(btn)

def find_clicked():
    # удаляем лэйблы, созданные ранее:
    # и чужие, и свои

    if len(lbl_ln) != 0: 
        lbl_ln.pop().grid_forget()
        lbl_n.pop().grid_forget()
        lbl_t.pop().grid_forget()
        lbl_d.pop().grid_forget()

    if len(lbl_what_to_find) != 0: 
        lbl_what_to_find.pop().grid_forget()

    # удаляем виджеты Entry, созданные ранее (если до этого нажималась кнопка Add contact):
    
    if len(ent_ln) != 0: 
        ent_ln.pop().grid_forget()
        ent_n.pop().grid_forget()
        ent_t.pop().grid_forget()
        ent_d.pop().grid_forget() 

    if len(ent_ln) != 0: 
        ent_ln.pop().grid_forget()

    # удаляем кнопку Add, если она есть:
    
    if len(btn_add) != 0: 
        btn_add.pop().grid_forget()
    if len(btn_find) != 0: 
        btn_find.pop().grid_forget()

    # создаем и запоминаем лэйбл для страницы Find contact:

    lbl = Label(window, text = 'Data to find: ')
    lbl.grid(row=1, column=1)
    lbl_what_to_find.append(lbl)

    # заканчиваем создание виджета Entry из тела программы (добавляя менеджер геометрии) и запоминаем его:

    t_f.grid(row=1, column=2)
    ent_what_to_find.append(t_f)

    # создаем кнопку Find и запоминаем ее:

    btn = Button(window, text = "Find", height=1, width=10, command = get_entry_find)
    btn.grid(column=2, row=2)
    btn_find.append(btn)


window = Tk()
window.title('Your phonebook')
window.geometry('440x250')

l_n = Entry(window)
n = Entry(window)
t = Entry(window)
d = Entry(window)
t_f = Entry(window)

box = Listbox(window, width=30)

Button(window, text = "Add contact", height=1, width=10, command = add_clicked).grid(column=0, row=1)
Button(window, text = "Find contact", height=1, width=10, command = find_clicked).grid(column=0, row=2)
Button(window, text = "Show all", height=1, width=10).grid(column=0, row=3)
# Button(window, text = "Export to txt", height=1, width=10).grid(column=0, row=4)

lbl_ln = []
lbl_n = []
lbl_t = []
lbl_d = []
lbl_what_to_find = []

ent_ln = []
ent_n = []
ent_t = []
ent_d = []
ent_what_to_find = []

btn_add = []
btn_find = []

window.mainloop()