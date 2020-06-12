from tkinter import *
import sqlite3
import tkinter.messagebox
#connecting to the database
conn = sqlite3.connect('hospital1.db')
#cursor to move around the database
#tkinter window
c=conn.cursor()
class Application:
    def __init__(self,master):
        self.master=master

        #creating the frame in the master
        self.left=Frame(master,width=920,height=720,bg='lightgreen')
        self.left.pack(side=LEFT)
        self.right = Frame(master,width=400,height=720,bg='steelblue')
                           #creating labels for windows
        self.heading=Label(self.left,text='NEIGHBOUR Hospital Appointments',font=('arial 40 bold'),fg='black',bg='lightgreen')
        self.heading.place(x=0,y=0)
        #patients name
        self.name=Label(self.left,text='Patient\'s name',font=('arial 18 bold'),fg='black',bg='lightgreen')
        self.name.place(x=0,y=100)
        #age
        self.age=Label(self.left,text='Age',font=('arial 18 bold'),fg='black',bg='lightgreen')
        self.age.place(x=0, y=140)
        #gender
        self.gender=Label(self.left,text='Gender',font=('arial 18 bold'),fg='black',bg='lightgreen')
        self.gender.place(x=0,y=180)
        #location
        self.location=Label(self.left,text='Location',font=('arial 18 bold'),fg='black',bg='lightgreen')
        self.location.place(x=0,y=220)
        #entries for all labels
        self.name_ent=Entry(self.left,width=30)
        self.name_ent.place(x=250,y=100)
        #age
        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=250, y=140)

        self.gender_ent = Entry(self.left, width=30)
        self.gender_ent.place(x=250, y=180)

        self.location_ent = Entry(self.left, width=30)
        self.location_ent.place(x=250, y=220)
        #button to perform a command
        self.submit=Button(self.left,text='Add appointments',width=20,height=2,bg='steelblue',command=self.add)
        self.submit.place(x=300,y=300)
        #take note when adding a command to a button that is inside a class that you
        #created, remember to add self to the name of the function
#function to call when the submit button is clicked
    def add(self):
        self.val1=self.name_ent.get()
        self.val2=self.age_ent.get()
        self.val3=self.gender_ent.get()
        self.val4=self.location_ent.get()

        if self.val1==''or self.val2=='' or self.val3=='' or self.val4=='':
            tkinter.messagebox.showinfo('Warning','Please fill up all the Boxes')
        else:
            sql="INSERT INTO 'patients' (name,age,gender,location)VALUES(?,?,?,?)"
            c.execute(sql,(self.val1,self.val2,self.val3,self.val4))
            conn.commit()
            print('Successfully added to the database')
            #tkinter.messagebox.showinfo('success','Appointments for '+str(self.val1)+ 'has been created')
            conn.close()
root = Tk()
b=Application(root)
#resolution of the window
root.geometry('1200x720+0+0')
#preventing the resize feature
root.resizable(False,False)
#end the loop
root.mainloop()