from tkinter import*
import  string
import random
def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_characters=string.punctuation
    all=small_alphabets+capital_alphabets+numbers+special_characters
    password_length=int(length_Box.get())
    if choice.get()=="1":
        passwordField.insert(0,random.sample(small_alphabets,password_length))
    if choice.get()=="2":
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))
    if choice.get()=="3":
        passwordField.insert(0,random.sample(all,password_length))
    password=random.sample(all,password_length)
    passwordField.insert(0,password)

root=Tk()


root.config(bg="gray20")
choice=IntVar()
Font=("arial",13,"bold")
passwordLabel=Label(root,text="password generator",font=("times new roman",20,"bold"),bg="gray20",fg="white")
passwordLabel.grid(pady=10)
weakradioButton=Radiobutton(root,text="weak",value=1,variable=choice,font=Font)
weakradioButton.grid(pady=5)
mediumradioButton=Radiobutton(root,text="medium",value=2,variable=choice,font=Font)
mediumradioButton.grid(pady=5)
strongradioButton=Radiobutton(root,text="strong",value=3,variable=choice,font=Font)
strongradioButton.grid(pady=5)
lengthLabel=Label(root,text="password length",font=Font,bg="gray20",fg="white")
lengthLabel.grid()
length_Box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_Box.grid()
generateButton=Button(root,text="generator",font=Font,command=generator)
generateButton.grid(pady=5)
passwordField=Entry(root,width=25,bd=2,font=Font)
passwordField.grid()
root.mainloop()