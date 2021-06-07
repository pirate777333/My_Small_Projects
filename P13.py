from tkinter import *
import sqlite3

def connect():
    conn=sqlite3.connect('routine.db')
    cur=conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS routine
            (Id INTEGER PRIMARY KEY,
            date TEXT,
            earnings INTEGER,
            exercise TEXT,
            study TEXT,
            diet TEXT,
            python TEXT)''')
    conn.commit()
    conn.close()

#connect()

def insertdata(date,earnings,exercise,study,diet,python):
    conn=sqlite3.connect('routine.db')
    cur=conn.cursor()
    cur.execute('''INSERT INTO routine
                VALUES (NULL,?,?,?,?,?,?)''',
                (date,earnings,exercise,study,diet,python))
    conn.commit()
    conn.close()

#insertdata('1-2-2019',200,'no','no','yes','yes')
#insertdata('2-2-2019',300,'yes','yes','yes','yes')
    
def viewdata():
    conn=sqlite3.connect('routine.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM routine")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

#print(viewdata())

def deletedata(id_):
    conn=sqlite3.connect('routine.db')
    cur=conn.cursor()
    cur.execute("DELETE FROM routine WHERE id=?",(id_,))
    conn.commit()
    conn.close()

#deletedata(2)

def search(date='',earnings='',exercise='',study='',diet='',python=''):
    conn=sqlite3.connect('routine.db')
    cur=conn.cursor()
    cur.execute('''SELECT * FROM routine WHERE date=? OR
                earnings=? OR exercise=? OR study=? OR diet=? OR python=?''',
                (date,earnings,exercise,study,diet,python))
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

#print(search(date='2-2-2019'))

def view_all():
    listb.delete(0,END)
    for r in viewdata():
        listb.insert(END,r)

def search_all():
    listb.delete(0,END)
    for r in search(datext.get(),earningxt.get(),excercisext.get(),studyxt.get(),dietxt.get(),pyxt.get()):
        listb.insert(END,r)    

def add_data():
    insertdata(datext.get(),earningxt.get(),excercisext.get(),studyxt.get(),dietxt.get(),pyxt.get())
    listb.delete(0,END)
    listb.insert(END,(datext.get(),earningxt.get(),excercisext.get(),studyxt.get(),dietxt.get(),pyxt.get()))
    
def get_selected_row(event):
    global selected_row
    index=listb.curselection()[0]
    selected_row=listb.get(index)
    print(index)

def delete_data():
    deletedata(selected_row[0])
    

win = Tk()

win.wm_title('PROJECT DATABASExTKINTER')

l1=Label(win,text='Date')
l1.grid(row=0,column=0)
l2=Label(win,text='Earnings')
l2.grid(row=0,column=2)
l3=Label(win,text='Excercise')
l3.grid(row=1,column=0)
l4=Label(win,text='Study')
l4.grid(row=1,column=2)
l5=Label(win,text='Diet')
l5.grid(row=2,column=0)
l6=Label(win,text='Python')
l6.grid(row=2,column=2)

datext=StringVar()
e1=Entry(win,textvariable=datext)
e1.grid(row=0,column=1)
earningxt=StringVar()
e2=Entry(win,textvariable=earningxt)
e2.grid(row=0,column=3)
excercisext=StringVar()
e3=Entry(win,textvariable=excercisext)
e3.grid(row=1,column=1)
studyxt=StringVar()
e4=Entry(win,textvariable=studyxt)
e4.grid(row=1,column=3)
dietxt=StringVar()
e5=Entry(win,textvariable=dietxt)
e5.grid(row=2,column=1)
pyxt=StringVar()
e6=Entry(win,textvariable=pyxt)
e6.grid(row=2,column=3)

listb=Listbox(win,height=8,width=35)
listb.grid(row=3,column=0,rowspan=9,columnspan=2)

sb=Scrollbar(win)
sb.grid(row=3,column=2,rowspan=9)

listb.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(win,text='ADD',width=12,pady=5,command=add_data)
b1.grid(row=3,column=3)
b2=Button(win,text='SEARCH',width=12,pady=5,command=search_all)
b2.grid(row=4,column=3)
b3=Button(win,text='DELETE',width=12,pady=5,command=delete_data)
b3.grid(row=5,column=3)
b4=Button(win,text='VIEW ALL',width=12,pady=5,command=view_all)
b4.grid(row=6,column=3)
b5=Button(win,text='CLOSE',width=12,pady=5,command=win.destroy)
b5.grid(row=7,column=3)

