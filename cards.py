from tkinter import *
root=Tk()
root.title('Igatus Calculator')
operator=''
test_input=StringVar()
def btnClicks(numbers):
    global operator
    operator=operator+str(numbers)
    test_input.set(operator)
def btnClear():
    global operator
    operator=''
    test_input.set('')
def btnEquals():
    global operator
    sumup=str(eval(operator))
    test_input.set(sumup)
    operator=''
display=Entry(root,font=('times 20 bold'),textvariable=test_input,bd=30,insertwidth=4,bg='powder blue',justify='right').grid(columnspan=4)
btn7=Button(root,padx=16,pady=16,bd=8,fg='black',font=('times 20 bold'),
            text='7',command=lambda :btnClicks(7)).grid(row=1,column=0)
btn8=Button(root,padx=16,pady=16,bd=8,fg='black',font=('times 20 bold'),
            text='8',command=lambda :btnClicks(8)).grid(row=1,column=1)
btn9=Button(root,padx=16,pady=16,bd=8,fg='black',font=('times 20 bold'),
            text='9',command=lambda :btnClicks(9)).grid(row=1,column=2)
addition=Button(root,padx=16,pady=16,bd=8,fg='black',font=('times 20 bold'),
            text='+',command=lambda :btnClicks('+')).grid(row=1,column=3)
#==================================================
btn4=Button(root,padx=16,pady=16,bd=8,fg='black',font=('times 20 bold'),
            text='4',command=lambda :btnClicks(4)).grid(row=2,column=0)
btn5=Button(root,padx=16,pady=16,bd=8,fg='black',font=('times 20 bold'),
            text='5',command=lambda :btnClicks(5)).grid(row=2,column=1)
btn6=Button(root,padx=16,pady=16,bd=8,fg='black',font=('times 20 bold'),
            text='6',command=lambda :btnClicks(6)).grid(row=2,column=2)
subtraction=Button(root,padx=16,pady=16,bd=8,fg='black',font=('times 20 bold'),
            text='-',command=lambda :btnClicks('-')).grid(row=2,column=3)
#====================================================
btn1=Button(root,padx=16,pady=16,bd=8,fg='black',font=('times 20 bold'),
            text='1',command=lambda :btnClicks(1)).grid(row=3,column=0)
btn2=Button(root,padx=16,pady=16,bd=8,fg='black',font=('times 20 bold'),
            text='2',command=lambda :btnClicks(2)).grid(row=3,column=1)
btn3=Button(root,padx=16,pady=16,bd=8,fg='black',font=('times 20 bold'),
            text='3',command=lambda :btnClicks(3)).grid(row=3,column=2)
multiply=Button(root,padx=16,pady=16,bd=8,fg='black',font=('times 20 bold'),
            text='*',command=lambda :btnClicks('*')).grid(row=3,column=3)
#==================================================
btn0=Button(root,padx=16,pady=16,bd=8,fg='black',font=('times 20 bold'),
            text='0',command=lambda :btnClicks(0)).grid(row=4,column=0)
btnC=Button(root,padx=16,pady=16,bd=8,fg='black',font=('times 20 bold'),
            text='C',command=btnClear).grid(row=4,column=1)
btn=Button(root,padx=16,pady=16,bd=8,fg='black',font=('times 20 bold'),
            text='=',command=btnEquals).grid(row=4,column=2)
division=Button(root,padx=16,pady=16,bd=8,fg='black',font=('times 20 bold'),
            text='/',command=lambda :btnClicks('/')).grid(row=4,column=3)
root.mainloop()