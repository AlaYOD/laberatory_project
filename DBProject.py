from tkinter import *
from tkinter import ttk
import mysql.connector 
from datetime import date

def deleteFrames(main_frame : Frame):
    for frame in main_frame.winfo_children():
        frame.destroy()

def fins(main_frame, *args):
    deleteFrames(main_frame)
    style = ttk.Style()
    style.theme_use('default')

    style.configure("Treeview",
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3")

    style.map('Treeview',
    background=[('selected', "#347083")])
    f1 = Frame(main_frame)
    scroller = Scrollbar(f1)
    scroller.pack(side=RIGHT, fill=Y,pady="25")
    tree = ttk.Treeview(f1, yscrollcommand=scroller.set, selectmode="extended")
    tree.pack(pady="25")
    f1.pack()
    scroller.config(command=tree.yview)
    tree['columns'] = ("Payment ID", "Payment Amount", "Payment Date")

    tree.column("#0", width=0, stretch=NO)
    tree.column("Payment ID", anchor=CENTER, width=140)
    tree.column("Payment Amount", anchor=CENTER, width=140)
    tree.column("Payment Date", anchor=CENTER, width=100)

    tree.heading("#0", text="", anchor=W)
    tree.heading("Payment ID", text="Payment ID", anchor=CENTER)
    tree.heading("Payment Amount", text="Payment Amount", anchor=CENTER)
    tree.heading("Payment Date", text="Payment Date", anchor=CENTER)
    #tree.insert(parent='', index='end', iid=0, text='', values=("15","Test1","1500","dsfd", "dfdfd"))


    def search():
        for child in tree.get_children():
            tree.delete(child) 
        cursor.execute("SELECT * FROM finances f, TestBank T WHERE f.P_ID = T.TB_Payment_ID and T.TB_ID = %s",(e_test.get(),))
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2]))


    search_frame =LabelFrame(main_frame,text="Search", pady="15")
    search_frame.pack(fill="x",padx="20")
    lb_test = Label(search_frame,text="Test Bank ID")
    e_test = Entry(search_frame)
    bt_test = Button(search_frame,text="Search", command=search)
    lb_test.grid(row=0,column=0,padx="10",pady="10")
    bt_test.grid(row=0,column=2,padx="10",pady="10")
    e_test.grid(row=0,column=1,padx="15",pady="10")

    data_frame = LabelFrame(main_frame, text="Payments",pady="20")
    data_frame.pack(fill="x", padx=20)

    lb1 = Label(data_frame, text="Payment ID")
    lb1.grid(row=0, column=0, padx=10, pady=10)
    e1 = Entry(data_frame)
    e1.grid(row=0, column=1, padx=10, pady=10)

    lb2 = Label(data_frame, text="Payment Amount")
    lb2.grid(row=0, column=2, padx=10, pady=10)
    e2 = Entry(data_frame)
    e2.grid(row=0, column=3, padx=10, pady=10)

    lb3 = Label(data_frame, text="Payment Date")
    lb3.grid(row=0, column=4, padx=10, pady=10)
    e3 = Entry(data_frame)
    e3.grid(row=0, column=5, padx=10, pady=10)

    def clear():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)

    def add():
        cursor.execute("UPDATE finances set  P_Amount = P_Amount +  %s ,P_Date = %s where P_ID = %s", (e2.get(),date.today(),e1.get()))
        db.commit()
        for child in tree.get_children():
            tree.delete(child)
        cursor.execute("SELECT * FROM finances")
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2]))
        clear()
    
    def remove():
        cursor.execute("DELETE FROM finances where P_ID=%s", (e1.get(),))
        db.commit()
        for child in tree.get_children():
            tree.delete(child)
        cursor.execute("SELECT * FROM finances")
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2]))
        clear()    
        
    button_frame = LabelFrame(main_frame, text="Options",pady="20")
    button_frame.pack(fill="x", expand="yes", padx=20,pady="20")

    b1 = Button(button_frame, text="Add Payment",command=add)
    b1.grid(row=0, column=0, padx=10, pady=10)

    b3 = Button(button_frame, text="Remove Payment",command=remove)
    b3.grid(row=0, column=2, padx=10, pady=10)

    cursor.execute("SELECT * FROM finances")
    for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2]))
    if args:
        e1.insert(0,args[0])
    e3.insert(0,date.today())  
    def selectItem(a):
            clear()
            curItem = tree.focus()
            e1.insert(0,tree.item(curItem,'values')[0])
            #e2.insert(0,tree.item(curItem,'values')[1])
            #e3.insert(0,tree.item(curItem,'values')[2])
            e3.insert(0,date.today())
    tree.bind('<ButtonRelease-1>', selectItem)

def tests(main_frame):
    deleteFrames(main_frame)
    style = ttk.Style()
    style.theme_use('default')

    style.configure("Treeview",
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3")

    style.map('Treeview',    background=[('selected', "#347083")])
    f1 = Frame(main_frame)
    scroller = Scrollbar(f1)
    scroller.pack(side=RIGHT, fill=Y,pady="25")
    tree = ttk.Treeview(f1, yscrollcommand=scroller.set, selectmode="extended")
    tree.pack(pady="25")
    f1.pack()
    scroller.config(command=tree.yview)
    tree['columns'] = ( "Test ID", "Test Name","Test Description" , "Test Cost", "Chemical Used", "Equipment Used")



    tree.column("#0", width=0, stretch=NO)
    tree.column("Test ID", anchor=CENTER, width=100)
    tree.column("Test Name", anchor=CENTER, width=140)
    tree.column("Test Description", anchor=CENTER,width=200)
    tree.column("Test Cost", anchor=CENTER, width=100)
    tree.column("Chemical Used", anchor=CENTER, width=140)
    tree.column("Equipment Used", anchor=CENTER, width=140)


    tree.heading("#0", text="", anchor=W)
    tree.heading("Test ID", text="Test ID", anchor=CENTER)
    tree.heading("Test Name", text="Test Name", anchor=CENTER)
    tree.heading("Test Description", text="Test Desciption", anchor=CENTER)
    tree.heading("Test Cost", text="Test Cost", anchor=CENTER)
    tree.heading("Chemical Used", text="Chemical Used", anchor=CENTER)
    tree.heading("Equipment Used", text="Equipment Used", anchor=CENTER)

    def search():
        for child in tree.get_children():
            tree.delete(child)  
        cursor.execute("SELECT * FROM Test WHERE T_Name LIKE %s ",("%"+e_test.get()+"%",))
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4],x[5]))

    search_frame =LabelFrame(main_frame,text="Search", pady="15")
    search_frame.pack(fill="x",padx="20")
    lb_test = Label(search_frame,text="Test Name")
    e_test = Entry(search_frame)
    bt_test = Button(search_frame,text="Search",command=search)
    lb_test.grid(row=0,column=0,padx="10",pady="10")
    bt_test.grid(row=0,column=2,padx="10",pady="10")
    e_test.grid(row=0,column=1,padx="15",pady="10")


    data_frame = LabelFrame(main_frame, text="Test",pady="15")
    data_frame.pack(fill="x", padx=20)

    # lb1 = Label(data_frame, text="Test ID")
    # lb1.grid(row=0, column=0, padx=10, pady=10)
    # e1 = Entry(data_frame)
    # e1.grid(row=0, column=1, padx=10, pady=10)

    lb2 = Label(data_frame, text="Test Name")
    lb2.grid(row=0, column=0, padx=10, pady=10)
    tname = Entry(data_frame)
    tname.grid(row=0, column=1, padx=10, pady=10)

    lb3 = Label(data_frame, text="Test Cost")
    lb3.grid(row=0, column=2, padx=10, pady=10)
    tcost = Entry(data_frame)
    tcost.grid(row=0, column=3, padx=10, pady=10)

    lb4 = Label(data_frame, text="Chemical Used")
    lb4.grid(row=1, column=0, padx=10, pady=10)
    tchem= Entry(data_frame)
    tchem.grid(row=1, column=1, padx=10, pady=10)
    lb5 = Label(data_frame, text="Equipment Used")
    lb5.grid(row=1, column=2, padx=10, pady=10)
    teq = Entry(data_frame)
    teq.grid(row=1, column=3, padx=10, pady=10)

    lb6 = Label(data_frame, text="Test Description")
    lb6.grid(row=2, column=0, padx=10, pady=10)
    tdesc = Entry(data_frame)
    tdesc.grid(row=2, column=1, padx=10, pady=10)
    
    def clear():
        tname.delete(0,END)
        tcost.delete(0,END)
        tchem.delete(0,END)
        teq.delete(0,END)
        tdesc.delete(0,END)

    def add():
        if tchem.get() == '' or tchem.get() == 'None 'and teq.get() == '' or teq.get() == 'None':
            cursor.execute("INSERT INTO Test(T_Name,T_Desc,T_Cost,T_C_ID,T_E_ID) VALUES (%s,%s,%s,%s,%s)", (tname.get(),tdesc.get(),tcost.get(),None,None))
        elif tchem.get() =='' or tchem.get() == 'None':
            cursor.execute("INSERT INTO Test (T_Name,T_Desc,T_Cost,T_C_ID,T_E_ID) VALUES (%s,%s,%s,%s,%s)", (tname.get(),tdesc.get(),tcost.get(),None,teq.get()))
        elif teq.get()=='' or teq.get() == 'None':
            cursor.execute("INSERT INTO Test (T_Name,T_Desc,T_Cost,T_C_ID,T_E_ID) VALUES (%s,%s,%s,%s,%s)", (tname.get(),tdesc.get(),tcost.get(),tchem.get(),None))
        else:
            cursor.execute("INSERT INTO Test (T_Name,T_Desc,T_Cost,T_C_ID,T_E_ID) VALUES (%s,%s,%s,%s,%s)", (tname.get(),tdesc.get(),tcost.get(),tchem.get(),teq.get()))
        db.commit()
        for child in tree.get_children():
            tree.delete(child)  
        cursor.execute("Select * from Test")
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4],x[5]))
        clear()
    
    def update():
        curItem = tree.focus()
        # tree.item(curItem,'values')[0])
        if tchem.get() == '' or tchem.get() == 'None 'and teq.get() == '' or teq.get() == 'None':
            cursor.execute("UPDATE Test SET T_Name=%s,T_Cost=%s,T_Desc=%s WHERE T_ID=%s",(tname.get(),tcost.get(),tdesc.get(),tree.item(curItem,'values')[0]))
        elif tchem.get() =='' or tchem.get() == 'None':
            cursor.execute("UPDATE Test SET T_Name=%s,T_Cost=%s,T_Desc=%s,T_E_ID=%s WHERE T_ID=%s",(tname.get(),tcost.get(),tdesc.get(),teq.get(),tree.item(curItem,'values')[0]))
        elif teq.get()=='' or teq.get() == 'None':
            cursor.execute("UPDATE Test SET T_Name=%s,T_Cost=%s,T_Desc=%s,T_C_ID=%s WHERE T_ID=%s",(tname.get(),tcost.get(),tdesc.get(),tchem.get(),tree.item(curItem,'values')[0]))
        else:
            cursor.execute("UPDATE Test SET T_Name=%s,T_Cost=%s,T_Desc=%s,T_C_ID=%s,T_E_ID=%s WHERE T_ID=%s",(tname.get(),tcost.get(),tdesc.get(),tchem.get(),teq.get(),tree.item(curItem,'values')[0]))
        db.commit()
        for child in tree.get_children():
            tree.delete(child)  
        cursor.execute("SELECT * FROM Test")
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4],x[5]))
        clear()


    def remove():
        curItem = tree.focus()
        # tree.item(curItem,'values')[0])
        cursor.execute("DELETE FROM Test where T_ID=%s", (tree.item(curItem,'values')[0],))
        db.commit()
        for child in tree.get_children():
            tree.delete(child)
        cursor.execute("SELECT * FROM Test")
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4],x[5]))
        clear()

    button_frame = LabelFrame(main_frame, text="Options",pady="15")
    button_frame.pack(fill="x", expand="yes", padx=20)

    b1 = Button(button_frame, text="Add Test",command=add)
    b1.grid(row=0, column=0, padx=10, pady=10)

    b2 = Button(button_frame, text="Update Values",command=update)
    b2.grid(row=0, column=1, padx=10, pady=10)

    b3 = Button(button_frame, text="Remove Test", command=remove)
    b3.grid(row=0, column=2, padx=10, pady=10)

    cursor.execute("SELECT * FROM Test")
    for x in cursor:
        tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4],x[5]))

    def selectItem(a):
            clear()
            curItem = tree.focus()
            tname.insert(0,tree.item(curItem,'values')[1])
            tcost.insert(0,tree.item(curItem,'values')[3])
            tdesc.insert(0,tree.item(curItem,'values')[2])
            tchem.insert(0,tree.item(curItem,'values')[4])
            teq.insert(0,tree.item(curItem,'values')[5])


    tree.bind('<ButtonRelease-1>', selectItem)

