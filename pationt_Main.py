from tkinter import *
from tkinter.ttk import Treeview , Scrollbar ,Style
  












#creating the application main window.   
top = Tk()  
top.geometry('990x580+150+50')
#Entering the event main loop  


# data_frame1 = LabelFrame(top, text="Pationt",bg='#D3D3D3')

# data_frame1.place(x=30, y=35, width=150,height=510)
# b1 = Button(data_frame1, text='SEARCH',height=3,width=8)

# b2 = Button(data_frame1, text='ADD',height=3,width=8)
# b3 = Button(data_frame1, text='UPDATE',height=3,width=8)

# b1.pack(padx=5,pady=5)
# b2.pack(padx=5,pady=5)
# b3.pack(padx=5,pady=5)


my_tree = Treeview(top)


#Define Our Columns 
my_tree['columns'] = ("Pationt_ID","First Name", "mid Name","Last Name", "Phone", "Doctor_Name", "Email") 

#  Formate Our Columns
my_tree.column("#0",width=120,minwidth=25)
my_tree.column("Pationt_ID",anchor=W,width=45,stretch=False)
my_tree.column("First Name",anchor=W,width=120,stretch=False)
my_tree.column("mid Name",anchor=W,width=120)
my_tree.column("Last Name",anchor=W,width=120)
my_tree.column("Phone",anchor=W,width=20)
my_tree.column("Doctor_Name",anchor=W,width=35)
my_tree.column("Email",anchor=W,width=50)

# Create Heading 
# my_tree.heading("#0",text="Label",anchor=W)
my_tree.heading("Pationt_ID",text="Pationt_ID",anchor=W)
my_tree.heading("First Name",text="First Name",anchor=W)
my_tree.heading("mid Name",text="mid Name",anchor=W,)
my_tree.heading("Last Name",text="Last Name",anchor=W,)
my_tree.heading("Phone",text="Phone",anchor=W)
my_tree.heading("Doctor_Name",anchor=W,text="Doctor_Name")
my_tree.heading("Email",text="Email",anchor=W)

style = Style()
style.theme_use('default')

style.configure("Treeview",
background="#D3D3D3",
foreground="black",
rowheight=25,
fieldbackground="#D3D3D3")

style.map('Treeview',
    background=[('selected', "#347083")])
# ADD Data
my_tree.insert(parent='',index='end',iid=0,text="", values=(1203085,'Alaa','Yasin','Darawish','0597308909','hatem','alaa@gmail.com'))

# scrollbar = Scrollbar(treeView,orient="vertical",command=treeView.yview)

# scrollbar.pack(side="right", fill="y")
# treeView.pack(side="top", fill="both", expand=True)

my_tree.pack(padx=250,pady=50)

# Frame 2 in the Bottom 

data_frame2 = LabelFrame(top, text="Pationt Bank",bg='#D3D3D3')
data_frame2.place(x=180, y=450, width=728,height=100)





# data_frame3 = LabelFrame(top, text="Pationt",bg='#D3D3D3')

# data_frame1.place(x=30, y=35, width=150,height=510)

data_frame4 = LabelFrame(top, text="Test",bg='#D3D3D3')
data_frame4.place(x=180, y=330,width=728,height=100)

lb1 = Label(data_frame4, text="Pationt ID")
lb1.grid(row=0, column=0, padx=10, pady=10)
e1 = Entry(data_frame4)
e1.grid(row=0, column=1, padx=10, pady=10)

lb2 = Label(data_frame4, text="First Name")
lb2.grid(row=0, column=2, padx=10, pady=10)
e2 = Entry(data_frame4)
e2.grid(row=0, column=3, padx=10, pady=10)

lb3 = Label(data_frame4, text="med Name")
lb3.grid(row=0, column=4, padx=10, pady=10)
e3 = Entry(data_frame4)
e3.grid(row=0, column=5, padx=10, pady=10)

lb4 = Label(data_frame4, text="Last Name")
lb4.grid(row=1, column=0, padx=10, pady=10)
e4 = Entry(data_frame4)
e4.grid(row=1, column=1, padx=10, pady=10)

lb5 = Label(data_frame4, text="Phone")
lb5.grid(row=1, column=2, padx=10, pady=10)
e5 = Entry(data_frame4)
e5.grid(row=1, column=3, padx=10, pady=10)

lb6 =Label(data_frame4,text='Doctor Name') 
lb6.grid(row=1,column=4,padx=10,pady=10)   


e6 = Entry(data_frame4)
e6.grid(row=1,column=5,padx=10,pady=10)
def add_Pationt():
    id = e1.get()
    print('ID :')
    print(id)
b1 = Button(data_frame2, text='SEARCH',height=3,width=10)
b2 = Button(data_frame2, text='ADD',height=3,width=10,command=add_Pationt())
b3 = Button(data_frame2, text='UPDATE',height=3,width=10)
b4 = Button(data_frame2,text='PHB',height=3,width=10)
b5 = Button(data_frame2,text='Print Report',height=3,width=10)
b1.grid(row=0,column=0,padx=10,pady=3)
b2.grid(row=0,column=1,padx=10,pady=3)
b3.grid(row=0,column=3,padx=10,pady=3)
b4.grid(row=0,column=4,padx=10,pady=3)
b5.grid(row=0,column=5,padx=10,pady=3)
top.mainloop()  


# def TestBank(main_frame):
#     # deleteFrames(main_frame)
#     style = Style()
#     style.theme_use('default')

