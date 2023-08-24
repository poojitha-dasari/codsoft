from tkinter import*
root=Tk()
#title of the application
root.title("My calculator")
e=Entry(root,width=50,borderwidth=30,fg="black")
e.grid(row=0,column=0,columnspan=20,padx=20,pady=30)
#declaring the functions
def buttonclick(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def clear():
    e.delete(0,END)
def buttonadd():
    firstnum=e.get()
    global fnum
    global math
    math="add"
    fnum=int(firstnum)
    e.delete(0,END)
def equal():
    secnum=e.get()
    e.delete(0,END)
    if math=="add":
        e.insert(0,fnum+int(secnum))
    elif math=="sub":
       e.insert(0,fnum-int(secnum))
    elif math=="mul":
      e.insert(0,fnum*int(secnum))
    elif math=="div":
      e.insert(0,fnum/int(secnum))
    elif math=="pow":
     e.insert(0,fnum**int(secnum))
def sub():
   firstnum=e.get()
   global fnum
   global math
   math="sub"
   fnum=int(firstnum)
   e.delete(0,END)
   return
def mul():
   firstnum=e.get()
   global fnum
   global math
   math="mul"
   fnum=int(firstnum)
   e.delete(0,END)
   return
def div():
   firstnum=e.get()
   global fnum
   global math
   math="div"
   fnum=int(firstnum)
   e.delete(0,END)
   return
def pow():
   firstnum=e.get()
   global fnum
   global math
   math="pow"
   fnum=int(firstnum)
   e.delete(0,END)
   return
#creation of buttons
button1=Button(root,text="1",padx=40,pady=20,command=lambda:buttonclick(1))
button2=Button(root,text="2",padx=40,pady=20,command=lambda:buttonclick(2))
button3=Button(root,text="3",padx=40,pady=20,command=lambda:buttonclick(3))
button4=Button(root,text="4",padx=40,pady=20,command=lambda:buttonclick(4))
button5=Button(root,text="5",padx=40,pady=20,command=lambda:buttonclick(5))
button6=Button(root,text="6",padx=40,pady=20,command=lambda:buttonclick(6))
button7=Button(root,text="7",padx=40,pady=20,command=lambda:buttonclick(7))
button8=Button(root,text="8",padx=40,pady=20,command=lambda:buttonclick(8))
button9=Button(root,text="9",padx=40,pady=20,command=lambda:buttonclick(9))
button0=Button(root,text="0",padx=40,pady=20,command=lambda:buttonclick(0))
#opeartions
buttonaddd=Button(root,text="+",padx=40,pady=20,command=buttonadd)
buttonsub=Button(root,text="-",padx=40,pady=20,command=sub)
buttonmul=Button(root,text="*",padx=40,pady=20,command=mul)
buttondiv=Button(root,text="/",padx=40,pady=20,command=div)
buttonpower=Button(root,text="power",padx=40,pady=20,command=pow)
buttonequal=Button(root,text="=",padx=40,pady=20,command=equal)
buttonclear=Button(root,text="clear",padx=40,pady=20,command=clear)
buttonquit=Button(root,text="exit",padx=20,pady=10,command=root.quit)
#put buttons on screen
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button0.grid(row=4,column=0)
buttonaddd.grid(row=4,column=1)
buttonsub.grid(row=4,column=2)
buttonmul.grid(row=5,column=0)
buttondiv.grid(row=5,column=1)
buttonpower.grid(row=5,column=2)
buttonclear.grid(row=6,column=0)
buttonequal.grid(row=6,column=1)
buttonquit.grid(row=6,column=2)
root.mainloop()


    