def Insurance(main_frame):
    deleteFrames(main_frame)
    style = ttk.Style()
    style.theme_use('default')

    style.configure("Treeview",
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3")

    style.map('Treeview',
    background=[('selected', "#347083")])
    f1 = Frame(main_frame)
    scroller = Scrollbar(f1)
    scroller.pack(side=RIGHT, fill=Y,pady="25")
    tree = ttk.Treeview(f1, yscrollcommand=scroller.set, selectmode="extended")
    tree.pack(pady="25")
    f1.pack()
    scroller.config(command=tree.yview)
    tree['columns'] = ("Insurance ID", "Name", "E-mail", "Phone")

    tree.column("#0", width=0, stretch=NO)
    tree.column("Insurance ID", anchor=CENTER, width=75)
    tree.column("Name", anchor=CENTER, width=150)
    tree.column("E-mail", anchor=CENTER, width=150)
    tree.column("Phone", anchor=CENTER, width=100)


    tree.heading("#0", text="", anchor=W)
    tree.heading("Insurance ID", text="Insurance ID", anchor=CENTER)
    tree.heading("Name", text="Name", anchor=CENTER)
    tree.heading("E-mail", text="E-mail", anchor=CENTER)
    tree.heading("Phone", text="Phone", anchor=CENTER)
    #tree.insert(parent='', index='end', iid=0, text='', values=("15","Test1","1500","dsfd", "dfdfd"))


    def search():
        for child in tree.get_children():
            tree.delete(child)  
        cursor.execute("SELECT * FROM InsuranceCompany WHERE I_Name = %s",(e_test.get(),))
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3]))

    search_frame =LabelFrame(main_frame,text="Search", pady="15")
    search_frame.pack(fill="x",padx="20")
    lb_test = Label(search_frame,text="Insurance Name")
    e_test = Entry(search_frame)
    bt_test = Button(search_frame,text="Search",command=search)
    lb_test.grid(row=0,column=0,padx="10",pady="10")
    bt_test.grid(row=0,column=2,padx="10",pady="10")
    e_test.grid(row=0,column=1,padx="15",pady="10")


    data_frame = LabelFrame(main_frame, text="Insurance Company",pady="15")
    data_frame.pack(fill="x", padx=20)

    lb2 = Label(data_frame, text="Name")
    lb2.grid(row=0, column=0, padx=10, pady=10)
    ename = Entry(data_frame)
    ename.grid(row=0, column=1, padx=10, pady=10)

    lb3 = Label(data_frame, text="E-mail")
    lb3.grid(row=0, column=2, padx=10, pady=10)
    eEmail = Entry(data_frame)
    eEmail.grid(row=0, column=3, padx=10, pady=10)

    lb6 = Label(data_frame, text="Phone")
    lb6.grid(row=0, column=4, padx=10, pady=10)
    ephon = Entry(data_frame)
    ephon.grid(row=0, column=5, padx=10, pady=10)



    def clear():
        ename.delete(0,END)
        eEmail.delete(0,END)
        ephon.delete(0,END)
    def add():

        cursor.execute("INSERT INTO InsuranceCompany (I_Name,I_Email,I_Phone) VALUES (%s,%s,%s)", (ename.get(), eEmail.get(),ephon.get()))
        db.commit()

        cursor.execute("SELECT * FROM InsuranceCompany")
        for child in tree.get_children():
            tree.delete(child) 
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3]))

        clear()
    
    def update():
        curItem = tree.focus()
        id = tree.item(curItem,'values')[0] 
        cursor.execute("UPDATE InsuranceCompany SET I_Name =%s, I_Email = %s, I_Phone=%s  WHERE I_ID=%s",(ename.get(),eEmail.get(),ephon.get(),id))
        db.commit()

        cursor.execute("SELECT * FROM InsuranceCompany")
        for child in tree.get_children():
            tree.delete(child)
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3]))
        clear()


    def remove():
        curItem = tree.focus()
        cursor.execute("DELETE FROM InsuranceCompany where I_ID=%s", (tree.item(curItem,'values')[0],))
        db.commit()

        for child in tree.get_children():
            tree.delete(child)
        cursor.execute("SELECT * FROM InsuranceCompany")
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3]))
        clear()

    button_frame = LabelFrame(main_frame, text="Options",pady="15")
    button_frame.pack(fill="x", expand="yes", padx=20)

    b1 = Button(button_frame, text="Add Insurance",command=add)
    b1.grid(row=0, column=0, padx=10, pady=10)

    b2 = Button(button_frame, text="Update Values",command=update)
    b2.grid(row=0, column=1, padx=10, pady=10)

    b3 = Button(button_frame, text="Remove Insurance",command=remove)
    b3.grid(row=0, column=2, padx=10, pady=10)

    cursor.execute("SELECT * FROM InsuranceCompany")
    for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3]))
    clear()
    def selectItem(a):
            clear()
            curItem = tree.focus()
            ename.insert(0,tree.item(curItem,'values')[1])
            eEmail.insert(0,tree.item(curItem,'values')[2])
            ephon.insert(0,tree.item(curItem,'values')[3])

    tree.bind('<ButtonRelease-1>', selectItem)

