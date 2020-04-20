from tkinter import *
from tkinter import ttk
import databaseteacher
import databasestudent
import sqlite3
import take_attendence
#import jaipurtemp

root=Tk()
root.title("Attendence record")
label=0
def createlabel():
    global label,t
    l=Label(root,fg='#1800f5',bg='#fff',image=image222,width=1105)
    l.place(x=0,y=100)
    #if label==0:
       # t="temp: "+str(jaipurtemp.temp())
    label=Label(root,fg='#1800f5',bg='#fff',font='arial 15 bold',width=95)
    label.place(x=0,y=670)
    #label['text']=t
    
def createbatch():
    createlabel()
    databaseteacher.createbatch(root)

def teacher():
    createlabel()
    databaseteacher.addteacher(root)

def comboevent5(event):
    global combo3,combo4,combo5
    createlabel()
    start=combo5.get().split()[1]
    end=combo5.get().split()[3]
    conn=sqlite3.connect("course.db")
    rows=conn.execute(f'''select * from {combo4.get()} where branch_prefer='{combo3.get()}'
                                and stime="{start}" and etime="{end}"''')
    rows=rows.fetchall()
    conn.close()
    X=50
    for i in ['Roll no','Name','Mob No.']:
        label=Label(root,text=i,font='arial 15 bold',bg='#fff',fg='#03f')
        label.place(x=X,y=170)
        X=X+300
    Y=220
    for i in rows:
        X=50
        label=Label(root,text=i[0],font='arial 12 bold',bg='#fff',fg='#03f')
        label.place(x=X,y=Y)
        X=X+300
        label=Label(root,text=i[1],font='arial 12 bold',bg='#fff',fg='#03f')
        label.place(x=X,y=Y)
        X=X+300
        label=Label(root,text=i[3],font='arial 12 bold',bg='#fff',fg='#03f')
        label.place(x=X,y=Y)
        X=X+300
        Y=Y+40

def comboevent4(event):
    global combo3,combo5,combo4
    l=Label(root,text="Select Time Slot",fg='#1800f5',font='arial 15 bold',bg='#fff')
    l.place(x=40,y=310)
    conn=sqlite3.connect("course.db")
    rows=conn.execute(f"select * from {combo4.get()} where branch_prefer='{combo3.get()}'")
    rows=rows.fetchall()
    lis=[]
    for i in rows:
        lis.append(f"from {i[12]} to {i[13]}")
    conn.close()
    lis=list(set(lis))
    lis.sort()
    combo5=ttk.Combobox(root)
    combo5['values']=tuple(lis)
    #combo5['width']=40
    combo5.place(x=300,y=310)
    combo5.bind("<<ComboboxSelected>>", comboevent5)

def comboevent3(event):
    global combo3,combo4
    l=Label(root,text="Select Subject",fg='#1800f5',font='arial 15 bold',bg='#fff')
    l.place(x=40,y=230)
    combo4=ttk.Combobox(root)
    combo4['values']=("Python","Dsa","Django","Java")
    #combo4['width']=40
    combo4.place(x=300,y=230)
    combo4.bind("<<ComboboxSelected>>", comboevent4)

def viewstudent():
    global combo3
    createlabel()
    l=Label(root,text="Select Branch",fg='#1800f5',font='arial 15 bold',bg='#fff')
    l.place(x=40,y=150)
    combo3=ttk.Combobox(root)
    combo3['values']=("Mansarovar","Pratap Nagar")
    #combo3['width']=40
    combo3.place(x=300,y=150)
    combo3.bind("<<ComboboxSelected>>", comboevent3)
    
    
def comboevent2(event):
    global combo1,combo2
    createlabel()
    take_attendence.ok(root,combo1,combo2)

def comboevent(event):
    global combo1,combo2
    l=Label(root,text="Select Subject info.",fg='#1800f5',font='arial 15 bold',bg='#fff')
    l.place(x=40,y=230)
    conn=sqlite3.connect("teacher.db")
    rows=conn.execute(f"select * from allbatch where id='{combo1.get()}'")
    rows=rows.fetchall()
    lis=[]
    for i in rows:
        lis.append(f"{i[0]} : {i[2]} : {i[3]} to {i[4]} at {i[5]}")
    conn.close()
    lis=list(set(lis))
    lis.sort()
    combo2=ttk.Combobox(root)
    combo2['values']=tuple(lis)
    combo2['width']=40
    combo2.place(x=300,y=230)
    combo2.bind("<<ComboboxSelected>>", comboevent2)

def takeattendence():
    global combo1
    createlabel()
    l=Label(root,text="Select your ID",fg='#1800f5',font='arial 15 bold',bg='#fff')
    l.place(x=40,y=150)
    combo1=ttk.Combobox(root)
    conn=sqlite3.connect("teacher.db")
    rows=conn.execute("select * from allteacher")
    rows=rows.fetchall()
    lis=[]
    for i in rows:
        lis.append(i[0])
    conn.close()
    lis=list(set(lis))
    lis.sort()
    combo1['values']=tuple(lis[1:])
    combo1.place(x=300,y=150)
    combo1.bind("<<ComboboxSelected>>", comboevent)

def newenquire():
    createlabel()
    databasestudent.addentry(root)
    
checkv=0
checka=0
root.geometry("1200x800+100+50")

image222=PhotoImage(file="acad3.png")
createlabel()

f=Frame(root,bg='#fff',height=100,width=1360,relief=SOLID)
f.place(x=0,y=0)
#img=PhotoImage(file="logo.png")
Label(f,bg='#fff').place(x=0,y=0)
Label(f,bg='#fff').place(x=1070,y=0)

l=Label(f,text="Attendance Management System",fg='#1800f5'
        ,font='arial 30 bold',bg='#fff')
l.place(x=680,y=50,anchor = CENTER)

f=Frame(root,bg='#fff',height=600,width=250,relief=SOLID)
f.place(x=1110,y=100)

b=Button(f,text="New Enquire",fg="#1800f5",font='arial 18 bold',command=newenquire)
b.place(x=5,y=20)

b=Button(f,text="New teacher",fg="#1800f5",font='arial 18 bold',command=teacher)
b.place(x=5,y=100)

b=Button(f,text="Create Batch",fg="#1800f5",font='arial 18 bold',command=createbatch)
b.place(x=5,y=180)

b=Button(f,text="Take Attendence",fg="#1800f5",font='arial 18 bold',command=takeattendence)
b.place(x=5,y=260)

b=Button(f,text="View student",fg="#1800f5",font='arial 18 bold',command=viewstudent)
b.place(x=5,y=340)

root.mainloop()
