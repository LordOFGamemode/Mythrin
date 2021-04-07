from tkinter import *
import sqlite3
import time
import tkinter.font as font

def get_arg(tabelle,arg):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT " + arg + " FROM " + tabelle)
    rows = cursor.fetchall()
    conn.close()
    return rows

count = 0
counter = 0
checkupdate = 0
def update():
    checkupdate = 0
    counter = 0
    def uplabel():
        global checkupdate
        if checkupdate == 0:
            checkupdate += 1
        else:
            checkupdate = -1
            funktions('downloadani2')
        my_lable2.config(font=('Arial', 23))
        text = get_arg('displaydata','text')
        my_lable2.config(text=str(text))
        root.after(10000, update)
    uplabel()

text = '#'
text2 = '#'

def download():
    counter = 0
    def startdownl():
        dl.config(font=('Arial', 18))
        global counter
        counter += 1
        global text
        global text2
        if counter == 1:
            text = '#'
        elif counter > 99:
            print('100%')
            counter = 0
        else:
            if counter % 4 == 0:
                text = text + text2
        dl.config(text=str(text))
        print(counter)
        if counter != 99:
            root.after(10, download)

    startdownl()
def defnotfound(function):
    my_lable.config(text='Function ' + function + ' not found!')
    time.sleep(5)
    my_lable.config(text='')

def funktions(function):
    def start(function):
        if function == 'downloadani':
            download()
        else:
            defnotfound(function)
    start(function)

root = Tk()
root.geometry("500x550")
root.title('Mythrin')

root.wm_attributes('-transparentcolor', 'green')

global my_lable
my_lable = Label(root,bg="green",width=400,height=200)
my_lable.pack()

global dl
dl = Label(root,text='hallo welt',bg="green")
dl.place(relx=1.0,rely=0.0,anchor='ne')

global my_lable2
my_lable2 = Label(root,text='hallo welt',bg="green")
my_lable2.place(relx=0.0,rely=1.0,anchor='sw')


update()


root.mainloop()