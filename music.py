from tkinter import *
import pygame
import os
root = Tk()
def start_stop():
    print('')
root.geometry('400x150')
label=Label(root,text='Music Player ',font=('Times new roman',20))
label.grid(row=1,column=1)
button = Button(root,text='o',width=20,command=start_stop)
button.grid(row=4,column=1)
songs_list=os.listdir()
songs_listbox=StringVar(root)
songs_listbox.set('select songs')
menu = OptionMenu(root,songs_listbox,songs_list)
menu.grid(row=4,column=4)
mainloop()