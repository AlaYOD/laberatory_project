from tkinter import *
import mysql.connector
from tkinter import ttk
def tests():

    t3 = Toplevel()
    t3.title("Tests")
    t3.geometry("800x550+100+25")


    style = ttk.Style()

    style.theme_use('default')

    style.configure("Treeview",
	background="#D3D3D3",
	foreground="black",
	rowheight=25,
	fieldbackground="#D3D3D3")

    style.map('Treeview',
	background=[('selected', "#347083")])
    f1 = Frame(t3)
    scroller = Scrollbar(f1)
    scroller.pack(side=RIGHT, fill=Y,pady="25")
    tree = ttk.Treeview(f1, yscrollcommand=scroller.set, selectmode="extended")
    tree.pack(pady="25")
    f1.pack()
    scroller.config(command=tree.yview)
    tree['columns'] = ("Test ID", "Test Name", "Test Cost", "Chemical Used", "Equipment Used")

    tree.column("#0", width=0, stretch=NO)
    tree.column("Test ID", anchor=CENTER, width=140)
    tree.column("Test Name", anchor=CENTER, width=140)
    tree.column("Test Cost", anchor=CENTER, width=100)
    tree.column("Chemical Used", anchor=CENTER, width=140)
    tree.column("Equipment Used", anchor=CENTER, width=140)

    tree.heading("#0", text="", anchor=W)
    tree.heading("Test ID", text="Test ID", anchor=CENTER)
    tree.heading("Test Name", text="Test Name", anchor=CENTER)
    tree.heading("Test Cost", text="Test Cost", anchor=CENTER)
    tree.heading("Chemical Used", text="Chemical Used", anchor=CENTER)
    tree.heading("Equipment Used", text="Equipment Used", anchor=CENTER)
    #tree.insert(parent='', index='end', iid=0, text='', values=("15","Test1","1500","dsfd", "dfdfd"))

    data_frame = LabelFrame(t3, text="Test")
    data_frame.pack(fill="x", padx=20)

    lb1 = Label(data_frame, text="Test ID")
    lb1.grid(row=0, column=0, padx=10, pady=10)
    e1 = Entry(data_frame)
    e1.grid(row=0, column=1, padx=10, pady=10)

    lb2 = Label(data_frame, text="Test Name")
    lb2.grid(row=0, column=2, padx=10, pady=10)
    e2 = Entry(data_frame)
    e2.grid(row=0, column=3, padx=10, pady=10)

    lb3 = Label(data_frame, text="Test Cost")
    lb3.grid(row=0, column=4, padx=10, pady=10)
    e3 = Entry(data_frame)
    e3.grid(row=0, column=5, padx=10, pady=10)

    lb4 = Label(data_frame, text="Chemical Used")
    lb4.grid(row=1, column=0, padx=10, pady=10)
    e4 = Entry(data_frame)
    e4.grid(row=1, column=1, padx=10, pady=10)

    lb5 = Label(data_frame, text="Equipment Used")
    lb5.grid(row=1, column=2, padx=10, pady=10)
    e5 = Entry(data_frame)
    e5.grid(row=1, column=3, padx=10, pady=10)
    

    button_frame = LabelFrame(root, text="Commands")
    button_frame.pack(fill="x", expand="yes", padx=20)

    update_button = Button(button_frame, text="Update Record")
    update_button.grid(row=0, column=0, padx=10, pady=10)

    add_button = Button(button_frame, text="Add Record")
    add_button.grid(row=0, column=1, padx=10, pady=10)

    remove_all_button = Button(button_frame, text="Remove All Records")
    remove_all_button.grid(row=0, column=2, padx=10, pady=10)

    remove_one_button = Button(button_frame, text="Remove One Selected")
    remove_one_button.grid(row=0, column=3, padx=10, pady=10)

    remove_many_button = Button(button_frame, text="Remove Many Selected")
    remove_many_button.grid(row=0, column=4, padx=10, pady=10)

    move_up_button = Button(button_frame, text="Move Up")
    move_up_button.grid(row=0, column=5, padx=10, pady=10)

    move_down_button = Button(button_frame, text="Move Down")
    move_down_button.grid(row=0, column=6, padx=10, pady=10)

    select_record_button = Button(button_frame, text="Clear Entry Boxes")
    select_record_button.grid(row=0, column=7, padx=10, pady=10)

    t3.mainloop()

root = Tk()
root.title('Medical Laboratory')
root.geometry("800x500+200+100")

lb1 = Label(root,text="Laboratory System")
lb2 = Label(root,text="Username")
lb3 = Label(root,text="Password")

e1 = Entry(root,width="50")
e2 = Entry(root, width="50")

lb1.grid(row="1",column="1",padx="15",pady="15")
lb2.grid(row="2",column="2",padx="15",pady="15")
e1.grid(row="2",column="3",padx="15",pady="15")
e2.grid(row="3",column="3",padx="15",pady="15")
lb3.grid(row="3",column="2",padx="15",pady="15")

def bt1():
    if e1.get() == 'Root' and e2.get() == '12345' or True:
        T2 = Toplevel()
        T2.geometry("900x650+200+75")
        T2.title("Main Application")
        lb1 = Label(T2,text="")
        
        b1=Button(T2,text='Pationt',font=('tawajal',12))
        b1.place(x=50,y=50)
        b2=Button(T2,text='Tests',font=('tawajal',12), command=tests)
        b2.place(x=50,y=100)
        b3=Button(T2,text='Doctor',font=('tawajal',12))
        b3.place(x=50,y=150)
        b4=Button(T2,text='supplier',font=('tawajal',12))
        b4.place(x=50,y=200)
        b5=Button(T2,text='maintenance',font=('tawajal',12))
        b5.place(x=50,y=250)
        b6=Button(T2,text='Financials',font=('tawajal',12))
        b6.place(x=50,y=300)
        b5=Button(T2,text='Suppliers',font=('tawajal',12))
        b5.place(x=50,y=350)
        b5=Button(T2,text='Employees',font=('tawajal',12))
        b5.place(x=50,y=400)
        b6=Button(T2,text='System',font=('tawajal',12))
        b6.place(x=450,y=300)
        b7=Button(T2,text='Test Bank',font=('tawajal',12))
        b7.place(x=50,y=350)
        T2.mainloop()

btn1 = Button(root, text="Sign In", command=bt1)

btn1.grid(row="4",column="3",padx="10",pady="10")





root.mainloop()