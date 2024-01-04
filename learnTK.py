  
from tkinter import *
from tkinter.ttk import Treeview
def pationt():
    T3 = Toplevel()
    T3.geometry("900x650+200+75")
    T3.title("Pationt Info")
    tree_frame = Frame(T3)
    tree_frame.pack(pady=10)
    # Create a Treeview Scrollbar
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)
    # Create The Treeview
    my_tree = Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
    my_tree.pack()

    # Configure the Scrollbar
    tree_scroll.config(command=my_tree.yview)

    # Define Our Columns
    my_tree['columns'] = ("First Name", "mid Name","Last Name", "Phone", "Doctor_Name", "Doctor_ID", "Email") 
    # my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("First Name", anchor=W, width=40)
    my_tree.column("mid Name", anchor=W, width=40)
    my_tree.column("Last Name", anchor=CENTER, width=40)
    my_tree.column("Phone", anchor=CENTER, width=140)
    my_tree.column("Doctor_Name", anchor=CENTER, width=140)
    my_tree.column("Doctor_ID", anchor=CENTER, width=140)
    my_tree.column("Email", anchor=CENTER, width=140)
    # Create Headings
    # my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("First Name", text="First Name", anchor=W)
    my_tree.heading("mid Name", text="mid Name", anchor=W)
    my_tree.heading("Last Name", text="Last Name", anchor=CENTER)
    my_tree.heading("Phone", text="Phone", anchor=CENTER)
    my_tree.heading("Doctor_Name", text="Doctor_Name", anchor=CENTER)
    my_tree.heading("Doctor_ID", text="Doctor_ID", anchor=CENTER)
    my_tree.heading("Email", text="Email", anchor=CENTER)

    data = [
	["John", "Elder", 1, "123 Elder St.", "Las Vegas", "NV", "89137"],
	["Mary", "Smith", 2, "435 West Lookout", "Chicago", "IL", "60610"],
	["Tim", "Tanaka", 3, "246 Main St.", "New York", "NY", "12345"],
	["Erin", "Erinton", 4, "333 Top Way.", "Los Angeles", "CA", "90210"],
	["Bob", "Bobberly", 5, "876 Left St.", "Memphis", "TN", "34321"],
	["Steve", "Smith", 6, "1234 Main St.", "Miami", "FL", "12321"],
	["Tina", "Browne", 7, "654 Street Ave.", "Chicago", "IL", "60611"],
	["Mark", "Lane", 8, "12 East St.", "Nashville", "TN", "54345"],
	["John", "Smith", 9, "678 North Ave.", "St. Louis", "MO", "67821"],
	["Mary", "Todd", 10, "9 Elder Way.", "Dallas", "TX", "88948"],
	["John", "Lincoln", 11, "123 Elder St.", "Las Vegas", "NV", "89137"],
	["Mary", "Bush", 12, "435 West Lookout", "Chicago", "IL", "60610"],
	["Tim", "Reagan", 13, "246 Main St.", "New York", "NY", "12345"],
	["Erin", "Smith", 14, "333 Top Way.", "Los Angeles", "CA", "90210"],
	["Bob", "Field", 15, "876 Left St.", "Memphis", "TN", "34321"],
	["Steve", "Target", 16, "1234 Main St.", "Miami", "FL", "12321"],
	["Tina", "Walton", 17, "654 Street Ave.", "Chicago", "IL", "60611"],
	["Mark", "Erendale", 18, "12 East St.", "Nashville", "TN", "54345"],
	["John", "Nowerton", 19, "678 North Ave.", "St. Louis", "MO", "67821"],
	["Mary", "Hornblower", 20, "9 Elder Way.", "Dallas", "TX", "88948"]
	
    ]
    # Create Striped Row Tags
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightblue")

    # Add our data to the screen
    global count
    count = 0

    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('oddrow',))
        # increment counter
        count += 1


    # Add Record Entry Boxes
    data_frame = LabelFrame(T3, text="Record")
    data_frame.pack(fill="x", expand="yes", padx=20)
    
    fn_label = Label(data_frame, text="First Name")
    fn_label.grid(row=0, column=0, padx=10, pady=10)
    fn_entry = Entry(data_frame)
    fn_entry.grid(row=0, column=1, padx=10, pady=10)

    ln_label = Label(data_frame, text="Mid Name")
    ln_label.grid(row=0, column=2, padx=10, pady=10)
    ln_entry = Entry(data_frame)
    ln_entry.grid(row=0, column=3, padx=10, pady=10)

    id_label = Label(data_frame, text="Last Name")
    id_label.grid(row=0, column=4, padx=10, pady=10)
    id_entry = Entry(data_frame)
    id_entry.grid(row=0, column=5, padx=10, pady=10)

    address_label = Label(data_frame, text="phone")
    address_label.grid(row=1, column=0, padx=10, pady=10)
    address_entry = Entry(data_frame)
    address_entry.grid(row=1, column=1, padx=10, pady=10)

    city_label = Label(data_frame, text="Doctor Name")
    city_label.grid(row=1, column=2, padx=10, pady=10)
    city_entry = Entry(data_frame)
    city_entry.grid(row=1, column=3, padx=10, pady=10)

    state_label = Label(data_frame, text="email")
    state_label.grid(row=1, column=4, padx=10, pady=10)
    state_entry = Entry(data_frame)
    state_entry.grid(row=1, column=5, padx=10, pady=10)

    # zipcode_label = Label(data_frame, text="First Name")
    # zipcode_label.grid(row=1, column=6, padx=10, pady=10)
    # zipcode_entry = Entry(data_frame)
    # zipcode_entry.grid(row=1, column=7, padx=10, pady=10)


    # Add Buttons
    button_frame = LabelFrame(T3, text="Commands")
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

    select_record_button = Button(button_frame, text="Select Record")
    select_record_button.grid(row=0, column=7, padx=10, pady=10)












    T3.mainloop()
def bt1():
    if e1.get() == 'Root' and e2.get() == '12345':
        T2 = Toplevel()
        T2.geometry("900x650+200+75")
        T2.title("Main Application")
        lb1 = Label(T2,text="")
        
        b1=Button(T2,text='Pationt',font=('tawajal',12),command=pationt)
        b1.place(x=50,y=50)
        b2=Button(T2,text='Tests',font=('tawajal',12))
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







#cursor.execute("INSERT INTO Supplier (supp_ID, supp_name,supp_email) VALUES (%s,%s,%s)" , (15,"Supplier One","supp@gmail.com"))
#db.commit()

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

btn1 = Button(root, text="Sign In", command=bt1)

btn1.grid(row="4",column="3",padx="10",pady="10")




root.mainloop()


