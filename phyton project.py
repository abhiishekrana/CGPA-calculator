from tkinter import *
import tkinter.messagebox as tmsg
def plot():
    import matplotlib.pyplot as plt
    x = [int(sub1ent.get()),int(sub2ent.get()),int(sub3ent.get()),int(sub4ent.get()),int(sub5ent.get()),int(sub6ent.get()),int(sub7ent.get())]
    index=range(len(x))
    plt.bar(index,x)
    plt.title("Marks Comparision")
    plt.show()
def entry_delete():
    sub1ent.delete(first=0,last=50)
    sub2ent.delete(first=0, last=50)
    sub3ent.delete(first=0, last=50)
    sub4ent.delete(first=0, last=50)
    sub5ent.delete(first=0, last=50)
    sub6ent.delete(first=0, last=50)
    sub7ent.delete(first=0, last=50)
# calculation of TGPA of sem1

root=Tk()
root.geometry("600x644")
# root.maxsize(600,644)
photo=PhotoImage(file="lpu.gif")
lb=Label(image=photo)
lb.grid(row=1)

Label(root,text="CGPA-CALCULATOR",font="helvatica 25 bold italic",pady=15,fg="green").grid(row=2)
f1=Frame(root,borderwidth=3,relief=SUNKEN,bg="black")
f1.grid(row=3)

f2=Frame(root,borderwidth=3,relief=SUNKEN,bg="black")
f2.grid(row=4)

f3=Frame(root,borderwidth=3,relief=SUNKEN,bg="black")
f3.grid(row=3,column=6)

plot1=Label(f2,text="DO you want to see marks comparision among all subjects?",fg="green",bg="black")
plot1.grid()
Button(f2,text="Click here",command=plot,fg="green",bg="black",borderwidth=8).grid()
def counter1():
    tmsg.showinfo("msg","Write credits in console")
    credit1=[]
    marks1 = [int(sub1ent.get()),int(sub2ent.get()),int(sub3ent.get()),int(sub4ent.get()),int(sub5ent.get()),int(sub6ent.get()),int(sub7ent.get())]

    tgpa1,first1,first2,i=0,0,0,0
    print("Enter 7 credits of first sem")
    y=0
    while (y <7):
        credit= int(input(""))
        credit1.append(credit)
        y = y +1

    while (i < 7):
        first1 += credit1[i] * marks1[i]
        first2 += credit1[i]
        i = i + 1
    tgpa1=first1/first2

    my_label.config(text=tgpa1)
my_button = Button(f3,
                   text="TGPA SEM1",
                   command=counter1,bg="black",fg="green",borderwidth=8)

my_label = Label(f3,
                 text="TGPA SEM 1",bg="black",fg="green")
my_label.grid()
my_button.grid()
 # calcilation of TGPA of sem2
def counter2():
    tmsg.showinfo("msg", "Write credits in console")
    marks = [int(sub1ent.get()),int(sub2ent.get()),int(sub3ent.get()),int(sub4ent.get()),int(sub5ent.get()),int(sub6ent.get()),int(sub7ent.get())]
    credit2=[]
    tgpa2,second1,second2,i=0,0,0,0
    print("Enter 7 credits of second sem")
    y=0
    while (y <7):
        credit= int(input(""))
        credit2.append(credit)
        y = y +1

    while (i < 7):
        second1 += credit2[i] * marks[i]
        second2 += credit2[i]
        i = i + 1
    tgpa2=second1/second2

    my_label2.config(text=tgpa2)
my_button = Button(f3,text="TGPA SEM2",command=counter2,bg="black",fg="green",borderwidth=8)

my_label2 = Label(f3,
                 text="TGPA sem 2",bg="black",fg="green")
my_label2.grid(row=0,column=2)
my_button.grid(row=1,column=2)

def sum():
    cgpa= int(sub1ent.get())+int(sub2ent.get())+int(sub3ent.get())+int(sub4ent.get())+int(sub5ent.get())+int(sub6ent.get())+int(sub7ent.get())
    tmsg.showinfo("CGPA",f"CGPA is {cgpa/7}")
    if cgpa/7 == 10:
        tmsg.showinfo("Grade","Grade is O")
    elif cgpa/7 ==  9:
        tmsg.showinfo("Grade","Grade is A+")
    elif cgpa/7 ==  8:
        tmsg.showinfo("Grade","Grade is A")
    elif cgpa/7 ==  7:
        tmsg.showinfo("Grade","Grade is B+")
    elif cgpa/7 ==  6:
        tmsg.showinfo("Grade","Grade is B")
    elif cgpa/7 ==  5:
        tmsg.showinfo("Grade","Grade is C+")
    elif cgpa/7 ==  4:
        tmsg.showinfo("Grade","congratulations! You have reappaer")
    else:
        tmsg.showinfo("Grade","You got fail")

sub1=Label(f1,text="CSE211",fg="green",bg="black")
sub2=Label(f1,text="CSE205",fg="green",bg="black")
sub3=Label(f1,text="CSE320",fg="green",bg="black")
sub4=Label(f1,text="INT213",fg="green",bg="black")
sub5=Label(f1,text="INT306",fg="green",bg="black")
sub6=Label(f1,text="MTH401",fg="green",bg="black")
sub7=Label(f1,text="PEL135",fg="green",bg="black")
sub1.grid(row=1,column=7)
sub2.grid(row=2,column=7)
sub3.grid(row=3,column=7)
sub4.grid(row=4,column=7)
sub5.grid(row=5,column=7)
sub6.grid(row=6,column=7)
sub7.grid(row=7,column=7)
sub1val=StringVar()
sub2val=StringVar()
sub3val=StringVar()
sub4val=StringVar()
sub5val=StringVar()
sub6val=StringVar()
sub7val=StringVar()
sub1ent=Entry(f1,textvariable=sub1val,fg="green",bg="black",insertbackground='green')
sub2ent=Entry(f1,textvariable=sub2val,fg="green",bg="black",insertbackground='green')
sub3ent=Entry(f1,textvariable=sub3val,fg="green",bg="black",insertbackground='green')
sub4ent=Entry(f1,textvariable=sub4val,fg="green",bg="black",insertbackground='green')
sub5ent=Entry(f1,textvariable=sub5val,fg="green",bg="black",insertbackground='green')
sub6ent=Entry(f1,textvariable=sub6val,fg="green",bg="black",insertbackground='green')
sub7ent=Entry(f1,textvariable=sub7val,fg="green",bg="black",insertbackground='green')
sub1ent.grid(row=1,column=8)
sub2ent.grid(row=2,column=8)
sub3ent.grid(row=3,column=8)
sub4ent.grid(row=4,column=8)
sub5ent.grid(row=5,column=8)
sub6ent.grid(row=6,column=8)
sub7ent.grid(row=7,column=8)


b1=Button(f1,text="click!to claculate CGPA",command=sum,bg="black",fg="green",borderwidth=8)
b1.grid(row=8,column=8,pady=23)
B=Button(f1, text="Discard values", command=entry_delete,bg="black",fg="green",borderwidth=8)
B.grid(row=8,column=7,pady=23,padx=23)
root.mainloop()