def TestBank(main_frame, * args):
    deleteFrames(main_frame)
    style = ttk.Style()
    style.theme_use('default')

    style.configure("Treeview",
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3")

    style.map('Treeview',
    background=[('selected', "#347083")])
    f1 = Frame(main_frame)
    scroller = Scrollbar(f1)
    scroller.pack(side=RIGHT, fill=Y,pady="25")
    tree = ttk.Treeview(f1, yscrollcommand=scroller.set, selectmode="extended")
    tree.pack(pady="25")
    f1.pack()
    scroller.config(command=tree.yview)
    tree['columns'] = ("Test Bank ID", "Test Name", "Patient Name", "Result", "Date","Payment ID", "Doctor")

    tree.column("#0", width=0, stretch=NO)
    tree.column("Test Bank ID", anchor=CENTER, width=75)
    tree.column("Test Name", anchor=CENTER, width=140)
    tree.column("Patient Name", anchor=CENTER, width=100)
    tree.column("Result", anchor=CENTER, width=140)
    tree.column("Date", anchor=CENTER, width=100)
    tree.column("Payment ID", anchor=CENTER, width=75)
    tree.column("Doctor", anchor=CENTER, width=140)


    tree.heading("#0", text="", anchor=W)
    tree.heading("Test Bank ID", text="Test Bank ID", anchor=CENTER)
    tree.heading("Test Name", text="Test Name", anchor=CENTER)
    tree.heading("Patient Name", text="Patient Name", anchor=CENTER)
    tree.heading("Result", text="Result", anchor=CENTER)
    tree.heading("Date", text="Date", anchor=CENTER)
    tree.heading("Payment ID", text="Payment ID", anchor=CENTER)
    tree.heading("Doctor", text="Doctor", anchor=CENTER)
    #tree.insert(parent='', index='end', iid=0, text='', values=("15","Test1","1500","dsfd", "dfdfd"))


    def search():
        field = option.get()
        if field == "Patient Name":         
            cursor.execute("select TB.TB_ID , T.T_Name , P.P_Name , TB.TB_Result , TB.TB_Date, TB.TB_Payment_ID, D.D_Name from TestBank TB, Patient P, Test T, Doctor D  where TB.TB_P_ID = P.P_ID and TB.TB_T_ID = T.T_ID AND TB.TB_D_ID = D.D_ID and P.P_Name = %s",(e_test.get(),) )
        elif field == "Test Name":
            cursor.execute("select TB.TB_ID , T.T_Name , P.P_Name , TB.TB_Result , TB.TB_Date, TB.TB_Payment_ID, D.D_Name from TestBank TB, Patient P, Test T, Doctor D  where TB.TB_P_ID = P.P_ID and TB.TB_T_ID = T.T_ID AND TB.TB_D_ID = D.D_ID and T.T_Name = %s",(e_test.get(),) )
        elif field == "Date":
            cursor.execute("select TB.TB_ID , T.T_Name , P.P_Name , TB.TB_Result , TB.TB_Date, TB.TB_Payment_ID, D.D_Name from TestBank TB, Patient P, Test T, Doctor D  where TB.TB_P_ID = P.P_ID and TB.TB_T_ID = T.T_ID AND TB.TB_D_ID = D.D_ID and TB.TB_Date = %s",(e_test.get(),) )
        elif field == "Doctor Name":
            cursor.execute("select TB.TB_ID , T.T_Name , P.P_Name , TB.TB_Result , TB.TB_Date, TB.TB_Payment_ID, D.D_Name from TestBank TB, Patient P, Test T, Doctor D  where TB.TB_P_ID = P.P_ID and TB.TB_T_ID = T.T_ID AND TB.TB_D_ID = D.D_ID and D.D_Name = %s",(e_test.get(),) )
        elif field == "Test Bank ID":
            cursor.execute("select TB.TB_ID , T.T_Name , P.P_Name , TB.TB_Result , TB.TB_Date, TB.TB_Payment_ID, D.D_Name from TestBank TB, Patient P, Test T, Doctor D  where TB.TB_P_ID = P.P_ID and TB.TB_T_ID = T.T_ID AND TB.TB_D_ID = D.D_ID and TB.TB_ID = %s",(e_test.get(),) )
        for child in tree.get_children():
            tree.delete(child)
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))


    search_frame =LabelFrame(main_frame,text="Search", pady="15")
    search_frame.pack(fill="x",padx="20")
    lb_test = Label(search_frame,text="Search Value")
    e_test = Entry(search_frame)
    bt_test = Button(search_frame,text="Search",command=search)
    lb_test.grid(row=0,column=0,padx="10",pady="10")
    bt_test.grid(row=0,column=4,padx="10",pady="10")
    e_test.grid(row=0,column=1,padx="15",pady="10")


    option = ttk.Combobox(search_frame, values=["Test Bank ID", "Test Name", "Patient Name","Date", "Doctor Name"])
    option.grid(row=0,column=3,padx=10,pady=10)
    option_lb = Label(search_frame,text="Search Metric")
    option_lb.grid(row=0,column=2,padx=10,pady=10)

    data_frame = LabelFrame(main_frame, text="Test",pady="15")
    data_frame.pack(fill="x", padx=20)

    lb2 = Label(data_frame, text="Test Name")
    lb2.grid(row=0, column=0, padx=10, pady=10)
    cursor.execute("SELECT T_Name FROM Test")
    options2=[]
    for x in cursor :
        options2.append(x[0]) 
    tbname = ttk.Combobox(data_frame,values=options2)
    
    tbname.grid(row=0, column=1, padx=10, pady=10)

    lb3 = Label(data_frame, text="Patient Name")
    lb3.grid(row=0, column=2, padx=10, pady=10)
    tbpat = Entry(data_frame)
    tbpat.grid(row=0, column=3, padx=10, pady=10)

    lb4 = Label(data_frame, text="Result")
    lb4.grid(row=1, column=0, padx=10, pady=10)
    tbresult = Entry(data_frame)
    tbresult.grid(row=1, column=1, padx=10, pady=10)
    lb5 = Label(data_frame, text="Date")
    lb5.grid(row=1, column=2, padx=10, pady=10)
    tbdate = Entry(data_frame)
    tbdate.grid(row=1, column=3, padx=10, pady=10)

    lb7 = Label(data_frame, text="Doctor")
    lb7.grid(row=2, column=0, padx=10, pady=10)
    cursor.execute("SELECT D_Name FROM Doctor")
    options=[]
    for x in cursor :
        options.append(x[0]) 
    tbdoc = ttk.Combobox(data_frame,values=options)
    tbdoc.grid(row=2, column=1, padx=10, pady=10)

    def fillTree():
        cursor.execute("select TB.TB_ID , T.T_Name , P.P_Name , TB.TB_Result , TB.TB_Date, TB.TB_Payment_ID, D.D_Name from TestBank TB, Patient P, Test T, Doctor D  where TB.TB_P_ID = P.P_ID and TB.TB_T_ID = T.T_ID AND TB.TB_D_ID = D.D_ID" )
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))
    def clear():
        tbname.delete(0,END)
        tbpat.delete(0,END)
        tbdoc.delete(0,END)
        tbresult.delete(0,END)
        tbdate.delete(0,END)
        e_test.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
    def add():
        cursor.execute("SELECT P_ID FROM Patient WHERE P_Name =%s",(tbpat.get(),))
        for row in cursor:
           pName=row[0]
        
        cursor.execute("SELECT D_ID FROM Doctor WHERE D_Name =%s",(tbdoc.get(),))
        for row in cursor:
            dName=row[0]
        cursor.execute("SELECT T_ID FROM Test WHERE T_Name =%s",(tbname.get(),))
        for row in cursor:
            tName=row[0]
        cursor.execute("INSERT INTO finances(P_Amount,P_Date) VALUES(%s,%s)", (0,date.today()))
        cursor.execute("select * from finances order by P_ID desc limit 1")
        for row in cursor:
            finID = row[0]
        cursor.execute("INSERT INTO TestBank(TB_T_ID,TB_P_ID,TB_Result,TB_Date,TB_Payment_ID,TB_D_ID) VALUES (%s,%s,%s,%s,%s,%s)", (tName,pName,tbresult.get(),tbdate.get(),finID,dName))
        db.commit()
        for child in tree.get_children():
            tree.delete(child) 
        fillTree()
        clear()
    
    def remove():
        curItem = tree.focus()
        cursor.execute("DELETE FROM TestBank where TB_ID=%s", (tree.item(curItem,'values')[0],))
        db.commit()
        for child in tree.get_children():
            tree.delete(child)
        fillTree()
        clear()
    def countTests():
        cursor.execute("SELECT COUNT(*) FROM TestBank where TB_Date = %s",(str(date.today()),))
        for x in cursor:
            e5.insert(0,x[0])

    def countCost():
        cursor.execute("SELECT SUM(T.T_Cost) FROM TestBank TB , Test T WHERE TB.TB_T_ID = T.T_ID and TB.TB_Date = %s", (str(date.today()),))
        for x in cursor:
            e6.insert(0,x[0])

    button_frame = LabelFrame(main_frame, text="Options",pady="15")
    button_frame.pack(fill="x", expand="yes", padx=20)

    b1 = Button(button_frame, text="Add Test",command=add)
    b1.grid(row=0, column=0, padx=10, pady=10)

    b3 = Button(button_frame, text="Remove Test",command=remove)
    b3.grid(row=0, column=1, padx=10, pady=10)

    b4 = Button(button_frame,text="Make Payment", command= lambda : fins(main_frame,tree.item(tree.focus(),'values')[5]))
    b4.grid(row=0,column=2,padx=20,pady=10)


    b5 = Button(button_frame,text="# Of Tests", command=countTests)
    e5 = Entry(button_frame)

    b5.grid(row=1, column=0,padx=10,pady=10)
    e5.grid(row=1, column=1,padx=10,pady=10)
    
    b6 = Button(button_frame,text="Total Cost", command=countCost)
    e6 = Entry(button_frame)

    b6.grid(row=1, column=2,padx=10,pady=10)
    e6.grid(row=1, column=3,padx=10,pady=10)

    fillTree()
    if args:
        tbpat.insert(0,args[0])
        tbdate.insert(0,date.today())
    def selectItem(a):
            clear()
            curItem = tree.focus()
            tbname.insert(0,tree.item(curItem,'values')[1])
            tbpat.insert(0,tree.item(curItem,'values')[2])
            tbresult.insert(0,tree.item(curItem,'values')[3])
            tbdate.insert(0,tree.item(curItem,'values')[4])
            tbdoc.insert(0,tree.item(curItem,'values')[6])


    tree.bind('<ButtonRelease-1>', selectItem)

