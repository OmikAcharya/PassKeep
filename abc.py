import tkinter as tk
from tkinter import messagebox
import random
dummy = 0
username = ''
def button_click():
    f = open("details.txt",'r')
    f1 = f.readlines()
    global dummy
    global username
    username = usre.get()
    username = username.strip()
    password = pasw.get()
    check = username+"="+password
    check1 = " "
    for detail in f1:
        if detail.startswith(username):
            check1 = detail
    f.close()
    if check1.endswith("\n"):
        check1 = check1[0:(len(check1)-1)]

    if check == check1:
        dummy = 1
        entry.destroy()
    else:
        messagebox.showinfo("Invalid", "Incorrect Username or Password")
        dummy = 1
        exit()


entry = tk.Tk()
entry.title("Detail Entry")
entry.geometry("350x150+500+300")
entry.resizable(0, 0)
dum = tk.Label(entry, text="Sign In", font=('Elephant', 20))
usre = tk.Entry(entry)
pasw = tk.Entry(entry,show="*")
usrnm = tk.Label(entry, text="Username:", font=('Courier', 15))
psswrd = tk.Label(entry, text="Password:", font=('Courier', 15))
buttona = tk.Button(entry, text="Enter", font=40, width=15, command=button_click)
usre.place(relx=0.5, rely=0.25)
pasw.place(relx=0.5, rely=0.45)
dum.pack()
buttona.place(relx=0.5, rely=0.75,anchor='n')
usrnm.place(relx=0.05, rely=0.25)
psswrd.place(relx=0.05, rely=0.45)
entry.mainloop()

if dummy == 0:
    exit()
def generitator():
    str = ''
    i = 1
    while i <= 16:
        a = random.choice('abcdefghijklmnopqrstuvwqyz')
        b = random.choice('ABCDEFGHIJKLMNOPQRSTUVWQYZ')
        c = random.choice('1234567890')
        d = random.choice('!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~')
        e = random.choice([1, 2, 3, 4])
        if e == 1:
            str += a
        elif e == 2:
            str += b
        elif e == 3:
            str += c
        else:
            str += d
        i += 1
    return str
def random_generator():
    str = generitator()
    l1['state'] = 'normal'
    l1.delete(0, len(l1.get()))
    l1.insert(0, str)
    body.clipboard_clear()
    body.clipboard_append(str)
    l1['state'] = 'readonly'
def copy(str):
    body.clipboard_clear()
    body.clipboard_append(str)
def saved_passwords():
    save = tk.Tk()
    save.title("Saved Passwords")
    save.geometry("600x350")
    file = username+".txt"
    s = open(file, 'r')
    s1 = s.readlines()
    s2 = tk.Button(save, text='copy selected', command=lambda: copy(text.selection_get()))
    text = tk.Text(save, width=40, height=17, spacing3=2, font=40)
    for d in s1:
        text.insert(tk.INSERT, d)
    text['state']= 'disabled'
    newsave=tk.Button(save, text='create new save', command=new_save)
    newsave.pack()
    text.place(relx=0.05, rely=0.1)
    #text.bind('<Double-1>', lambda event: copy(event, text.selection_get()))
    s.close()
    save.mainloop()
def new_save ():
    file = username+'.txt'
    goblin = open(file, 'a')
    ns = tk.Tk()
    acc = tk.Label(ns, text="Account:")
    lpass = tk.Label(ns, text='Password:')
    nusername = tk.Entry(ns)
    npassword = tk.Entry(ns)
    done = tk.Button(ns, text='Enter', command=lambda: [goblin.write("\n"+nusername.get()+"->"+npassword.get()), ns.destroy()])
    rnd = tk.Button(ns, text='Generate random password',
                    command=lambda: [npassword.delete(0, len(npassword.get())), npassword.insert(0, generitator())])
    acc.pack()
    nusername.pack()
    lpass.pack()
    npassword.pack()
    done.pack()
    rnd.pack()
    ns.mainloop()
    goblin.close()
def new_file (n):
    n = n+'.txt'
    goblin1 = open(n, 'w')
    goblin1.close()
def new_user ():
    goblin = open('details.txt', 'a')
    ns = tk.Tk()
    acc = tk.Label(ns, text="Username:")
    lpass = tk.Label(ns, text='Password:')
    nusername = tk.Entry(ns)
    npassword = tk.Entry(ns)
    done = tk.Button(ns, text='Enter',
                     command=lambda: [goblin.write("\n" + nusername.get() + "=" + npassword.get()), new_file(nusername.get()), ns.destroy()])
    acc.pack()
    nusername.pack()
    lpass.pack()
    npassword.pack()
    done.pack()
    ns.mainloop()
    goblin.close()

body = tk.Tk()
body.title("Passwords")
body.geometry("350x450+500+100")
ti = tk.Label(body, text="Welcome", font=('times', 30))
ti2 = tk.Label(body, text=username, font=('bell mt', 33))
generator = tk.Button(body, text="Generate Random Password", font=40, command=random_generator)
newuser = tk.Button(body, text="New User", font=40, command=new_user)
l1 = tk.Entry(body, width=20, state='readonly', justify='center')
saved = tk.Button(body, text='Saved Passwords', font=40, command=saved_passwords)
#ti.place(relx=0.5, rely=0.025, anchor='n')
#ti2.place(relx=0.5, rely=0.1175,anchor='n')
newuser.pack()
saved.pack()
generator.pack()
l1.pack()
body.mainloop()