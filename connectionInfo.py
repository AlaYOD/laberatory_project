from tkinter import *
# +-----------+------------+-------------------+-----------------------+-------------+----------+-----------------+---------------------+-------------------+--------------+----------
root = Tk()
root.geometry('1190x550+200+40')
#root.resizable(False,False)
root.config(background='white')
root.title('Alaa [Database Controlls v1.0 (SQL)')
root.iconbitmap('C:\\programing\\PythonGui\\database.png')
title1 = Label(root, text='Database Controlls v1.0 Systems ' , fg='white',bg='#19282f',font=('Tajawal;px=5px'))
title1.pack(fill=X)
# class connectionInfo:
#      def __init__(self,user,password):
         
class connectionInfo:
    def __init__(self,host,user,password):
        self.host=host
        self.user=user
        self.password=password
        print("The host is :{} & User is : {} & and password :{} ".format(host,user,password))
        
    # def getHost(self):        
def show_DBS():
    import mysql.connector
    # 
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '12345'
        

    ) 
    # mycur to excute 
    mycur = conn.cursor()   
    mycur.execute('SHOW DATABASES')
    F=Frame(root,bg='whitesmoke',bd=2,relief=GROOVE)
    F.place(x=400,y=240,width=200,height=360)
    title3=Label(F,text='DATABASE FOUNDS',fg='black',bg='#FF6363')              
    title3.pack(fill=X)
    for x in mycur:
        Label(F, text=x).pack()

def DBconnect():
    import mysql.connector
    from tkinter import messagebox

    host = Enn1.get()
    user = Enn2.get()
    passw = Enn3.get()
    try:
        c=connectionInfo(host,user,passw)
        conn = mysql.connector.connect(
             host = host,
             user = user,
             password = passw
        )
        messagebox.showinfo('DB[System]', 'تم الاتصال بدون مشاكل')
    except mysql.connector.Error as r: 
        messagebox.showerror('Error',r)
def DBcreate():
    import mysql.connector
    from tkinter import messagebox
    db = En1.get()
    try:
        conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '12345'

    ) 
        mycur = conn.cursor()
        mycur.execute('CREATE DATABASE {}'.format(db))
        messagebox.showinfo('DB[System','تم انشاء قاعدة بيانات جديدة')
    except mysql.connector.Error as r :
        messagebox.showerror('Error',r)
        
    
F1 = Frame(root,bg='whitesmoke',bd=1,relief=GROOVE)
F1.place(x=5,y=40,width=300,height=190)

title1 = Label(F1, text='Database Controlls ' , fg='white',bg='#5534A5',font=('Tajawal;px=5px'))
title1.pack(fill=X)




# ===========show Databases ========
L=Label(F1,text='All Database ')
L.place(x=10,y=35)

button1=Button(F1,text='All Data Base',cursor='hand2',command=show_DBS)
button1.place(x=100,y=35,width=90)
button2=Button(F1,text='Hide',bg='#F4DFBA',cursor='hand2')
button2.place(x=200,y=35,width=60)

#================= DBname ==================

L1 = Label (F1,text='DB-Name :')
L1.place(x=10,y=80)

En1 = Entry(F1)
En1.place(x=100,y=80)

b1 = Button(F1, text='Create' , bg = '#F4DFBA', cursor='hand2',command=DBcreate)
b1.place(x=230,y=74,width=60)

# ================ Table ===============

L3 = Label(F1, text = 'Table-cols :')
L3.place(x=10,y=120)


button1=Button(F1,text='Create Table',cursor='hand2')
button1.place(x=100,y=120,width=90)
button2=Button(F1,text='Hide',bg='#F4DFBA',cursor='hand2')
button2.place(x=200,y=120,width=60)

# =============== DBtable ===========
L1 = Label (F1,text='DB-columns :')
L1.place(x=10,y=160)

button1=Button(F1,text='ADD columns ',cursor='hand2')
button1.place(x=100,y=160,width=90)
button2=Button(F1,text='Hide',bg='#F4DFBA',cursor='hand2')
button2.place(x=200,y=160,width=60)



# =============DatabaseConnection======

F2 = Frame(root,bg='whitesmoke',bd=1,relief=GROOVE)
F2.place(x=320,y=40,width=300,height=190)
title2=Label(F2, text='Database Connection ' , fg='white',bg='#5534A5',font=('Tajawal;px=5px'))
title2.pack(fill=X)

# =================server==========
LL1 = Label(F2,text='server-Name :')
LL1.place(x=10,y=35,width=80)

Enn1 = Entry(F2)
Enn1.place(x=100,y=35)

# ================User=========
LL2 = Label(F2,text='user-Name :')
LL2.place(x=10,y=75,width=80)
Enn2 = Entry(F2)
Enn2.place(x=100,y=75)

# ========== pass ===========
LL3 = Label(F2,text='Password :')
LL3.place(x=10,y=115,width=80)
Enn3= Entry(F2)
Enn3.place(x=100,y=115)

BtnConnect = Button(F2,text='Connect ',fg='black',bg='#FFEBC1',bd=1,relief='groove',command=DBconnect)
BtnConnect.place(x=100,y=150,width=80)

LL4 = Label(F2,text='Test the Connect of Server ',fg='black')
LL4.place(x=10,y=170)
logo = PhotoImage(file='database.png')
logolabel = Label(root, image=logo)
logolabel.place(x=630,y=40,width=490,height=600)



# show_DBS()
root.mainloop()