def Chemical(main_frame):
    deleteFrames(main_frame)
    style = ttk.Style()
    style.theme_use('default')

    style.configure("Treeview",
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3")

    style.map('Treeview',
    background=[('selected', "#347083")])
    f1 = Frame(main_frame)
    scroller = Scrollbar(f1)
    scroller.pack(side=RIGHT, fill=Y,pady="25")
    tree = ttk.Treeview(f1, yscrollcommand=scroller.set, selectmode="extended")
    tree.pack(pady="25")
    f1.pack()
    scroller.config(command=tree.yview)
    tree['columns'] = ("Chemical ID", "Name", "Cost", "Produced", "Expires", "Supplier")

    tree.column("#0", width=0, stretch=NO)
    tree.column("Chemical ID", anchor=CENTER, width=75)
    tree.column("Name", anchor=CENTER, width=150)
    tree.column("Cost", anchor=CENTER, width=150)
    tree.column("Produced", anchor=CENTER, width=100)
    tree.column("Expires", anchor=CENTER, width=100)
    tree.column("Supplier", anchor=CENTER, width=100)

    tree.heading("#0", text="", anchor=W)
    tree.heading("Chemical ID", text="Chemical ID", anchor=CENTER)
    tree.heading("Name", text="Name", anchor=CENTER)
    tree.heading("Cost", text="Cost", anchor=CENTER)
    tree.heading("Produced", text="Produced", anchor=CENTER)
    tree.heading("Expires", text="Expires", anchor=CENTER)
    tree.heading("Supplier", text="Supplier", anchor=CENTER)
    #tree.insert(parent='', index='end', iid=0, text='', values=("15","Test1","1500","dsfd", "dfdfd"))

    def search():
        field = e_test1.get()
        if field == "Chemical Name":
            for child in tree.get_children():
                tree.delete(child) 
            # TB_P_ID
            cursor.execute("SELECT * FROM Chemical WHERE C_Name = %s",(e_test.get(),))
            for x in cursor:
                tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4],x[5]))

        elif field == "Date Expiers":
            for child in tree.get_children():
                tree.delete(child) 
             # TB_P_ID
            cursor.execute("SELECT * FROM Chemical WHERE C_Expire = %s",(e_test.get(),))
            for x in cursor:
                tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4],x[5]))

    search_frame =LabelFrame(main_frame,text="Search", pady="15")
    search_frame.pack(fill="x",padx="20")
    lb_test = Label(search_frame,text="Search Value")
    e_test = Entry(search_frame)
    lb_test1 = Label(search_frame,text="Search metrics")
    options = ["Chemical Name","Date Expiers"]
    e_test1 = ttk.Combobox(search_frame,values=options)
    e_test1.current(0)
    bt_test = Button(search_frame,text="Search",command=search)
    lb_test.grid(row=0,column=0,padx="10",pady="10")
    bt_test.grid(row=0,column=4,padx="10",pady="10")
    e_test.grid(row=0,column=1,padx="15",pady="10")
    lb_test1.grid(row=0,column=2,padx="10",pady="10")
    e_test1.grid(row=0,column=3,padx="10",pady="10")


    data_frame = LabelFrame(main_frame, text="Chemical",pady="15")
    data_frame.pack(fill="x", padx=20)

    lb2 = Label(data_frame, text="Name")
    lb2.grid(row=0, column=0, padx=10, pady=10)
    ename = Entry(data_frame)
    ename.grid(row=0, column=1, padx=10, pady=10)

    lb3 = Label(data_frame, text="Cost")
    lb3.grid(row=0, column=2, padx=10, pady=10)
    ecost = Entry(data_frame)
    ecost.grid(row=0, column=3, padx=10, pady=10)

    lb4 = Label(data_frame, text="Produced")
    lb4.grid(row=0, column=4, padx=10, pady=10)
    eproduced = Entry(data_frame)
    eproduced.grid(row=0, column=5, padx=10, pady=10)
    lb5 = Label(data_frame, text="Expires")
    lb5.grid(row=1, column=0, padx=10, pady=10)
    eExpires = Entry(data_frame)
    eExpires.grid(row=1, column=1, padx=10, pady=10)

    lb6 = Label(data_frame, text="Supplier")
    lb6.grid(row=1, column=2, padx=10, pady=10)
    cursor.execute("SELECT S_Name FROM Supplier")
    options=[]
    for x in cursor :
        options.append(x[0]) 
    eSupplier = ttk.Combobox(data_frame,values=options)
    eSupplier.grid(row=1, column=3, padx=10, pady=10)
    #eSupplier.current(0)

    def clear():
        ename.delete(0,END)
        ecost.delete(0,END)
        eproduced.delete(0,END)
        eExpires.delete(0,END)
        eSupplier.delete(0,END)

    def FillTree():
        cursor.execute("SELECT C.C_ID,C.C_Name,C.C_Cost,C.C_Prod,C.C_Expire,S.S_Name FROM Chemical C , SUPPLIER S WHERE C.S_ID = S.S_ID ")
        for child in tree.get_children():
            tree.delete(child) 
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4],x[5]))

    def add():       
        cursor.execute("SELECT S_ID FROM Supplier WHERE S_Name = %s",(eSupplier.get(),))
        for x in cursor:
            a=x[0]
        cursor.execute("INSERT INTO Chemical (C_Name,C_Cost,C_Prod,C_Expire,S_ID) VALUES (%s,%s,%s,%s,%s)", (ename.get(),ecost.get(),eproduced.get(),eExpires.get(),a))
        db.commit()

        FillTree()

        clear()
    
    def update():
        curItem = tree.focus()
        id = tree.item(curItem,'values')[0] 
        cursor.execute("UPDATE Chemical SET C_Name = %s, C_Cost = %s , C_Prod =%s, C_Expire = %s WHERE C_ID=%s",(ename.get(),ecost.get(),eproduced.get(),eExpires.get(),id))
        db.commit()

        FillTree()

        clear()

    def remove():
        curItem = tree.focus()
        cursor.execute("DELETE FROM Chemical where C_ID=%s", (tree.item(curItem,'values')[0],))
        db.commit()
        
        FillTree()
        clear()

    button_frame = LabelFrame(main_frame, text="Options",pady="15")
    button_frame.pack(fill="x", expand="yes", padx=20)

    b1 = Button(button_frame, text="Add Chemical",command=add)
    b1.grid(row=0, column=0, padx=10, pady=10)

    b2 = Button(button_frame, text="Update Values",command=update)
    b2.grid(row=0, column=1, padx=10, pady=10)

    b3 = Button(button_frame, text="Remove Chemical",command=remove)
    b3.grid(row=0, column=2, padx=10, pady=10)
    FillTree()
    clear()
    def selectItem(a):
            clear()
            curItem = tree.focus()
            ename.insert(0,tree.item(curItem,'values')[1])
            ecost.insert(0,tree.item(curItem,'values')[2])
            eproduced.insert(0,tree.item(curItem,'values')[3])
            eExpires.insert(0,tree.item(curItem,'values')[4])
            eSupplier.insert(0,tree.item(curItem,'values')[5])

    tree.bind('<ButtonRelease-1>', selectItem)

def Maintenance(main_frame):
    deleteFrames(main_frame)
    style = ttk.Style()
    style.theme_use('default')

    style.configure("Treeview",
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3")

    style.map('Treeview',
    background=[('selected', "#347083")])
    f1 = Frame(main_frame)
    scroller = Scrollbar(f1)
    scroller.pack(side=RIGHT, fill=Y,pady="25")
    tree = ttk.Treeview(f1, yscrollcommand=scroller.set, selectmode="extended")
    tree.pack(pady="25")
    f1.pack()
    scroller.config(command=tree.yview)
    tree['columns'] = ("Maintenance ID", "Name", "Phone", "E-mail")

    tree.column("#0", width=0, stretch=NO)
    tree.column("Maintenance ID", anchor=CENTER, width=100)
    tree.column("Name", anchor=CENTER, width=150)
    tree.column("Phone", anchor=CENTER, width=150)
    tree.column("E-mail", anchor=CENTER, width=100)


    tree.heading("#0", text="", anchor=W)
    tree.heading("Maintenance ID", text="Maintenance ID", anchor=CENTER)
    tree.heading("Name", text="Name", anchor=CENTER)
    tree.heading("Phone", text="Phone", anchor=CENTER)
    tree.heading("E-mail", text="E-mail", anchor=CENTER)

    def search():
        for child in tree.get_children():
            tree.delete(child)  
        cursor.execute("SELECT * FROM Maintenance WHERE M_Name = %s",(e_test.get(),))
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3]))


    search_frame =LabelFrame(main_frame,text="Search", pady="15")
    search_frame.pack(fill="x",padx="20")
    lb_test = Label(search_frame,text="Maintenance Name")
    e_test = Entry(search_frame)
    bt_test = Button(search_frame,text="Search",command=search)
    lb_test.grid(row=0,column=0,padx="10",pady="10")
    bt_test.grid(row=0,column=2,padx="10",pady="10")
    e_test.grid(row=0,column=1,padx="15",pady="10")


    data_frame = LabelFrame(main_frame, text="Maintenance Company",pady="15")
    data_frame.pack(fill="x", padx=20)

    #lb1 = Label(data_frame, text="Maintenance ID")
    #lb1.grid(row=0, column=0, padx=10, pady=10)
    #e1 = Entry(data_frame)
    #e1.grid(row=0, column=1, padx=10, pady=10)

    lb2 = Label(data_frame, text="Name")
    lb2.grid(row=0, column=0, padx=10, pady=10)
    mname = Entry(data_frame)
    mname.grid(row=0, column=1, padx=10, pady=10)

    lb3 = Label(data_frame, text="Phone")
    lb3.grid(row=0, column=2, padx=10, pady=10)
    mphone = Entry(data_frame)
    mphone.grid(row=0, column=3, padx=10, pady=10)

    lb4 = Label(data_frame, text="E-mail")
    lb4.grid(row=1, column=0, padx=10, pady=10)
    memail = Entry(data_frame)
    memail.grid(row=1, column=1, padx=10, pady=10)
    
    def clear():
        mname.delete(0,END)
        mphone.delete(0,END)
        memail.delete(0,END)
    def add():
        cursor.execute("INSERT INTO Maintenance(M_Name,M_Phone,M_Email) VALUES (%s,%s,%s)", (mname.get(), mphone.get(),memail.get()))
        db.commit()
        for child in tree.get_children():
            tree.delete(child)
        cursor.execute("SELECT * FROM MAINTENANCE")
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3]))
        clear()
    
    def update():
        curItem = tree.focus()
        cursor.execute("UPDATE Maintenance SET M_Name=%s,M_Email=%s,M_Phone=%s WHERE M_ID=%s",(mname.get(),memail.get(),mphone.get(),tree.item(curItem,'values')[0]))
        db.commit()
        cursor.execute("SELECT * FROM Maintenance")
        for child in tree.get_children():
            tree.delete(child)  
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3]))
        clear()


    def remove():
        curItem = tree.focus()
        cursor.execute("DELETE FROM Maintenance where M_ID=%s", (tree.item(curItem,'values')[0],))
        db.commit()
        for child in tree.get_children():
            tree.delete(child)
        cursor.execute("SELECT * FROM Maintenance")
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3]))
        clear()

    button_frame = LabelFrame(main_frame, text="Options",pady="15")
    button_frame.pack(fill="x", expand="yes", padx=20)

    b1 = Button(button_frame, text="Add Maintenance",command=add)
    b1.grid(row=0, column=0, padx=10, pady=10)

    b2 = Button(button_frame, text="Update Values",command=update)
    b2.grid(row=0, column=1, padx=10, pady=10)

    b3 = Button(button_frame, text="Remove Maintenance", command=remove)
    b3.grid(row=0, column=2, padx=10, pady=10)

    cursor.execute("SELECT * FROM Maintenance")
    for x in cursor:
        tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3]))

    def selectItem(a):
            clear()
            curItem = tree.focus()
            mname.insert(0,tree.item(curItem,'values')[1])
            mphone.insert(0,tree.item(curItem,'values')[2])
            memail.insert(0,tree.item(curItem,'values')[3])

    tree.bind('<ButtonRelease-1>', selectItem)