#     style.configure("Treeview",
#     background="#D3D3D3",
#     foreground="black",
#     rowheight=25,
#     fieldbackground="#D3D3D3")

#     style.map('Treeview',
#     background=[('selected', "#347083")])
#     f1 = Frame(main_frame)
#     scroller = Scrollbar(f1)
#     scroller.pack(side=RIGHT, fill=Y,pady="25")
#     tree = Treeview(f1, yscrollcommand=scroller.set, selectmode="extended")
#     tree.pack(pady="25")
#     f1.pack()
#     scroller.config(command=tree.yview)
#     tree['columns'] = ("Test Bank ID", "Test Name", "Patient Name", "Result", "Date","Payment ID", "Doctor")

#     tree.column("#0", width=0, stretch=NO)
#     tree.column("Test Bank ID", anchor=CENTER, width=75)
#     tree.column("Test Name", anchor=CENTER, width=140)
#     tree.column("Patient Name", anchor=CENTER, width=100)
#     tree.column("Result", anchor=CENTER, width=140)
#     tree.column("Date", anchor=CENTER, width=100)
#     tree.column("Payment ID", anchor=CENTER, width=75)
#     tree.column("Doctor", anchor=CENTER, width=140)
     

#     tree.heading("#0", text="", anchor=W)
#     tree.heading("Test Bank ID", text="Test Bank ID", anchor=CENTER)
#     tree.heading("Test Name", text="Test Name", anchor=CENTER)
#     tree.heading("Patient Name", text="Patient Name", anchor=CENTER)
#     tree.heading("Result", text="Result", anchor=CENTER)
#     tree.heading("Date", text="Date", anchor=CENTER)
#     tree.heading("Payment ID", text="Payment ID", anchor=CENTER)
#     tree.heading("Doctor", text="Doctor", anchor=CENTER)
#     #tree.insert(parent='', index='end', iid=0, text='', values=("15","Test1","1500","dsfd", "dfdfd"))
    
#     search_frame =LabelFrame(main_frame,text="Search", pady="15")
#     search_frame.pack(fill="x",padx="20")
#     lb_test = Label(search_frame,text="Test Name")
#     e_test = Entry(search_frame)
#     bt_test = Button(search_frame,text="Search")
#     lb_test.grid(row=0,column=0,padx="10",pady="10")
#     bt_test.grid(row=0,column=2,padx="10",pady="10")
#     e_test.grid(row=0,column=1,padx="15",pady="10")


#     data_frame = LabelFrame(main_frame, text="Test",pady="15")
#     data_frame.pack(fill="x", padx=20)

#     lb1 = Label(data_frame, text="Test Bank ID")
#     lb1.grid(row=0, column=0, padx=10, pady=10)
#     e1 = Entry(data_frame)
#     e1.grid(row=0, column=1, padx=10, pady=10)

#     lb2 = Label(data_frame, text="Test Name")
#     lb2.grid(row=0, column=2, padx=10, pady=10)
#     e2 = Entry(data_frame)
#     e2.grid(row=0, column=3, padx=10, pady=10)

#     lb3 = Label(data_frame, text="Patient Name")
#     lb3.grid(row=0, column=4, padx=10, pady=10)
#     e3 = Entry(data_frame)
#     e3.grid(row=0, column=5, padx=10, pady=10)

#     lb4 = Label(data_frame, text="Result")
#     lb4.grid(row=1, column=0, padx=10, pady=10)
#     e4 = Entry(data_frame)
#     e4.grid(row=1, column=1, padx=10, pady=10)
#     lb5 = Label(data_frame, text="Date")
#     lb5.grid(row=1, column=2, padx=10, pady=10)
#     e5 = Entry(data_frame)
#     e5.grid(row=1, column=3, padx=10, pady=10)

#     lb6 = Label(data_frame, text="Payment ID")
#     lb6.grid(row=1, column=4, padx=10, pady=10)
#     e6 = Entry(data_frame)
#     e6.grid(row=1, column=5, padx=10, pady=10)
#     lb7 = Label(data_frame, text="Doctor")
#     lb7.grid(row=2, column=0, padx=10, pady=10)
#     e7 = Entry(data_frame)
#     e7.grid(row=2, column=1, padx=10, pady=10)
          

#     button_frame = LabelFrame(main_frame, text="Options",pady="15")
#     button_frame.pack(fill="x", expand="yes", padx=20)

#     b1 = Button(button_frame, text="Add Test")
#     b1.grid(row=0, column=0, padx=10, pady=10)

#     b2 = Button(button_frame, text="Update Values")
#     b2.grid(row=0, column=1, padx=10, pady=10)

#     b3 = Button(button_frame, text="Remove Test")
#     b3.grid(row=0, column=2, padx=10, pady=10)
#     def selectItem(a):
#             e1.configure(state="normal")
#             e1.delete(0,END)
#             e2.delete(0,END)
#             e3.delete(0,END)
#             e4.delete(0,END)
#             e5.delete(0,END)
#             curItem = tree.focus()
#             e1.insert(0,tree.item(curItem,'values')[0])
#             e1.configure(state="disabled")
#             e2.insert(0,tree.item(curItem,'values')[1])
#             e3.insert(0,tree.item(curItem,'values')[2])
#             e4.insert(0,tree.item(curItem,'values')[3])
#             e5.insert(0,tree.item(curItem,'values')[4])
   
#     tree.bind('<ButtonRelease-1>', selectItem)


# def deleteFrames(main_frame : Frame):
    # for frame in main_frame.winfo_children():
    #     frame.destroy()