def Equipment(main_frame):

    deleteFrames(main_frame)
    list=[]
    cursor.execute("SELECT M_Name FROM  Maintenance")  
    print('Alaa')
    for x in cursor:
      list.append(x[0])

    style = ttk.Style()
    style.theme_use('default')

    style.configure("Treeview",
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3")

    style.map('Treeview',
    background=[('selected', "#347083")])
    f1 = Frame(main_frame)
    scroller = Scrollbar(f1)
    scroller.pack(side=RIGHT, fill=Y,pady="25")
    tree = ttk.Treeview(f1, yscrollcommand=scroller.set, selectmode="extended")
    tree.pack(pady="25")
    f1.pack()
    scroller.config(command=tree.yview)
    tree['columns'] = ("Equipment ID", "Name","Guide","Producer E-mail",  "Maintenance")

    tree.column("#0", width=0, stretch=NO)
    tree.column("Equipment ID", anchor=CENTER, width=75)
    tree.column("Name", anchor=CENTER, width=150)
    tree.column("Guide", anchor=CENTER, width=150)
    tree.column("Producer E-mail", anchor=CENTER, width=100)
    tree.column("Maintenance", anchor=CENTER, width=100)

    tree.heading("#0", text="", anchor=W)
    tree.heading("Equipment ID", text="Equipment ID", anchor=CENTER)
    tree.heading("Name", text="Name", anchor=CENTER)
    tree.heading("Guide", text="Guide", anchor=CENTER)
    tree.heading("Producer E-mail", text="Producer E-mail", anchor=CENTER)
    tree.heading("Maintenance", text="Maintenance", anchor=CENTER)

    def search():
        for child in tree.get_children():
            tree.delete(child)  
        cursor.execute("SELECT E.E_ID,E.E_Name, E.E_Desc, E.P_Email, M.M_Name FROM Equipment E , Maintenance M WHERE E.M_ID = M.M_ID and E.E_Name = %s",(e_test.get(),))
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4]))

    search_frame =LabelFrame(main_frame,text="Search", pady="15")
    search_frame.pack(fill="x",padx="20")
    lb_test = Label(search_frame,text="Equipment Name")
    e_test = Entry(search_frame)
    bt_test = Button(search_frame,text="Search",command=search)
    lb_test.grid(row=0,column=0,padx="10",pady="10")
    bt_test.grid(row=0,column=2,padx="10",pady="10")
    e_test.grid(row=0,column=1,padx="15",pady="10")


    data_frame = LabelFrame(main_frame, text="Equipment",pady="15")
    data_frame.pack(fill="x", padx=20)

    lb2 = Label(data_frame, text="Name")
    lb2.grid(row=0, column=0, padx=10, pady=10)
    ename = Entry(data_frame)
    ename.grid(row=0, column=1, padx=10, pady=10)

    lb11 = Label(data_frame,text="Guide")
    eguide = Entry(data_frame)
    lb11.grid(row=0,column=2,padx=10,pady=10)
    eguide.grid(row=0,column=3,padx=10,pady=10)

    lb4 = Label(data_frame, text="Producer E-mail")
    lb4.grid(row=1, column=0, padx=10, pady=10)
    eemail = Entry(data_frame)
    eemail.grid(row=1, column=1, padx=10, pady=10)
    
    lb6 = Label(data_frame, text="Maintenance name")
    lb6.grid(row=1, column=2, padx=10, pady=10)
    
    comboList=[]
    cursor.execute("SELECT M_Name from  Maintenance")
    for n in cursor:
            print(n)
            comboList.append(n)
    
    emain = ttk.Combobox(data_frame,values=comboList)
    emain.grid(row=1, column=3, padx=10, pady=10)
    def clear():
        ename.delete(0,END)
        eemail.delete(0,END)
        eguide.delete(0,END)
        emain.delete(0,END)
    def fillTree():
        cursor.execute("SELECT E.E_ID,E.E_Name, E.E_Desc, E.P_Email, M.M_Name FROM Equipment E , Maintenance M WHERE E.M_ID = M.M_ID ")
        for child in tree.get_children():
            tree.delete(child) 
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4]))


    def add():
        cursor.execute("SELECT M_ID from Maintenance where M_Name=%s", (emain.get(),))
        for x in cursor:
            M_id = x[0]
        cursor.execute("INSERT INTO Equipment (E_Name,E_Desc,P_Email,M_ID) VALUES (%s,%s,%s,%s)", (ename.get(),eguide.get(),eemail.get(),M_id))
        db.commit()
        fillTree()
        clear()
    
    def update():
        cursor.execute("SELECT M_ID from Maintenance Where M_Name = %s", (emain.get(),))
        for x in cursor:
            new_id = x[0]
        cursor.execute("UPDATE Equipment SET E_Name=%s,E_Desc = %s , P_Email=%s, M_ID=%s WHERE E_ID=%s",(ename.get(),eguide.get(),eemail.get(),new_id,tree.item(tree.focus(),'values')[0]))
        db.commit()
        fillTree()
        clear()


    def remove():
        cursor.execute("DELETE FROM Equipment where E_ID=%s", (tree.item(tree.focus(),'values')[0],))
        db.commit()
        fillTree()
        clear()

    button_frame = LabelFrame(main_frame, text="Options",pady="15")
    button_frame.pack(fill="x", expand="yes", padx=20)

    b1 = Button(button_frame, text="Add Equipment",command=add)
    b1.grid(row=0, column=0, padx=10, pady=10)

    b2 = Button(button_frame, text="Update Values",command=update)
    b2.grid(row=0, column=1, padx=10, pady=10)

    b3 = Button(button_frame, text="Remove Equipment", command=remove)
    b3.grid(row=0, column=2, padx=10, pady=10)
    fillTree()
    clear()
    def selectItem(a):
            clear()
            curItem = tree.focus()
            ename.insert(0,tree.item(curItem,'values')[1])
            eguide.insert(0,tree.item(curItem,'values')[2])
            eemail.insert(0,tree.item(curItem,'values')[3])
            emain.insert(0,tree.item(curItem,'values')[4])

    tree.bind('<ButtonRelease-1>', selectItem)

def Employee(main_frame):
    deleteFrames(main_frame)
    style = ttk.Style()
    style.theme_use('default')

    style.configure("Treeview",
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3")

    style.map('Treeview',
    background=[('selected', "#347083")])
    f1 = Frame(main_frame)
    scroller = Scrollbar(f1)
    scroller.pack(side=RIGHT, fill=Y,pady="25")
    tree = ttk.Treeview(f1, yscrollcommand=scroller.set, selectmode="extended")
    tree.pack(pady="25")
    f1.pack()
    scroller.config(command=tree.yview)
    tree['columns'] = ("Employee ID", "Name", "Type", "Salary", "E-mail", "Phone", "Payment ID")

    tree.column("#0", width=0, stretch=NO)
    tree.column("Employee ID", anchor=CENTER, width=75)
    tree.column("Name", anchor=CENTER, width=150)
    tree.column("Type", anchor=CENTER, width=150)
    tree.column("Salary", anchor=CENTER, width=100)
    tree.column("E-mail", anchor=CENTER, width=100)
    tree.column("Phone", anchor=CENTER, width=100)
    tree.column("Payment ID", anchor=CENTER, width=100)

    tree.heading("#0", text="", anchor=W)
    tree.heading("Employee ID", text="Employee ID", anchor=CENTER)
    tree.heading("Name", text="Name", anchor=CENTER)
    tree.heading("Type", text="Type", anchor=CENTER)
    tree.heading("Salary", text="Salary", anchor=CENTER)
    tree.heading("E-mail", text="E-mail", anchor=CENTER)
    tree.heading("Phone", text="Phone", anchor=CENTER)
    tree.heading("Payment ID", text="Payment ID", anchor=CENTER)
    
    def search():
        for child in tree.get_children():
            tree.delete(child) 
        cursor.execute("SELECT * FROM Employee WHERE E_Name = %s",(e_test.get(),))
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))

    search_frame =LabelFrame(main_frame,text="Search", pady="15")
    search_frame.pack(fill="x",padx="20")
    lb_test = Label(search_frame,text="Employee Name")
    e_test = Entry(search_frame)
    bt_test = Button(search_frame,text="Search",command=search)
    lb_test.grid(row=0,column=0,padx="10",pady="10")
    bt_test.grid(row=0,column=2,padx="10",pady="10")
    e_test.grid(row=0,column=1,padx="15",pady="10")


    data_frame = LabelFrame(main_frame, text="Employee",pady="15")
    data_frame.pack(fill="x", padx=20)

    lb2 = Label(data_frame, text="Name")
    lb2.grid(row=0, column=0, padx=10, pady=10)
    ename = Entry(data_frame)
    ename.grid(row=0, column=1, padx=10, pady=10)

    lb3 = Label(data_frame, text="Type")
    lb3.grid(row=0, column=2, padx=10, pady=10)
    options = ["Manager","Laboratory Doctor","Nurse","Receptionist"]
    etype = ttk.Combobox(data_frame,values=options)
    etype.current(0)
    etype.grid(row=0, column=3, padx=10, pady=10)

    lb4 = Label(data_frame, text="Salary")
    lb4.grid(row=0, column=4, padx=10, pady=10)
    esalary= Entry(data_frame)
    esalary.grid(row=0, column=5, padx=10, pady=10)
    lb5 = Label(data_frame, text="E-mail")
    lb5.grid(row=1, column=0, padx=10, pady=10)
    eemail = Entry(data_frame)
    eemail.grid(row=1, column=1, padx=10, pady=10)

    lb6 = Label(data_frame, text="Phone")
    lb6.grid(row=1, column=2, padx=10, pady=10)
    ephone = Entry(data_frame)
    ephone.grid(row=1, column=3, padx=10, pady=10)
    
    def clear():
        ename.delete(0,END)
        etype.delete(0,END)
        ephone.delete(0,END)
        eemail.delete(0,END)
        esalary.delete(0,END)
        eNum.delete(0,END)
        eTotalS.delete(0,END)
        e0.delete(0,END)
        e00.delete(0,END)
        e000.delete(0,END)
        e0000.delete(0,END)

    def add():
        cursor.execute("INSERT INTO finances(P_Amount,P_Date) VALUES(%s,%s)", (0,'14/1/2022'))
        cursor.execute("select * from finances order by P_ID desc limit 1")
        for row in cursor:
            finID = row[0]
        
        cursor.execute("INSERT INTO Employee (E_Name,E_Type,E_Salary ,E_Email,E_Phone,E_P_ID) VALUES (%s,%s,%s,%s,%s,%s)", (ename.get(),etype.get(),esalary.get(),eemail.get(),ephone.get(),finID))
        db.commit()


        cursor.execute("SELECT * FROM Employee")
        for child in tree.get_children():
            tree.delete(child) 
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))

        clear()
    
    def update():
        curItem = tree.focus()
        id = tree.item(curItem,'values')[0]
        cursor.execute("UPDATE Employee SET E_Name = %s, E_Type = %s , E_Salary =%s, E_Email = %s, E_Phone = %s WHERE E_ID=%s",(ename.get(),etype.get(),esalary.get(),eemail.get(),ephone.get(),id))
        db.commit()
        cursor.execute("SELECT * FROM Employee")
        for child in tree.get_children():
            tree.delete(child)  
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))
        clear()

    def remove():
        curItem = tree.focus()
        cursor.execute("DELETE FROM Employee where E_ID=%s", (tree.item(curItem,'values')[0],))
        db.commit()
        for child in tree.get_children():
            tree.delete(child)
        cursor.execute("SELECT * FROM Employee")
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))
        clear()
    
    def NumOFE():
        clear()
        cursor.execute("SELECT COUNT(*) FROM Employee")
        for x in cursor:
            eNum.insert(0,x[0])

    def CallculateSalary():
        clear()
        cursor.execute("SELECT SUM(E_Salary) FROM Employee")
        for x in cursor:
            eTotalS.insert(0,x[0])
    
    def avrege():
        clear()
        myDict = {}
        cursor.execute("SELECT E_Type,AVG(E_Salary) from Employee GROUP BY E_Type")
        for x in cursor:
            myDict[x[0]] = x[1]
        if "Manager" in myDict:
            e0.insert(0,int(myDict["Manager"]))
        else :
            e0.insert(0,"0")
        
        if "Laboratory Doctor" in myDict:
            e00.insert(0,int(myDict["Laboratory Doctor"]))
        else :
            e00.insert(0,"0")

        if "Nurse" in myDict:
            e000.insert(0,int(myDict["Nurse"]))
        else :
            e000.insert(0,"0")

        if "Receptionist" in myDict:
            e0000.insert(0,int(myDict["Receptionist"]))
        else :
            e0000.insert(0,"0") 

    button_frame = LabelFrame(main_frame, text="Options",pady="15")
    button_frame.pack(fill="x", expand="yes", padx=20)

    b1 = Button(button_frame, text="Add Employee",command=add)
    b1.grid(row=0, column=0, padx=10, pady=10)

    b2 = Button(button_frame, text="Update Values",command=update)
    b2.grid(row=0, column=1, padx=10, pady=10)

    b3 = Button(button_frame, text="Remove Employee",command=remove)
    b3.grid(row=0, column=2, padx=10, pady=10)

    b4 = Button(button_frame,text="Number of Employee",command=NumOFE)
    b4.grid(row=1, column=0, padx=10, pady=10)

    eNum = Entry(button_frame)
    eNum.grid(row=1, column=1, padx=10, pady=10)

    b5 = Button(button_frame,text="Compute All Salary",command=CallculateSalary)
    b5.grid(row=1, column=2, padx=10, pady=10)

    eTotalS = Entry(button_frame)
    eTotalS.grid(row=1, column=3, padx=10, pady=10)

    b6 = Button(button_frame,text="avrege for every group by type",command=avrege)
    b6.grid(row=1, column=4, padx=10, pady=10)

    lb7 = Label(button_frame, text="avrege for type(Manager):")
    lb7.grid(row=2, column=0, padx=10, pady=10)
    e0 = Entry(button_frame)
    e0.grid(row=2, column=1, padx=10, pady=10)

    lb8 = Label(button_frame, text="avrege for type(Laboratory Doctor):")
    lb8.grid(row=2, column=2, padx=10, pady=10)
    e00 = Entry(button_frame)
    e00.grid(row=2, column=3, padx=10, pady=10)

    lb9 = Label(button_frame, text="avrege for type(Nurse):")
    lb9.grid(row=3, column=0, padx=10, pady=10)
    e000 = Entry(button_frame)
    e000.grid(row=3, column=1, padx=10, pady=10)

    lb10 = Label(button_frame, text="avrege for type(Receptionist):")
    lb10.grid(row=3, column=2, padx=10, pady=10)
    e0000 = Entry(button_frame)
    e0000.grid(row=3, column=3, padx=10, pady=10)

    cursor.execute("SELECT * FROM Employee")
    for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))
    clear()

    def selectItem(a):
            clear()
            curItem = tree.focus()
            #e1.insert(0,tree.item(curItem,'values')[0])
            ename.insert(0,tree.item(curItem,'values')[1])
            etype.insert(0,tree.item(curItem,'values')[2])
            esalary.insert(0,tree.item(curItem,'values')[3])
            eemail.insert(0,tree.item(curItem,'values')[4])
            ephone.insert(0,tree.item(curItem,'values')[5])
            #e7.insert(0,tree.item(curItem,'values')[6])
    tree.bind('<ButtonRelease-1>', selectItem)

def Doctor(main_frame):
    deleteFrames(main_frame)
    style = ttk.Style()
    style.theme_use('default')

    style.configure("Treeview",
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3")

    style.map('Treeview',
    background=[('selected', "#347083")])
    f1 = Frame(main_frame)
    scroller = Scrollbar(f1)
    scroller.pack(side=RIGHT, fill=Y,pady="25")
    tree = ttk.Treeview(f1, yscrollcommand=scroller.set, selectmode="extended")
    tree.pack(pady="25")
    f1.pack()
    scroller.config(command=tree.yview)
    tree['columns'] = ("Doctor ID", "Name", "Type", "Phone", "E-mail")

    tree.column("#0", width=0, stretch=NO)
    tree.column("Doctor ID", anchor=CENTER, width=75)
    tree.column("Name", anchor=CENTER, width=150)
    tree.column("Type", anchor=CENTER, width=150)
    tree.column("Phone", anchor=CENTER, width=100)
    tree.column("E-mail", anchor=CENTER, width=100)


    tree.heading("#0", text="", anchor=W)
    tree.heading("Doctor ID", text="Doctor ID", anchor=CENTER)
    tree.heading("Name", text="Name", anchor=CENTER)
    tree.heading("Type", text="Type", anchor=CENTER)
    tree.heading("Phone", text="Phone", anchor=CENTER)
    tree.heading("E-mail", text="E-mail", anchor=CENTER)

    def search():
        for child in tree.get_children():
            tree.delete(child)  
        cursor.execute("SELECT * FROM Doctor WHERE D_Name = %s",(e_test.get(),))
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4]))

    
    search_frame =LabelFrame(main_frame,text="Search", pady="15")
    search_frame.pack(fill="x",padx="20")
    lb_test = Label(search_frame,text="Doctor Name")
    e_test = Entry(search_frame)
    bt_test = Button(search_frame,text="Search",command=search)
    lb_test.grid(row=0,column=0,padx="10",pady="10")
    bt_test.grid(row=0,column=2,padx="10",pady="10")
    e_test.grid(row=0,column=1,padx="15",pady="10")


    data_frame = LabelFrame(main_frame, text="Doctor",pady="15")
    data_frame.pack(fill="x", padx=20)

    lb2 = Label(data_frame, text="Name")
    lb2.grid(row=0, column=0, padx=10, pady=10)
    dname = Entry(data_frame)
    dname.grid(row=0, column=1, padx=10, pady=10)

    lb3 = Label(data_frame, text="Type")
    lb3.grid(row=0, column=2, padx=10, pady=10)
    dtype = Entry(data_frame)
    dtype.grid(row=0, column=3, padx=10, pady=10)

    lb4 = Label(data_frame, text="Phone")
    lb4.grid(row=1, column=0, padx=10, pady=10)
    dphone = Entry(data_frame)
    dphone.grid(row=1, column=1, padx=10, pady=10)
    lb5 = Label(data_frame, text="E-mail")
    lb5.grid(row=1, column=2, padx=10, pady=10)
    demail = Entry(data_frame)
    demail.grid(row=1, column=3, padx=10, pady=10)
    def clear():
        dname.delete(0,END)
        demail.delete(0,END)
        dtype.delete(0,END)
        dphone.delete(0,END)
        e_Num.delete(0,END)

    def add():
        cursor.execute("INSERT INTO Doctor (D_Name,D_Specialty,D_Email,D_Phone) VALUES (%s,%s,%s,%s)", (dname.get(),dtype.get(),demail.get(),dphone.get()))
        db.commit()
        clear()
        for child in tree.get_children():
            tree.delete(child) 
        cursor.execute("SELECT * FROM Doctor")
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4]))
    
    def update():
        curItem = tree.focus()     
        cursor.execute("UPDATE Doctor SET D_Name=%s,D_Specialty=%s,D_Email=%s,D_Phone=%s WHERE D_ID=%s",(dname.get(),dtype.get(),demail.get(),dphone.get(),tree.item(curItem,'values')[0]))
        db.commit()
        for child in tree.get_children():
            tree.delete(child)  
        cursor.execute("SELECT * FROM Doctor")
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4]))
        clear()


    def remove():
        curItem = tree.focus()
        cursor.execute("DELETE FROM Doctor where D_ID=%s", (tree.item(curItem,'values')[0],))
        db.commit()
        for child in tree.get_children():
            tree.delete(child)
        cursor.execute("SELECT * FROM Doctor")
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4]))
        clear()

    def NumOfTest():
        clear()
        id = tree.item(tree.focus(),'values')[0]
        cursor.execute("SELECT COUNT(*) FROM TestBank where TB_D_ID =  %s ", (id,) )
        for x in cursor:
            e_Num.insert(0,x[0])

    button_frame = LabelFrame(main_frame, text="Options",pady="15")
    button_frame.pack(fill="x", expand="yes", padx=20)

    b1 = Button(button_frame, text="Add Doctor",command=add)
    b1.grid(row=0, column=0, padx=10, pady=10)

    b2 = Button(button_frame, text="Update Values",command=update)
    b2.grid(row=0, column=1, padx=10, pady=10)

    b3 = Button(button_frame, text="Remove Doctor",command=remove)
    b3.grid(row=0, column=2, padx=10, pady=10)

    b4 = Button(button_frame, text="# of Test",command=NumOfTest)
    b4.grid(row=1, column=0, padx=10, pady=10)
    e_Num=Entry(button_frame)
    e_Num.grid(row=1,column=1,padx=10,pady=10)

    

    cursor.execute("SELECT * FROM Doctor")
    for x in cursor:
        tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4]))
    def selectItem(a):
            clear()
            curItem = tree.focus()
            dname.insert(0,tree.item(curItem,'values')[1])
            dtype.insert(0,tree.item(curItem,'values')[2])
            dphone.insert(0,tree.item(curItem,'values')[3])
            demail.insert(0,tree.item(curItem,'values')[4])

    tree.bind('<ButtonRelease-1>', selectItem)

def Supplier(main_frame):
    deleteFrames(main_frame)
    style = ttk.Style()
    style.theme_use('default')

    style.configure("Treeview",
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3")

    style.map('Treeview',
    background=[('selected', "#347083")])
    f1 = Frame(main_frame)
    scroller = Scrollbar(f1)
    scroller.pack(side=RIGHT, fill=Y,pady="25")
    tree = ttk.Treeview(f1, yscrollcommand=scroller.set, selectmode="extended")
    tree.pack(pady="25")
    f1.pack()
    scroller.config(command=tree.yview)
    tree['columns'] = ("Supplier ID", "Name", "E-mail", "Phone")

    tree.column("#0", width=0, stretch=NO)
    tree.column("Supplier ID", anchor=CENTER, width=75)
    tree.column("Name", anchor=CENTER, width=150)
    tree.column("E-mail", anchor=CENTER, width=150)
    tree.column("Phone", anchor=CENTER, width=100)


    tree.heading("#0", text="", anchor=W)
    tree.heading("Supplier ID", text="Supplier ID", anchor=CENTER)
    tree.heading("Name", text="Name", anchor=CENTER)
    tree.heading("E-mail", text="E-mail", anchor=CENTER)
    tree.heading("Phone", text="Phone", anchor=CENTER)

    #tree.insert(parent='', index='end', iid=0, text='', values=("15","Test1","1500","dsfd", "dfdfd"))

    def search():
        for child in tree.get_children():
            tree.delete(child)  
        cursor.execute("SELECT * FROM Supplier WHERE S_Name = %s",(e_test.get(),))
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],))

    search_frame =LabelFrame(main_frame,text="Search", pady="15")
    search_frame.pack(fill="x",padx="20")
    lb_test = Label(search_frame,text="Supplier Name")
    e_test = Entry(search_frame)
    bt_test = Button(search_frame,text="Search",command=search)
    lb_test.grid(row=0,column=0,padx="10",pady="10")
    bt_test.grid(row=0,column=2,padx="10",pady="10")
    e_test.grid(row=0,column=1,padx="15",pady="10")


    data_frame = LabelFrame(main_frame, text="Supplier",pady="15")
    data_frame.pack(fill="x", padx=20)

    lb2 = Label(data_frame, text="Name")
    lb2.grid(row=0, column=0, padx=10, pady=10)
    ename = Entry(data_frame)
    ename.grid(row=0, column=1, padx=10, pady=10)

    lb3 = Label(data_frame, text="E-mail")
    lb3.grid(row=0, column=2, padx=10, pady=10)
    eEmail = Entry(data_frame)
    eEmail.grid(row=0, column=3, padx=10, pady=10)

    lb4 = Label(data_frame, text="Phone")
    lb4.grid(row=0, column=4, padx=10, pady=10)
    ephon = Entry(data_frame)
    ephon.grid(row=0, column=5, padx=10, pady=10)


    def clear():
        ename.delete(0,END)
        eEmail.delete(0,END)
        ephon.delete(0,END)
    def add():
        cursor.execute("INSERT INTO Supplier(S_Name,S_Email,S_Phone) VALUES (%s,%s,%s)", (ename.get(), eEmail.get(),ephon.get()))
        db.commit()

        cursor.execute("SELECT * FROM Supplier")
        for child in tree.get_children():
            tree.delete(child) 
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3]))

        clear()
        
    def update():
        curItem = tree.focus()
        id = tree.item(curItem,'values')[0]
        cursor.execute("UPDATE Supplier SET S_Name=%s, S_Email=%s, S_Phone=%s WHERE S_ID=%s",(ename.get(),eEmail.get(),ephon.get(),id))
        db.commit()
        cursor.execute("SELECT * FROM Supplier")
        for child in tree.get_children():
            tree.delete(child)
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3]))
        clear()


    def remove():
        curItem = tree.focus()
        cursor.execute("DELETE FROM Supplier where S_ID=%s", (tree.item(curItem,'values')[0],))
        db.commit()
        for child in tree.get_children():
            tree.delete(child)
        cursor.execute("SELECT * FROM Supplier")
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3]))
        clear()

       
    button_frame = LabelFrame(main_frame, text="Options",pady="15")
    button_frame.pack(fill="x", expand="yes", padx=20)

    b1 = Button(button_frame, text="Add Supplier",command=add)
    b1.grid(row=0, column=0, padx=10, pady=10)

    b2 = Button(button_frame, text="Update Values",command=update)
    b2.grid(row=0, column=1, padx=10, pady=10)

    b3 = Button(button_frame, text="Remove Supplier",command=remove)
    b3.grid(row=0, column=2, padx=10, pady=10)

    cursor.execute("SELECT * FROM Supplier")
    for x in cursor:
        tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3]))
    clear()

    def selectItem(a):
            clear()
            curItem = tree.focus()
            ename.insert(0,tree.item(curItem,'values')[1])
            eEmail.insert(0,tree.item(curItem,'values')[2])
            ephon.insert(0,tree.item(curItem,'values')[3])

    tree.bind('<ButtonRelease-1>', selectItem)

def Patient(main_frame):
    deleteFrames(main_frame)
    style = ttk.Style()
    style.theme_use('default')

    style.configure("Treeview",
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3")

    style.map('Treeview',
    background=[('selected', "#347083")])
    f1 = Frame(main_frame)
    scroller = Scrollbar(f1)
    scroller.pack(side=RIGHT, fill=Y,pady="25")
    tree = ttk.Treeview(f1, yscrollcommand=scroller.set, selectmode="extended")
    tree.pack(pady="25")
    f1.pack()
    scroller.config(command=tree.yview)
    tree['columns'] = ("Patient ID", "Name", "Date Of Birth", "E-mail", "Phone", "Whatsapp","Gender")

    tree.column("#0", width=0, stretch=NO)
    tree.column("Patient ID", anchor=CENTER, width=50)
    tree.column("Name", anchor=CENTER, width=100)
    tree.column("Date Of Birth", anchor=CENTER, width=100)
    tree.column("E-mail", anchor=CENTER, width=100)
    tree.column("Phone", anchor=CENTER, width=100)
    tree.column("Whatsapp", anchor=CENTER, width=100)
    tree.column("Gender", anchor=CENTER, width=100)


    tree.heading("#0", text="", anchor=W)
    tree.heading("Patient ID", text="Patient ID", anchor=CENTER)
    tree.heading("Name", text="Name", anchor=CENTER)
    tree.heading("Date Of Birth", text="Date Of Birth", anchor=CENTER)
    tree.heading("E-mail", text="E-mail", anchor=CENTER)
    tree.heading("Phone", text="Phone", anchor=CENTER)
    tree.heading("Whatsapp", text="Whatsapp", anchor=CENTER)
    tree.heading("Gender", text="Gender", anchor=CENTER)

    def search():
        field = option.get()
        if field == "Patient ID":
                for child in tree.get_children():
                    tree.delete(child)  
                cursor.execute("SELECT * FROM PATIENT WHERE P_ID = %s",(e_test.get(),))
                for x in cursor:
                    tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))
        elif field == "Name":
            for child in tree.get_children():
                tree.delete(child)  
            cursor.execute("SELECT * FROM PATIENT WHERE P_Name = %s",(e_test.get(),))
            for x in cursor:
                tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))
        elif field == "E-Mail":
                for child in tree.get_children():
                    tree.delete(child)  
                cursor.execute("SELECT * FROM PATIENT WHERE P_Name = %s",(e_test.get(),))
                for x in cursor:
                    tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))
        elif field == "Phone":
                for child in tree.get_children():
                    tree.delete(child)  
                cursor.execute("SELECT * FROM PATIENT WHERE P_Name = %s",(e_test.get(),))
                for x in cursor:
                    tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))

    search_frame =LabelFrame(main_frame,text="Search", pady="15")
    search_frame.pack(fill="x",padx="20")
    lb_test = Label(search_frame,text="Search Value")
    e_test = Entry(search_frame)
    bt_test = Button(search_frame,text="Search",command=search)
    lb_test.grid(row=0,column=0,padx="10",pady="10")
    bt_test.grid(row=0,column=5,padx="10",pady="10")
    e_test.grid(row=0,column=1,padx="15",pady="10")

    option = ttk.Combobox(search_frame, values=["Patient ID", "Name","E-mail", "Phone"])
    option.grid(row=0,column=4,padx=10,pady=10)
    option_lb = Label(search_frame,text="Search Metric")
    option_lb.grid(row=0,column=3,padx=10,pady=10)



    data_frame = LabelFrame(main_frame, text="Patient",pady="15")
    data_frame.pack(fill="x", padx=20)


    lb2 = Label(data_frame, text="Name")
    lb2.grid(row=0, column=0, padx=10, pady=10)
    ename =  Entry(data_frame)
    ename.grid(row=0, column=1, padx=10, pady=10)

    lb3 = Label(data_frame, text="Date Of Birth")
    lb3.grid(row=1, column=0, padx=10, pady=10)
    dobentry = Entry(data_frame)
    dobentry.grid(row=1, column=1, padx=10, pady=10)

    lb4 = Label(data_frame, text="E-mail")
    lb4.grid(row=1, column=2, padx=10, pady=10)
    EmailEntry = Entry(data_frame)
    EmailEntry.grid(row=1, column=3, padx=10, pady=10)
    
    lb5 = Label(data_frame, text="Phone")
    lb5.grid(row=0, column=2, padx=10, pady=10)
    ePhone = Entry(data_frame)
    ePhone.grid(row=0, column=3, padx=10, pady=10)

    lbGender= Label(data_frame,text='Gender')
    lbGender.grid(row=0, column=4, padx=10, pady=10)
    options = ["Male", "Female"]
    box=ttk.Combobox(data_frame,values=options)
    box.grid(row=0, column=5, padx=10, pady=10)

    lb6 = Label(data_frame, text="Whatsapp")
    lb6.grid(row=1, column=4, padx=10, pady=10)
    eWhatsapp = Entry(data_frame)
    eWhatsapp.grid(row=1, column=5, padx=10, pady=10)

    def clear():
        e_test.delete(0,END)
        dobentry.delete(0,END)
        ename.delete(0,END)
        EmailEntry.delete(0,END)
        ePhone.delete(0,END)
        eWhatsapp.delete(0,END)

    def add():
        for child in tree.get_children():
            tree.delete(child)  
        cursor.execute("INSERT INTO Patient (P_Name,P_Email,P_DOB,P_Phone,P_Whatsapp,P_Gender) VALUES (%s,%s,%s,%s,%s,%s)", (ename.get(),EmailEntry.get(),dobentry.get(),ePhone.get(),eWhatsapp.get(),box.get()))
        db.commit()
        cursor.execute("SELECT * FROM PATIENT")
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))
        clear()
    
    def update():
        curItem = tree.focus()     
        cursor.execute("UPDATE Patient SET P_Name=%s,P_Email=%s,P_DOB=%s,P_Phone=%s,P_Whatsapp=%s WHERE  P_ID=%s",(ename.get(),EmailEntry.get(),dobentry.get(),ePhone.get(),eWhatsapp.get(),tree.item(curItem,'values')[0]))
        db.commit()
        for child in tree.get_children():
            tree.delete(child) 
        cursor.execute("SELECT * FROM Patient")
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))
        clear()

    def remove():   
        curItem = tree.focus()     
        cursor.execute("DELETE FROM Patient where P_ID=%s", (tree.item(curItem,'values')[0],))
        db.commit()
        for child in tree.get_children():
            tree.delete(child)
        cursor.execute("SELECT * FROM Patient")
        for x in cursor:
            tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))
        clear()

    def countTests():
        id = tree.item(tree.focus(),'values')[0]
        cursor.execute("SELECT COUNT(*) FROM TESTBANK WHERE TB_P_ID = %s", (id,))
        for x in cursor:
            ecount.insert(0,x[0])
        
    button_frame = LabelFrame(main_frame, text="Options",pady="15")
    button_frame.pack(fill="x", expand="yes", padx=20)

    b1 = Button(button_frame, text="Add Patient", command=add)
    b1.grid(row=0, column=0, padx=10, pady=10)

    b2 = Button(button_frame, text="Update Values",command=update)
    b2.grid(row=0, column=1, padx=10, pady=10)

    b3 = Button(button_frame, text="Remove Patient",command=remove)
    b3.grid(row=0, column=2, padx=10, pady=10)

    b4 = Button(button_frame,text="Create Test", command= lambda : TestBank(main_frame,tree.item(tree.focus(),'values')[1]))
    b4.grid(row=0,column=3,padx=1,pady=10)

    b5 = Button(button_frame,text="# of tests",command=countTests)
    b5.grid(row=1,column=0,padx=10,pady=10)

    ecount = Entry(button_frame)
    ecount.grid(row=1,column=1,padx=10,pady=10)

    cursor.execute("SELECT * FROM Patient")
    for x in cursor:
        tree.insert(parent='', index=0, text='', values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))

    def selectItem(a):
            clear()
            curItem = tree.focus()
            ename.insert(0,tree.item(curItem,'values')[1])
            dobentry.insert(0,tree.item(curItem,'values')[2])
            EmailEntry.insert(0,tree.item(curItem,'values')[3])
            ePhone.insert(0,tree.item(curItem,'values')[4])
            eWhatsapp.insert(0,tree.item(curItem,'values')[5])
    tree.bind('<ButtonRelease-1>', selectItem)         


def checkIfUser(user,passw):
    if user == '' and passw == '' or True:
        return True
def bt1():
    if checkIfUser(e1.get(),e2.get()):
            root.state(newstate="iconic")
            main_window = Toplevel()
            main_window.title("Medical Laboratory")
            main_window.geometry("1000x725+100+25")
            
            main_frame = Frame(main_window,height=600)
            options_frame = LabelFrame(main_window,bg="#c3c3c3")
            btn1 = Button(options_frame, text="Patient", command= lambda : Patient(main_frame))
            btn2 = Button(options_frame, text="Doctors", command= lambda : Doctor(main_frame))
            btn3 = Button(options_frame, text="Tests", command= lambda : tests(main_frame))
            btn4 = Button(options_frame, text="Test Bank", command= lambda : TestBank(main_frame) )
            btn5 = Button(options_frame, text="Maintenance" , command= lambda : Maintenance(main_frame))
            btn6 = Button(options_frame, text="Suppliers", command= lambda : Supplier(main_frame))
            btn7 = Button(options_frame, text="Chemicals", command= lambda : Chemical(main_frame))
            btn8 = Button(options_frame, text="Equipment", command= lambda : Equipment(main_frame))
            btn9 = Button(options_frame, text="Insurance", command= lambda : Insurance(main_frame))
            btn10 = Button(options_frame, text="Employees" , command= lambda : Employee(main_frame))
            btn11 = Button(options_frame, text="Finances", command= lambda : fins(main_frame))
            #btn12 = Button(options_frame, text="System",command=lambda : System(main_frame))
            btn1.pack(padx="5",pady="15")
            btn2.pack(padx="5",pady="15")
            btn3.pack(padx="5",pady="15")
            btn4.pack(padx="5",pady="15")
            btn5.pack(padx="5",pady="15")
            btn6.pack(padx="5",pady="15")
            btn7.pack(padx="5",pady="15")
            btn8.pack(padx="5",pady="15")
            btn9.pack(padx="5",pady="15")
            btn10.pack(padx="5",pady="15")
            btn11.pack(padx="5",pady="15")
            #btn12.pack(padx="5",pady="15")
            options_frame.grid(row="0",column="0",padx="15",pady="15")


            main_frame.grid(row="0",column="1",padx="15",pady="15")

            status_frame = LabelFrame(main_window,bg="#c3c3c3")
            user_lb = Label(status_frame,text="Current User : ")
            user_e = Entry(status_frame)
            user_lb.pack()
            user_e.pack()
            main_window.mainloop()


global db
db = mysql.connector.connect(
    user="root",
    host="localhost",
    passwd="12345",
    database="MedicalLab"
)

global cursor
cursor = db.cursor()

root = Tk()
root.title("Sadaka Medical Laboratory")
root.geometry("750x400+100+50")

lb1 = Label(root,text="Laboratory System")
lb2 = Label(root,text="Username")
lb3 = Label(root,text="Password")

e1 = Entry(root,width="50")
e2 = Entry(root, width="50",show="*")

lb1.grid(row="1",column="1",padx="15",pady="15")
lb2.grid(row="2",column="2",padx="15",pady="15")
e1.grid(row="2",column="3",padx="15",pady="15")
e2.grid(row="3",column="3",padx="15",pady="15")
lb3.grid(row="3",column="2",padx="15",pady="15")

btn1 = Button(root, text="Sign In", command=bt1)

btn1.grid(row="4",column="3",padx="10",pady="10")
root.mainloop()