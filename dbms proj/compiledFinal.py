import mysql.connector
import tkinter as tk
from tkinter import *
import customtkinter as ctk
from pathlib import Path
import tkinter.messagebox as messagebox
from PIL import Image,ImageTk
from random import *
from tkinter import ttk
Button
# Backend python functions code starts :
def createtable():
    conn=mysql.connector.connect(host="localhost",user="root",password="12345678",database="bank")
    if conn.is_connected():
            print("Connected to the database.")
    else:
        print("Failed to connect to the database.")
    cursor=conn.cursor()
    cursor.execute("create table if not exists customer(name varchar(50),address varchar(50),email varchar(30),phone varchar(50),age int,password varchar(50),account varchar(30) primary key)")
    conn.commit()
    conn.close()
    
def deletecustomer(accountno):
    conn=mysql.connector.connect(host="localhost",user="root",password="12345678",database="bank")
    cursor=conn.cursor()
    cursor.execute('delete from customer where account=?',(accountno))
    conn.commit()
    conn.close()
def accountexist():
    conn=mysql.connector.connect(host="localhost",user="root",password="12345678",database="bank")
    cursor=conn.cursor()
    cursor.execute("select count(*) from customer where account='"+entry1.get()+"'"+"and password='"+entry2.get()+"'")
    result=cursor.fetchone()
    conn.close()
    return result[0]>0

# frontend python functions code starts :
window=ctk.CTk()
def welcome():
    window.geometry("600x490+383+120")
    window.title("Bank Management Sysytem")
    ctk.set_appearance_mode("light")
    window.config(bg="#1F43A0")
    ctk.set_default_color_theme("green")
    frame=ctk.CTkFrame(master=window,fg_color='yellow2')
    frame.pack(pady=60,padx=60,fill="both",expand=True)
    label1=ctk.CTkLabel(master=frame,text="Welcome To Our Bank",font=("TkHeadingFont",30,'bold'))
    label1.pack(pady=20,padx=20)
    button1=ctk.CTkButton(master=frame,text="admin",command=adminlogin)
    button1.pack(pady=20,padx=20)
    button2=ctk.CTkButton(master=frame,text="customer",command=customerlogin)
    button2.pack(pady=20,padx=20)
    img=ImageTk.PhotoImage(Image.open("./DBMSPROJ/bank2.png"))
    label2=Label(image=img)
    label2.image=img
    label2.pack(pady=1)

def loanstatus():
    global entryam
    nw5=Toplevel(window)
    nw5.geometry("500x300")
    nw5.title("LOAN AMOUNT")
    ctk.set_appearance_mode("light")
    nw5.config(bg='blue4')
    frameln=ctk.CTkFrame(master=nw5,width=100,height=100,corner_radius=15,fg_color='ivory2')
    frameln.pack(pady=20,padx=20,fill="both",expand=True)
    labelam=ctk.CTkLabel(master=frameln,text="Amount:",font=("Arial",18),text_color='black')
    labelam.place(y=50,x=100)
    entryam=ctk.CTkEntry(master=frameln,width=300,placeholder_text="Amount")
    entryam.place(y=100,x=100)
    buttonam=ctk.CTkButton(master=frameln,text="Request",command=reqloan)
    buttonam.place(y=150,x=100)
    buttonams=ctk.CTkButton(master=frameln,text="Back",command=nw5.withdraw)
    buttonams.place(y=200,x=100)

def lstat():
    conn=mysql.connector.connect(host="localhost",user="root",password="12345678",database="bank")
    cursor=conn.cursor()
    qry1="create table if not exists loanstatus (account varchar(30) primary key,amount int,status int)"
    cursor.execute(qry1)
    qury2="select status from loanstatus where account=(%s)"
    values=(account,)
    cursor.execute(qury2,values)
    result=cursor.fetchone()

    if result is not None:
        print(result[0])
        if result[0]==1:
            messagebox.showinfo("Loan Status","Loan request not accepted.")
        elif result[0]==2:
            messagebox.showinfo("Loan Status","Loan request accepted.")
        else:
            messagebox.showinfo("Loan Status", "Unknown loan status value.")
    else:
        messagebox.showinfo("Loan Status", "No loan status found for the account.")
    cursor.close()
    conn.close()
def reqloan():
    amount = entryam.get()
    if not amount:
        messagebox.showwarning('Error', 'Enter all fields')
    elif not amount.isdigit():
        messagebox.showwarning('Error', 'Enter integer values only')
    else:
        entryam.delete(0, 'end')
        conn = mysql.connector.connect(host="localhost", user="root", password="12345678", database="bank")
        cursor = conn.cursor()
        qry1="create table if not exists loanstatus (account varchar(30) primary key,amount int,status int)"
        cursor.execute(qry1)
        # Check if there is an existing loan request for the account
        qry_check_existing = "SELECT * FROM loanstatus WHERE account = %s AND status = 1"
        cursor.execute(qry_check_existing, (account,))
        existing_loan_request = cursor.fetchone()

        if existing_loan_request:
            # If an existing loan request exists, you can choose to update it or show an error message
            messagebox.showinfo("Loan status", "A loan request already exists for this account.")
        else:
            # If no existing loan request, insert the new loan request
            qry_insert_loan = "INSERT INTO loanstatus (account, amount, status) VALUES (%s, %s, 1)"
            values = (account, int(amount),)
            cursor.execute(qry_insert_loan, values)
            messagebox.showinfo("Loan status", "Loan Request sent successfully")

        conn.commit()
        cursor.close()
        conn.close()

def emploanstatus():
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"./build9/assets/frame0")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window9 = Toplevel(window)
    window9.title("Loan Status")
    window9.geometry("800x600")
    window9.configure(bg = "#1F43A0")

    canvas = Canvas(
        window9,
        bg = "#1F43A0",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        400.0,
        45.0,
        image=image_image_1
    )

    canvas.create_text(
        85.0,
        25.0,
        anchor="nw",
        text="Loan",
        fill="#000000",
        font=("Inter Medium", 40 * -1)
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        401.0,
        347.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        54.0,
        51.0,
        image=image_image_3
    )
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        window9,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=4,
        command=window9.withdraw,
        relief="flat"
    )
    button_1.place(
        x=329.0,
        y=537.0,
        width=155.0,
        height=44.0
    )
     # Fetch loan requests from the database
    conn = mysql.connector.connect(host="localhost", user="root", password="12345678", database="bank")
    cursor = conn.cursor()
    qry = "SELECT account, amount FROM loanstatus WHERE status = 1"
    cursor.execute(qry)
    loan_requests = cursor.fetchall()
    cursor.close()
    conn.close()

    # Display loan requests in the GUI
    row_height = 100
    for idx, (account_number, amount) in enumerate(loan_requests):
        canvas.create_text(
            100.0,
            150 + idx * row_height,
            anchor="nw",
            text=f"Account: {account_number}\nAmount: {amount}",
            fill="#FFFFFF",
            font=("Inter Bold", 26 * -1)
        )

        # Approve Button
        approve_button = Button(
            window9,
            text=f"Approve Loan {idx + 1}",
            command=lambda acc=account_number: approve_loan(acc),
            relief="flat"
        )
        approve_button.place(
            x=400.0,
            y=150 + idx * row_height,
            width=155.0,
            height=44.0
        )

    window9.resizable(False, False)
    window9.mainloop()

def approve_loan(account_number):
    # Update the loan status to '2' in the database
    conn = mysql.connector.connect(host="localhost", user="root", password="12345678", database="bank")
    cursor = conn.cursor()
    qry = "UPDATE loanstatus SET status = 2 WHERE account = %s"
    cursor.execute(qry, (account_number,))
    conn.commit()
    cursor.close()
    conn.close()

    # Display a message indicating that the loan has been approved
    messagebox.showinfo("Loan Approval", f"Loan for account {account_number} has been approved.")
    
def deletestatus():
    conn = mysql.connector.connect(host="localhost", user="root", password="12345678", database="bank")
    cursor = conn.cursor()
    qry1 = "CREATE TABLE IF NOT EXISTS deletestatus(account VARCHAR(30) PRIMARY KEY, status INT)"
    cursor.execute(qry1)
    
     # Check if the account already exists in deletestatus
    qry_check_existing = "SELECT * FROM deletestatus WHERE account = %s"
    cursor.execute(qry_check_existing, (account,))
    existing_entry = cursor.fetchone()
    print(existing_entry)

    if existing_entry:
        # If the account exists, update the status
        qry_update_status = "UPDATE deletestatus SET status = 1 WHERE account = %s"
        values = (account,)
        cursor.execute(qry_update_status, values)
        conn.commit()
        messagebox.showinfo("Delete status", "Existing delete request updated successfully")
    else:
        # If the account doesn't exist, insert a new entry
        qry_insert_status = "INSERT INTO deletestatus (account,status) VALUES (%s, 1)"
        values = (account,)
        cursor.execute(qry_insert_status, values)
        conn.commit()
        messagebox.showinfo("Delete status", "Delete Request sent successfully")


def approve_deletion(account):
    conn = mysql.connector.connect(host="localhost", user="root", password="12345678", database="bank")
    cursor = conn.cursor()
    qry_update_status = "UPDATE deletestatus SET status = 2 WHERE account = %s"
    cursor.execute(qry_update_status, (account,))
    conn.commit()
    cursor.close()
    conn.close()
    messagebox.showinfo("Deletion", f"Account {account} has been deleted.")
    delete_customer_account(account)


def delete_customer_account(account):
    conn = mysql.connector.connect(host="localhost", user="root", password="12345678", database="bank")
    cursor = conn.cursor()

    # Check if the account exists in the customer table
    qry_check_account = "SELECT * FROM customer WHERE account = %s"
    cursor.execute(qry_check_account, (account,))
    existing_account = cursor.fetchone()

    if existing_account:
        # Delete the account from the customer table
        qry_delete_customer = "DELETE FROM customer WHERE account = %s"
        cursor.execute(qry_delete_customer, (account,))
        messagebox.showinfo("Delete status", "Customer account deleted successfully")
    else:
        messagebox.showinfo("Delete status", "Customer account not found")

    conn.commit()
    cursor.close()
    conn.close()

def empdelete():
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"./build8/assets/frame0")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window8 = Toplevel(window)
    window8.title("Delete Account")
    window8.geometry("800x600")
    window8.configure(bg="#1F43A0")

    canvas = Canvas(
        window8,
        bg="#1F43A0",
        height=600,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        400.0,
        45.0,
        image=image_image_1
    )

    canvas.create_text(
        85.0,
        25.0,
        anchor="nw",
        text="Delete",
        fill="#000000",
        font=("Inter Bold", 40 * -1)
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        54.0,
        51.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        401.0,
        347.0,
        image=image_image_3
    )

    conn = mysql.connector.connect(host="localhost", user="root", password="12345678", database="bank")
    cursor = conn.cursor()
    qry = "SELECT account FROM deletestatus WHERE status = 1"
    cursor.execute(qry)
    delete_requests = cursor.fetchall()
    cursor.close()
    conn.close()
    # Display delete requests in the GUI
    row_height = 100
    for idx, (account_number,) in enumerate(delete_requests):
        canvas.create_text(
            100.0,
            150 + idx * row_height,
            anchor="nw",
            text=f"Account: {account_number}",
            fill="#FFFFFF",
            font=("Inter Bold", 26 * -1)
        )

        # Approve Button
        approve_button = Button(
            window8,
            text=f"Approve Deletion {idx + 1}",
            command=lambda acc=account_number: approve_deletion(acc),
            relief="flat"
        )
        approve_button.place(
            x=400.0,
            y=150 + idx * row_height,
            width=155.0,
            height=44.0
        )
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))    
    button_1 = Button(
        window8,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=4,
        command=window8.withdraw,
        relief="flat"
    )
    button_1.place(
        x=329.0,
        y=537.0,
        width=155.0,
        height=44.0
    )
    window8.resizable(False, False)
    window8.mainloop()



def support():
        nw4=Toplevel(window)
        nw4.geometry("600x500")
        nw4.title("Customer Support")
        ctk.set_appearance_mode("light")
        nw4.config(bg='blue4')
        framemsg=ctk.CTkFrame(master=nw4,width=100,height=100,corner_radius=15,fg_color='ivory2')
        framemsg.pack(pady=20,padx=40,fill="both",expand=True)
        actext=ctk.CTkLabel(master=framemsg,text='''Thank you for reaching us,

    for further help
    
        contact:4563728913
        or
        email:customerhelp@gmail.com''',font=("Arial",20),text_color='black')
        actext.pack(pady=20,padx=40)
        userimg=Image.open("./DBMSPROJ/custserv.png")
        resized=userimg.resize((200,200),Image.ANTIALIAS)
        tk_image = ImageTk.PhotoImage(resized)
        labeluser=tk.Label(framemsg,image=tk_image)
        labeluser.image=tk_image
        labeluser.place(x=150,y=200)
        
def register():
    global a
    a=randint(100000000,999999999)
    name=entry3.get()
    address=entry4.get()
    email=entry5.get()
    phone=entry6.get()
    age=entry7.get()
    password=entry8.get()
    account=a
    if(name=="" or address=="" or email=="" or phone=="" or age=="" or password=="" ):
        messagebox.showwarning("Insert Status","All fields required")
    else:
        conn=mysql.connector.connect(host="localhost",user="root",password="12345678",database="bank")
        cursor=conn.cursor()
        query = "INSERT INTO customer VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (name, address, email, phone, age, password, account)
        cursor.execute("select * from customer")
        rows=cursor.fetchall()
        for row in rows:
            if row[0]==name:
                entry3.delete(0,'end')
                entry4.delete(0,'end')
                entry5.delete(0,'end')
                entry6.delete(0,'end')
                entry7.delete(0,'end')
                entry8.delete(0,'end')
                messagebox.showwarning("Insert Status","Account already exists")
                cursor.close()
                conn.close
                  
        cursor.execute(query, values)
        conn.commit()
        entry3.delete(0,'end')
        entry4.delete(0,'end')
        entry5.delete(0,'end')
        entry6.delete(0,'end')
        entry7.delete(0,'end')
        entry8.delete(0,'end')
        conn.close()
        nw3=Toplevel(window)
        nw3.geometry("400x400")
        nw3.title("Insert Status")
        ctk.set_appearance_mode("light")
        framemsg=ctk.CTkFrame(master=nw3,width=600,height=600,corner_radius=15,fg_color='ivory2')
        framemsg.pack(pady=0,padx=0,fill="both",expand=True)
        actext=ctk.CTkLabel(master=framemsg,text='''Registration Successfull!!
        Account Number is:''',font=("TkHeading",15),text_color='black')
        actext.pack(pady=20,padx=40)
        label9=ctk.CTkLabel(master=framemsg,text=a,font=("TkHeading",26),text_color='black')
        label9.pack(pady=20,padx=40)
def transaction():
    # Backend
    # python functions code starts :
    con=mysql.connector.connect(host="localhost",user="root",password="12345678",database="bank")
    cur=con.cursor()

    Query1="Create table if not exists transaction (accno integer primary key,balance integer);"
    cur.execute(Query1)
    con.commit()

    query4="select * from customer"
    cur.execute(query4)
    data1=cur.fetchall()

    for row in data1:   
        if (row[6]==account):
        # Check if the record already exists
            query_check = "SELECT 1 FROM transaction WHERE accno = %s LIMIT 1"
            values1 = (account,)
            cur.execute(query_check, values1)
            exists = cur.fetchone()
            if not exists:
                # Record doesn't exist, so insert a new record
                query5 = "INSERT INTO transaction (accno,balance) values(%s,0)"
                values = (account,)
                cur.execute(query5, values)
                con.commit()
            else:
                break

    query3="select * from transaction"
    cur.execute(query3)
    data2=cur.fetchall()
    con.close()
    def create_transaction_table(accno):
        con=mysql.connector.connect(host="localhost",user="root",password="12345678",database="bank")
        cur=con.cursor()
        table_name = f"transaction_{accno}"
        cur.execute(f"SHOW TABLES LIKE '{table_name}'")
        table_exists = cur.fetchall()
        if not table_exists:
            query2 = f"""
            CREATE TABLE if not exists {table_name} (
                transaction_id INT AUTO_INCREMENT PRIMARY KEY,
                credited DECIMAL(10, 2),
                debited DECIMAL(10, 2),
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
            cur.execute(query2)
            con.commit()

    for row in data2:
        create_transaction_table(row[0])

    def fetchtransac(accno): 
        cur=con.cursor()
        table_name = f"transaction_{accno}"
        cur.execute(f"SHOW TABLES LIKE '{table_name}'")
        table_exists = cur.fetchall()
        if table_exists:
            cur.execute(f'select * from transaction_{accno}')
            transaccno=cur.fetchall()
            con.commit()
            return transaccno

    con=mysql.connector.connect(host="localhost",user="root",password="12345678",database="bank")
    cur=con.cursor()
    global bal
    x="select balance from transaction where accno=%s"
    cur.execute(x, (account,))
    bal=cur.fetchone()[0]
    bal =float(bal)
    
    #backend ends
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"./build1/assets/frame0")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    '''window1 = Toplevel(window)
    window1.title("Transaction")
    window1.configure(bg="#000000")'''
    def update_balance_label():
            global bal
            canvas.itemconfig(tagOrId=balance_labelm, text=bal)
    def deposit():
        global bal
        OUTPUT_PATH2 = Path(__file__).parent
        ASSETS_PATH2 = OUTPUT_PATH2 / Path(r"./build2/assets/frame0")

        def relative_to_assets2(path: str) -> Path:
            return ASSETS_PATH2 / Path(path)

        nwindow = Toplevel(window)
        nwindow.title("Deposit")
        nwindow.geometry("450x500")
        nwindow.configure(bg = "#1F43A0")

        def depbalance_update(entry_value):
            global bal
            try:
                # Convert the string to a float
                amount_to_deposit = float(entry_value)
                insert_query = "INSERT INTO transaction_"+str(account)+ "  (credited, debited) VALUES (%s, %s)"
                data = (amount_to_deposit, 0)
                cur.execute(insert_query, data)
                bal=bal+amount_to_deposit
                q = f"UPDATE transaction SET balance = {bal} WHERE accno = '{account}'"
                cur.execute(q)
                con.commit()
                canvas.itemconfig(tagOrId=balance_label,text=bal)
                q
                
            except ValueError:
                messagebox.showwarning("Invalid input","Please enter a valid number.")
                #amount_to_deposit = float(entry_value)
        canvas = Canvas(
            nwindow,
            bg = "#1F43A0",
            height = 500,
            width = 450,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        image_image_12 = PhotoImage(
            file=relative_to_assets2("image_12.png"))
        image_2 = canvas.create_image(
            225.0,
            46.0,
            image=image_image_12
        )

        canvas.create_text(
            94.0,
            17.0,
            anchor="nw",
            text="Deposit",
            fill="#000000",
            font=("Inter Bold", 40 * -1)
        )

        image_image_22 = PhotoImage(
            file=relative_to_assets2("image_22.png"))
        image_22 = canvas.create_image(
            191.0,
            355.0,
            image=image_image_22
        )

        canvas.create_text(
            75.0,
            268.0,
            anchor="nw",
            text="Enter amount to deposit",
            fill="#FFFFFF",
            font=("Inter Bold", 25 * -1)
        )

        button_image_12 = PhotoImage(
            file=relative_to_assets2("button_12.png"))
        button_12 = Button(
            nwindow,
            image=button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:(nwindow.withdraw(),update_balance_label()),
            relief="flat"
        )
        button_12.place(
            x=146.0,
            y=424.0,
            width=155.0,
            height=44.0
        )

        image_image_32 = PhotoImage(
            file=relative_to_assets2("image_32.png"))
        image_32 = canvas.create_image(
            222.0,
            223.0,
            image=image_image_32
        )

        image_image_42 = PhotoImage(
            file=relative_to_assets2("image_42.png"))
        image_42 = canvas.create_image(
            213.0,
            151.0,
            image=image_image_42
        )

        image_image_52 = PhotoImage(
            file=relative_to_assets2("image_52.png"))
        image_52 = canvas.create_image(
            50.0,
            47.0,
            image=image_image_52
        )


        balance_label=canvas.create_text(
            88.0,
            201.0,
            anchor="nw",
            text=str(bal),
            fill="#000000",
            font=("Inter", 26 * -1)
        )

        entry_image_12 = PhotoImage(
            file=relative_to_assets2("entry_12.png"))
        entry_bg_12 = canvas.create_image(
            194.0,
            355.5,
            image=entry_image_12
        )
        entry_12 = Entry(
            nwindow,
            bd=0,
            bg="#AEC0FF",
            highlightthickness=0
        )
        entry_12.place(
            x=85.0,
            y=335.0,
            width=218.0,
            height=39.0
        )
        button_image_22 = PhotoImage(
            file=relative_to_assets2("button_22.png"))
        button_22 = Button(
            nwindow,
            image=button_image_22,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:depbalance_update(entry_12.get()),
            relief="flat"
        )
        button_22.place(
            x=346.0,
            y=331.0,
            width=49.0,
            height=49.0
        )
        nwindow.resizable(False, False)
        nwindow.mainloop()

    def withdraw():
        global bal
        OUTPUT_PATH3 = Path(__file__).parent
        ASSETS_PATH3 = OUTPUT_PATH3 / Path(r"./build3/assets/frame0")

        def relative_to_assets3(path: str) -> Path:
            return ASSETS_PATH3 / Path(path)

        newindow = Toplevel(window)
        newindow.title("Withdraw")
        newindow.geometry("450x500")
        newindow.configure(bg = "#1F43A0")
        def depbalance_update(entry_value):
            global bal
            try:
                # Convert the string to a float
                amount_to_withdraw = float(entry_value)
                try:
                    if(bal>amount_to_withdraw):
                        insert_query = "INSERT INTO transaction_"+str(account)+ " (credited, debited) VALUES (%s, %s)"
                        data = (0, amount_to_withdraw)
                        cur.execute(insert_query, data)
                        bal=bal-amount_to_withdraw
                        q = f"UPDATE transaction SET balance = {bal} WHERE accno = '{account}'"
                        cur.execute(q)
                        con.commit()
                        canvas.itemconfig(tagOrId=balance_label,text=bal)
                    else:
                        messagebox.showwarning("Insufficient funds","Not enough balance.")
                except ValueError:
                    messagebox.showwarning("Insufficient funds","Not enough balance.")
            except ValueError:
                    messagebox.showwarning("Invalid input","Please enter a valid number.")
                #amount_to_deposit = float(entry_value)
        canvas = Canvas(
            newindow,
            bg = "#1F43A0",
            height = 500,
            width = 450,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        image_image_13 = PhotoImage(
            file=relative_to_assets3("image_13.png"))
        image_13 = canvas.create_image(
            225.0,
            45.0,
            image=image_image_13
        )

        canvas.create_text(
            94.0,
            19.0,
            anchor="nw",
            text="Withdraw",
            fill="#000000",
            font=("Inter Bold", 40 * -1)
        )

        image_image_23 = PhotoImage(
            file=relative_to_assets3("image_23.png"))
        image_23 = canvas.create_image(
            191.0,
            355.0,
            image=image_image_23
        )

        entry_image_13 = PhotoImage(
            file=relative_to_assets3("entry_13.png"))
        entry_bg_13 = canvas.create_image(
            194.0,
            355.5,
            image=entry_image_13
        )
        entry_13 = Entry(
            newindow,
            bd=0,
            bg="#AEC0FF",
            fg="#000000",
            highlightthickness=0
        )
        entry_13.place(
            x=85.0,
            y=335.0,
            width=218.0,
            height=39.0
        )

        button_image_13 = PhotoImage(
            file=relative_to_assets3("button_13.png"))
        button_13 = Button(
            newindow,
            image=button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:depbalance_update(entry_13.get()),
            relief="flat"
        )
        button_13.place(
            x=346.0,
            y=331.0,
            width=49.0,
            height=49.0
        )

        canvas.create_text(
            63.0,
            259.0,
            anchor="nw",
            text="Enter amount to withdraw :",
            fill="#FFFFFF",
            font=("Inter Bold", 25 * -1)
        )

        button_image_23 = PhotoImage(
            file=relative_to_assets3("button_23.png"))
        button_23 = Button(
            newindow,
            image=button_image_23,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:(newindow.withdraw(),update_balance_label()),
            relief="flat"
        )
        button_23.place(
            x=148.0,
            y=424.0,
            width=155.0,
            height=44.0
        )

        image_image_33 = PhotoImage(
            file=relative_to_assets3("image_33.png"))
        image_33 = canvas.create_image(
            226.0,
            207.0,
            image=image_image_33
        )

        balance_label=canvas.create_text(
            88.0,
            186.0,
            anchor="nw",
            text=str(bal),
            fill="#000000",
            font=("Inter", 26 * -1)
        )

        image_image_43 = PhotoImage(
            file=relative_to_assets3("image_43.png"))
        image_43 = canvas.create_image(
            50.0,
            48.0,
            image=image_image_43
        )

        image_image_53 = PhotoImage(
            file=relative_to_assets3("image_53.png"))
        image_53 = canvas.create_image(
            212.0,
            142.0,
            image=image_image_53
        )
        newindow.resizable(False, False)
        newindow.mainloop()

    def transhis():
        OUTPUT_PATH4 = Path(__file__).parent
        ASSETS_PATH4 = OUTPUT_PATH4 / Path(r"./build4/assets/frame0")

        table_columns = ["Transaction_id", "Credited", "Debited","TimeStamp"]
        table_data = fetchtransac(account)
        newwindow = Toplevel(window)
        newwindow.geometry("900x650")
        newwindow.configure(bg = "#1F43A0")
               
        def relative_to_assets4(path: str) -> Path:
            return ASSETS_PATH4 / Path(path)
        
        canvas = Canvas(
            newwindow,
            bg = "#1F43A0",
            height = 650,
            width = 900,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        table= ttk.Treeview(master=newwindow,columns=table_columns,show="headings")
        for column in table_columns:
            table.heading(column= column,text=column,anchor='center')
            table.column(column=column,width=70,anchor='center')
        for row_data in table_data:
            table.insert(parent="",index="end",values=row_data)
        table.pack()
        style= ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",background="#AEC0FF")
        table.place(x=100.0,y=220.0, height=300, width=700) 

        canvas.place(x = 0, y = 0)

        image_image_14 = PhotoImage(
            file=relative_to_assets4("image_14.png"))
        image_14 = canvas.create_image(
            500.0,
            45.0,
            image=image_image_14
        )
        canvas.create_text(
            94.0,
            16.0,
            anchor="nw",
            text="Transactions History",
            fill="#000000",
            font=("Inter Bold", 40 * -1)
        )

        button_image_14 = PhotoImage(
            file=relative_to_assets4("button_14.png"))
        button_14 = Button(
            newwindow,
            image=button_image_14,
            borderwidth=0,
            highlightthickness=0,
            command=newwindow.withdraw,
            relief="flat"
        )
        button_14.place(
            x=372.0,
            y=569.0,
            width=155.0,
            height=44.0
        )

        image_image_24 = PhotoImage(
            file=relative_to_assets4("image_24.png"))
        image_24 = canvas.create_image(
            450.0,
            370.0,
            image=image_image_24
        )

        image_image_34 = PhotoImage(
            file=relative_to_assets4("image_34.png"))
        image_34 = canvas.create_image(
            43.0,
            43.0,
            image=image_image_34
        )

        canvas.create_text(
            76.0,
            121.0,
            anchor="nw",
            text="Last transactions :",
            fill="#FFFFFF",
            font=("Inter Bold", 30 * -1)
        ) 

        newwindow.resizable(False, False)
        newwindow.mainloop()

    def transferacc():
        global bal
        global destination_account
        OUTPUT_PATH5 = Path(__file__).parent
        ASSETS_PATH5 = OUTPUT_PATH5 / Path(r"./build5/assets/frame0")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH5 / Path(path)

        newwwindow = Toplevel(window)
        newwwindow.title("Transfer")
        newwwindow.geometry("800x600")
        newwwindow.configure(bg = "#1F43A0")

        def desaccno(entry_value):
            global destination_account
            destination_account = entry_value
            print(destination_account)

        def depbalance_update(entry_value):
            global bal
            try:
                # Convert the string to a float
                amount_to_transfer = float(entry_value)
                try:
                    conn=mysql.connector.connect(host="localhost",user="root",password="12345678",database="bank")
                    cur=conn.cursor()
                    cur.execute(f"SELECT accno FROM transaction WHERE accno = '{destination_account}'")
                    if cur.fetchone() is None:
                        messagebox.showwarning("Invalid destination account", "Please enter a valid destination account.")
                    if(bal>amount_to_transfer>0):
                        insert_query = "INSERT INTO transaction_"+str(account)+ " (credited, debited) VALUES (%s, %s)"
                        data = (0,amount_to_transfer)
                        cur.execute(insert_query, data)
                        conn.commit()
                        insert_query2 = "INSERT INTO transaction_"+str(destination_account)+ " (credited, debited) VALUES (%s, %s)"
                        data = (amount_to_transfer,0)
                        cur.execute(insert_query2, data)
                        conn.commit()
                        bal=bal-amount_to_transfer
                        q = f"UPDATE transaction SET balance = {bal} WHERE accno = '{account}'"
                        cur.execute(q)
                        conn.commit()
                        cur.execute(f"SELECT balance FROM transaction WHERE accno = '{destination_account}'")
                        destination_balance = float(cur.fetchone()[0])
                        destination_balance += amount_to_transfer
                        q2 = f"UPDATE transaction SET balance = {destination_balance} WHERE accno = '{destination_account}'"
                        cur.execute(q2)
                        conn.commit()
                        canvas.itemconfig(tagOrId=balance_label,text=bal)
                    else:
                        messagebox.showwarning("Insufficient funds","Not enough balance.")
                except ValueError:
                    messagebox.showwarning("Insufficient funds","Not enough balance.")
            except ValueError:
                messagebox.showwarning("Invalid input","Please enter a valid number.")
                #amount_to_deposit = float(entry_value)
        canvas = Canvas(
            newwwindow,
            bg = "#1F43A0",
            height = 600,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        image_image_15 = PhotoImage(
            file=relative_to_assets("image_15.png"))
        image_15 = canvas.create_image(
            515.0,
            45.0,
            image=image_image_15
        )

        canvas.create_text(
            94.0,
            25.0,
            anchor="nw",
            text="Transfer to Another Account",
            fill="#000000",
            font=("Inter Bold", 40 * -1)
        )

        image_image_25 = PhotoImage(
            file=relative_to_assets("image_25.png"))
        image_25 = canvas.create_image(
            520.0,
            447.0,
            image=image_image_25
        )

        image_image_35 = PhotoImage(
            file=relative_to_assets("image_35.png"))
        image_35 = canvas.create_image(
            543.0,
            314.0,
            image=image_image_35
        )

        entry_image_15 = PhotoImage(
            file=relative_to_assets("entry_15.png"))
        entry_bg_15 = canvas.create_image(
            542.0,
            316.0,
            image=entry_image_15
        )
        entry_15= Entry(
            newwwindow,
            bd=0,
            bg="#8DA6FF",
            highlightthickness=0
        )
        entry_15.place(
            x=423.0,
            y=297.0,
            width=238.0,
            height=36.0
        )

        balance_label=canvas.create_text(
            393.0,
            428.0,
            anchor="nw",
            text=str(bal),
            fill="#000000",
            font=("Inter", 22 * -1)
        )

        image_image_45 = PhotoImage(
            file=relative_to_assets("image_45.png"))
        image_45 = canvas.create_image(
            545.0,
            180.0,
            image=image_image_45
        )

        image_image_55 = PhotoImage(
            file=relative_to_assets("image_55.png"))
        image_55 = canvas.create_image(
            244.0,
            448.0,
            image=image_image_55
        )

        button_image_15 = PhotoImage(
            file=relative_to_assets("button_15.png"))
        button_15 = Button(
            newwwindow,
            image=button_image_15,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:(newwwindow.withdraw(),update_balance_label()),
            relief="flat"
        )
        button_15.place(
            x=325.0,
            y=526.0,
            width=155.0,
            height=44.0
        )

        canvas.create_text(
            46.0,
            284.0,
            anchor="nw",
            text="Enter amount to Transfer :",
            fill="#FFFFFF",
            font=("Inter Bold", 26 * -1)
        )

        canvas.create_text(
            46.0,
            156.0,
            anchor="nw",
            text="Enter Account Number to\nTransfer to :",
            fill="#FFFFFF",
            font=("Inter Bold", 25 * -1)
        )

        image_image_65 = PhotoImage(
            file=relative_to_assets("image_65.png"))
        image_65 = canvas.create_image(
            50.0,
            45.0,
            image=image_image_65
        )
        
        entry_image_25 = PhotoImage(
            file=relative_to_assets("entry_25.png"))
        entry_bg_25 = canvas.create_image(
            543.0,
            181.0,
            image=entry_image_25
        )
        entry_25 = Entry(
            newwwindow,
            bd=0,
            bg="#8DA6FF",
            highlightthickness=0
        )
        entry_25.place(
            x=424.0,
            y=162.0,
            width=238.0,
            height=36.0
        )
        '''
        button_image_35 = PhotoImage(
            file=relative_to_assets("button_35.png"))
        button_35 = Button(
            newwwindow,
            image=button_image_35,
            borderwidth=0,
            highlightthickness=0,amda

            command=lambda:desaccno(entry_15.get()) ,
            relief="flat"
        )
        button_35.place(
            x=716.0,
            y=150.0,
            width=60.0,
            height=60.0
        )
        '''
        button_image_25 = PhotoImage(
            file=relative_to_assets("button_25.png"))
        button_25 = Button(
            newwwindow,
            image=button_image_25,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:(desaccno(entry_25.get()),depbalance_update(entry_15.get())),
            relief="flat"
        )
        
        button_25.place(
            x=716.0,
            y=284.0,
            width=60.0,
            height=60.0
        )

        newwwindow.resizable(False, False)
        newwwindow.mainloop()

    window1 = Toplevel(window)
    window1.title("Transfer")
    window1.geometry("900x600")
    window1.configure(bg = "#1F43A0")
    canvas = Canvas(
    window1,
    bg = "#1F43A0",
    height = 600,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
    400.0,
    45.0,
    image=image_image_1
    )

    canvas.create_text(
    94.0,
    16.0,
    anchor="nw",
    text="Transactions",
    fill="#000000",
    font=("Inter Bold", 40 * -1)
    )

    image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
    46.0,
    46.0,
    image=image_image_2
    )

    image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
    361.0,
    456.0,
    image=image_image_3
    )

    image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
    113.0,
    456.0,
    image=image_image_4
    )
    
    button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
    button_1 = Button(
    window1,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=deposit,
    relief="flat"
    )
    button_1.place(
    x=583.0,
    y=131.0,
    width=270.0,
    height=70.0
    )

    canvas.create_rectangle(
    44.0,
    140.0,
    464.0,
    372.0,
    fill="#AEBFFF",
    outline="")

    button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
    button_2 = Button(
    window1,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=window1.withdraw,
    relief="flat"
    )
    button_2.place(
    x=395.0,
    y=527.0,
    width=155.0,
    height=44.0
    )

    button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
    button_3 = Button(
    window1,
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=withdraw,
    relief="flat"
    )
    button_3.place(
    x=583.0,
    y=231.0,
    width=270.0,
    height=70.0
    )

    button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
    button_4 = Button(
    window1,
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=transhis,
    relief="flat"
    )
    button_4.place(
    x=583.0,
    y=333.0,
    width=270.0,
    height=70.0
    )

    button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
    button_5 = Button(
    window1,
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=transferacc,
    relief="flat"
    )
    button_5.place(
    x=583.0,
    y=435.0,
    width=270.0,
    height=70.0
    )
    cur.execute("select * from customer")
    rows=cur.fetchall()
    for row in rows:
        if row[5]==password:
            a=row[0]
            b=row[3]
            c=row[4]
    canvas.create_text(
    60.0,
    150.0,
    anchor="nw",
    text="Account No. : "+str(account)+"\n\nName : "+str(a)+"\n\nPhone No. : "+str(c)+"\n\nEmail : "+str(b),
    fill="#000000",
    font=("Inter Bold", 26 * -1)
    )

    balance_labelm=canvas.create_text(
    235.0,
    435.0,
    anchor="nw",
    text=str(bal),
    fill="#000000",
    font=("Inter Bold", 26 * -1)
    )
    window1.resizable(False, False)
    window1.mainloop()
        
def menupg():
    conn=mysql.connector.connect(host="localhost",user="root",password="12345678",database="bank")
    cursor=conn.cursor()
    newindow2=Toplevel(window)
    newindow2.geometry("1280x650")
    newindow2.title("Menu Page")
    ctk.set_appearance_mode("light")
    newindow2.config(bg='blue4')
    ctk.set_default_color_theme("blue")
    frame3=ctk.CTkFrame(master=newindow2,width=600,height=600,corner_radius=15,fg_color='ivory2')
    frame3.pack(pady=50,padx=150,fill="both",expand=True)
    label7=ctk.CTkLabel(master=frame3,text="MAIN MENU",font=("TkHeading",30,'bold'),text_color='black')
    label7.pack(pady=20,padx=40)
    def back():
        newindow2.withdraw()
    userimg=Image.open("./DBMSPROJ/user1.png")
    resized=userimg.resize((200,200),Image.ANTIALIAS)
    tk_image = ImageTk.PhotoImage(resized)
    labeluser=tk.Label(frame3,image=tk_image)
    labeluser.image=tk_image
    labeluser.place(x=40,y=30)
    cursor.execute("select * from customer")
    rows=cursor.fetchall()
    for row in rows:
        if row[5]==password:
            labelname=ctk.CTkLabel(master=frame3,text="Name: "+row[0],font=("Arial",22),text_color='black')
            labelname.place(y=300,x=40)
            labelage=ctk.CTkLabel(master=frame3,text="Age: "+str(row[4]),font=("Arial",22),text_color='black')
            labelage.place(y=330,x=40)
            labelemail=ctk.CTkLabel(master=frame3,text="Email: "+row[2],font=("Arial",22),text_color='black')
            labelemail.place(y=360,x=40)
            label8=ctk.CTkLabel(master=frame3,text="Account number: "+account,font=("Arial",22),text_color='black')
            label8.place(y=390,x=40)
       
    button8=ctk.CTkButton(master=frame3,text="Transactions",command=transaction,height=100,width=375)
    button8.place(y=100,x=550)
    button9=ctk.CTkButton(master=frame3,text="Loan Request ",command=loanstatus,height=100,width=100)
    button9.place(y=250,x=525)
    buttonams=ctk.CTkButton(master=frame3,text="Loan Status",command=lstat,height=100,width=100)
    buttonams.place(y=250,x=650)
    button10=ctk.CTkButton(master=frame3,text="Request Account Deletion",command=deletestatus,height=100,width=130)
    button10.place(y=250,x=775)
    buttonexit=ctk.CTkButton(master=frame3,text="Exit",command=back,height=50,width=100)
    buttonexit.place(y=400,x=750)
    button11=ctk.CTkButton(master=frame3,text="Customer Support",command=support,height=50,width=130)
    button11.place(y=400,x=575)
    
def clogin():
    global account,password
    createtable()
    account=entry1.get()
    password=entry2.get()
    
    if not(account and password):
        messagebox.showwarning('Error','Enter all fields')
    elif (not(accountexist())):
        messagebox.showwarning('Error','Account or Password incorrect')
    else:
        entry1.delete(0,'end')
        entry2.delete(0,'end')
        menupg()
def csign():
    global entry3,entry4,entry5,entry6,entry7,entry8,newindow1
    newindow1=Toplevel(window)
    newindow1.geometry("925x925")
    newindow1.title("cutomer signin")
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")
    def show():
        if entry8.cget('show')=='*':
            entry8.configure(show='')

        else:
            entry8.configure(show='*')
    def back():
        newindow1.withdraw()
    frame2=ctk.CTkScrollableFrame(master=newindow1,width=470,height=510,corner_radius=15,fg_color='lemon chiffon')
    frame2.pack(pady=0,padx=0,fill="both",expand=True)
    label6=ctk.CTkLabel(master=frame2,text="Customer Registeration",font=("Helvetica",26),text_color='black')
    label6.pack(pady=20,padx=10)
    labelname=ctk.CTkLabel(master=frame2,text="Name:",font=("Arial",18),text_color='black')
    labelname.place(y=85,x=190)
    entry3=ctk.CTkEntry(master=frame2,width=300,placeholder_text="FullName")
    entry3.pack(pady=20,padx=10)
    labelad=ctk.CTkLabel(master=frame2,text="Address:",font=("Arial",18),text_color='black')
    labelad.place(y=155,x=190)
    entry4=ctk.CTkEntry(master=frame2,width=220,placeholder_text="Address")
    entry4.pack(pady=20,padx=15)
    labelem=ctk.CTkLabel(master=frame2,text="Email:",font=("Arial",18),text_color='black')
    labelem.place(y=225,x=190)
    entry5=ctk.CTkEntry(master=frame2,width=220,placeholder_text="Email")
    entry5.pack(pady=20,padx=15)
    labelph=ctk.CTkLabel(master=frame2,text="Phoneno:",font=("Arial",18),text_color='black')
    labelph.place(y=295,x=190)
    entry6=ctk.CTkEntry(master=frame2,width=220,placeholder_text="Mobilenumber")
    entry6.pack(pady=20,padx=15)
    labelag=ctk.CTkLabel(master=frame2,text="Age:",font=("Arial",18),text_color='black')
    labelag.place(y=365,x=190)
    entry7=ctk.CTkEntry(master=frame2,width=220,placeholder_text="Age")
    entry7.pack(pady=20,padx=15)
    label6=ctk.CTkLabel(master=frame2,text="Create Password:",font=("Helvetica",16),text_color='black')
    label6.pack(pady=20,padx=10)
    entry8=ctk.CTkEntry(master=frame2,width=220,placeholder_text="Password",show='*')
    entry8.pack(pady=20,padx=15)
    button7=ctk.CTkCheckBox(master=frame2,text="Show/Hide",command=show)
    button7.pack(pady=20,padx=15)
    button6=ctk.CTkButton(master=frame2,text="Register",command=register)
    button6.pack(pady=20,padx=15)
    buttonback=ctk.CTkButton(master=frame2,text="Back",command=back)
    buttonback.pack(pady=20,padx=15)
    userimg=Image.open("./DBMSPROJ/cust1.png")
    resized=userimg.resize((200,200),Image.ANTIALIAS)
    tk_image = ImageTk.PhotoImage(resized)
    labelcust=tk.Label(frame2,image=tk_image)
    labelcust.image=tk_image
    labelcust.place(x=660,y=30)
    newindow1.resizable(False,False)
def search():
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"./build7/assets/frame0")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window7 = Toplevel(window)
    window7.title("Search for Customer Account")
    window7.geometry("900x600")
    window7.configure(bg = "#1F43A0")

    canvas = Canvas(
        window7,
        bg = "#1F43A0",
        height = 600,
        width = 900,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        390.0,
        45.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        60.0,
        44.0,
        image=image_image_2
    )

    canvas.create_text(
        100.0,
        20.0,
        anchor="nw",
        text="SEARCH ACCOUNT ",
        fill="#000000",
        font=("Inter Bold", 40 * -1)
    )

    canvas.create_rectangle(
        44.0,
        128.0,
        506.0,
        503.0,
        fill="#AEBFFF",
        outline="")

    canvas.create_text(
        560.0,
        257.0,
        anchor="nw",
        text="ENTER ACCOUNT NO.",
        fill="#FFFFFF",
        font=("Inter Bold", 26 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        684.0,
        315.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        window7,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=2
    )
    entry_1.place(
        x=550.0,
        y=297.0,
        width=268.0,
        height=35.0
    )
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        window7,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=window7.withdraw,
        relief="flat"
    )
    button_1.place(
        x=389.0,
        y=527.0,
        width=155.0,
        height=44.0
    )
    def searchacc(accno):
        try:
            acc = float(accno)
            conn=mysql.connector.connect(host="localhost",user="root",password="12345678",database="bank")
            cur=conn.cursor()
            cur.execute("select * from customer where account=%s",(acc,))
            rows=cur.fetchall()
            for row in rows:
                #if row[5]==password:
                a=row[0]
                d=accno
                b=row[3]
                c=row[2]
                e=row[1]
                f=row[4]
            canvas.create_text(
            210.0,
            150.0,
            anchor="nw",
            text="\n\n      "+str(d)+"\n\n      "+str(a)+"\n\n      "+str(b)+"\n\n      "+str(c)+"\n\n      "+str(e)+"\n\n      "+str(f),
            fill="#000000",
            font=("Inter Bold", 18 * -1)
            )
        except ValueError:
            messagebox.showwarning("Invalid input","Please enter a valid account number.")

    button_image_13 = PhotoImage(
                file=relative_to_assets("button_13.png"))
    button_13 = Button(
        window7,
        image=button_image_13,
        borderwidth=0,
        highlightthickness=0,
        command=lambda:searchacc(entry_1.get()),
        relief="flat"
    )
    button_13.place(
        x=830.0,
        y=292.0,
        width=49.0,
        height=49.0
    )
    canvas.create_text(
        75.0,
        177.0,
        anchor="nw",
        text="Account no:",
        fill="#000000",
        font=("Inter Bold", 26 * -1)
    )

    canvas.create_text(
        80.0,
        221.0,
        anchor="nw",
        text="User Name:",
        fill="#000000",
        font=("Inter Bold", 26 * -1)
    )

    canvas.create_text(
        100.0,
        265.0,
        anchor="nw",
        text="Phone No:",
        fill="#000000",
        font=("Inter Bold", 26 * -1)
    )

    canvas.create_text(
        152.0,
        311.0,
        anchor="nw",
        text="Email:",
        fill="#000000",
        font=("Inter Bold", 26 * -1)
    )

    canvas.create_text(
        115.0,
        353.0,
        anchor="nw",
        text="Address:",
        fill="#000000",
        font=("Inter Bold", 26 * -1)
    )

    canvas.create_text(
        169.0,
        397.0,
        anchor="nw",
        text="Age:",
        fill="#000000",
        font=("Inter Bold", 26 * -1)
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        352.0,
        315.0,
        image=image_image_3
    )

    window7.resizable(False, False)
    window7.mainloop()
def update():
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"./build6/assets/frame0")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window6 = Toplevel(window)
    window6.title("Delete Customer Account")
    window6.geometry("900x600")
    window6.configure(bg = "#1F43A0")

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345678',
        database='bank',
        autocommit=True
    )

    cursor = connection.cursor()
    def update_details(acc_value,newuser,newaddr,newage,newno,newmail):
        try:
            accno =acc_value
            new_name = newuser
            new_address =newaddr
            new_age = newage
            new_phone = newno
            new_mail=newmail

            #Check if there is no input for any field, and retrieve the existing values
            if not new_age:
                new_age = get_existing_value(accno, 'age')
            if not new_mail:
                new_mail = get_existing_value(accno, 'email')
            if not new_phone:
                new_phone = get_existing_value(accno, 'phone')
            if not new_address:
                new_address = get_existing_value(accno, 'address')
            if not new_name:
                new_name = get_existing_value(accno, 'name')

            cursor = connection.cursor()
            update_query = "UPDATE customer SET age = %s, phone = %s, address = %s, name = %s, email= %s WHERE account = %s"
            cursor.execute(update_query, (new_age, new_phone, new_address, new_name, new_mail,accno))
            

            connection.commit()
            cursor.close()
            connection.close()


            print("Update successful")

            # Display a pop-up box indicating the success of the update
            messagebox.showinfo("Success", "Update successful!")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            feedback_label.config(text="Update failed. Check logs for details.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            feedback_label.config(text="Update failed. Check logs for details.")


    def get_existing_value(acc_no, field):
        # Function to retrieve the existing value for a given field
        cursor = connection.cursor()
        select_query = f"SELECT {field} FROM customer WHERE account = %s"
        cursor.execute(select_query, (acc_no,))
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else None


    canvas = Canvas(
        window6,
        bg = "#1F43A0",
        height = 600,
        width = 900,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    feedback_label = Label(
        window6, 
        text="",
        fg="red"  # You can change the color as needed
    )
    feedback_label.place(x=10, y=10)

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        390.0,
        45.0,
        image=image_image_1
    )

    canvas.create_text(
        86.0,
        17.0,
        anchor="nw",
        text="Update",
        fill="#000000",
        font=("Inter Bold", 40 * -1)
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        450.0,
        346.0,
        image=image_image_2
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        530.0,
        378.5,
        image=entry_image_3
    )
    entry_3 = Entry(
        window6,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=333.0,
        y=360.0,
        width=394.0,
        height=35.0
    )
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        530.0,
        472.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        window6,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=333.0,
        y=454.0,
        width=394.0,
        height=35.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        530.0,
        285,
        image=entry_image_4
    )
    entry_4 = Entry(
        window6,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=333.0,
        y=266.0,
        width=394.0,
        height=35.0
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        530.0,
        331.5,
        image=entry_image_6
    )
    entry_6 = Entry(
        window6,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_6.place(
        x=333.0,
        y=313.0,
        width=394.0,
        height=35.0
    )

    entry_5 = Entry(
        window6,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_5.place(
        x=333.0,
        y=160.0,
        width=394.0,
        height=35.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        530.0,
        425.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        window6,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=333.0,
        y=407.0,
        width=394.0,
        height=35.0
    )


    canvas.create_text(
        210.0,
        454.0,
        anchor="nw",
        text="Address:",
        fill="#000000",
        font=("Inter Bold", 26 * -1)
    )

    canvas.create_text(
        267.0,
        360.0,
        anchor="nw",
        text="Age:",
        fill="#000000",
        font=("Inter Bold", 26 * -1)
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        51.0,
        46.0,
        image=image_image_3
    )


    submit_button = Button(
        window6,
        text="UPDATE",  # Use an appropriate image or configure as needed
        borderwidth=0,
        highlightthickness=0,
        command=lambda:update_details(entry_5.get(),entry_4.get(),entry_1.get(),entry_3.get(),entry_2.get(),entry_6.get()),
        bg="#8ca6fe",
        font="bold",
        relief="raised"
    )
    submit_button.place(
        x=741.0,
        y=500.0,  # Adjust the y-coordinate as needed
        width=100.0,  # Adjust the width as needed
        height=40.0
    )


    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        window6,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=window6.withdraw,
        relief="flat"
    )
    button_1.place(
        x=380.0,
        y=500.0,
        width=155.0,
        height=43.0
    )

    canvas.create_text(
        267.0,
        220.0,
        anchor="nw",
        text="Enter in the fields to update",
        fill="#000000",
        font=("Inter Bold", 26 * -1)
    )

    canvas.create_text(
        104.0,
        160.0,
        anchor="nw",
        text="Account number:",
        fill="#000000",
        font=("Inter Bold", 26 * -1)
    )

    canvas.create_text(
        243.0,
        266.0,
        anchor="nw",
        text="Name:",
        fill="#000000",
        font=("Inter Bold", 26 * -1)
    )

    canvas.create_text(
        267.0,
        313.0,
        anchor="nw",
        text="Mail:",
        fill="#000000",
        font=("Inter Bold", 26 * -1)
    )

    canvas.create_text(
        127.0,
        407.0,
        anchor="nw",
        text="Phone Number:",
        fill="#000000",
        font=("Inter Bold", 26 * -1)
    )

    window6.resizable(False, False)
    window6.mainloop()

def adminmenu():
    empwindow=Toplevel(window)
    empwindow.geometry("700x600")
    empwindow.title("Admin")
    ctk.set_appearance_mode("light")
    empwindow.config(bg='blue4')
    ctk.set_default_color_theme("blue")
    empwindow.resizable(False, False)
    frame3=ctk.CTkFrame(master=empwindow,width=600,height=600,corner_radius=15,fg_color='ivory2')
    frame3.pack(pady=50,padx=100,fill="both",expand=True)
    labelmen=ctk.CTkLabel(master=frame3,text="ADMIN MENU",font=("TkHeading",26,'bold'),text_color='black')
    labelmen.pack(pady=20,padx=40)
    button11=ctk.CTkButton(master=frame3,text="Search",command=search,height=50,width=100)
    button11.pack(pady=20,padx=40)
    button11.place(x=365,y=100)
    button13=ctk.CTkButton(master=frame3,text="Update",command=update,height=50,width=100)
    button13.pack(pady=20,padx=40)
    button13.place(x=365,y=170)
    button14=ctk.CTkButton(master=frame3,text="Loan Approval",command=emploanstatus,height=50,width=100)
    button14.pack(pady=20,padx=40)
    button14.place(x=365,y=240)
    button15=ctk.CTkButton(master=frame3,text="Delete Approval",command=empdelete,height=50,width=100)
    button15.pack(pady=20,padx=40)
    button15.place(x=365,y=310)
    button16=ctk.CTkButton(master=frame3,text="Exit",command=empwindow.withdraw,height=50,width=100)
    button16.pack(pady=20,padx=40)
    button16.place(x=365,y=380)
    userimg=Image.open("./DBMSPROJ/admenu.jpg")
    resized=userimg.resize((300,400),Image.ANTIALIAS)
    tk_image = ImageTk.PhotoImage(resized)
    labelad=tk.Label(frame3,image=tk_image)
    labelad.image=tk_image
    labelad.place(x=15,y=70)
def alogin():
    global account2,password2
    createtable()
    account2=entryadn.get()
    password2=entryadp.get()
    
    if not(account2 and password2):
        messagebox.showinfo('Error','Enter all fields')
    elif (not(accountexist1())):
        messagebox.showinfo('Error','Account or Password incorrect')
    else:
        entryadn.delete(0,'end')
        entryadp.delete(0,'end')
        adminmenu()
def accountexist1():
    conn=mysql.connector.connect(host="localhost",user="root",password="12345678",database="bank")
    cursor=conn.cursor()
    cursor.execute("select count(*) from admin where admn='"+entryadn.get()+"'"+"and password='"+entryadp.get()+"'")
    result=cursor.fetchone()
    conn.close()
    return result[0]>0
def adminlogin():
    global entryadn,entryadp
    adw=Toplevel(window)
    adw.geometry("700x700")
    adw.title("Admin Loginpage")
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")
    def back():
        adw.withdraw()
    def show():
        if entryadp.cget('show')=='*':
            entryadp.configure(show='')

        else:
            entryadp.configure(show='*')
    framead=ctk.CTkFrame(master=adw,width=600,height=600,corner_radius=15,fg_color='light goldenrod')
    framead.pack(pady=0,padx=0,fill="both",expand=True)
    img1=ImageTk.PhotoImage(Image.open("./DBMSPROJ/admin.jpg"))
    labeli=tk.Label(adw,image=img1)
    labeli.image=img1
    labeli.pack(pady=0,padx=0)
    labeln=ctk.CTkLabel(master=framead,text="Admin Login",font=("TkHeading",26,'bold'),text_color='black')
    labeln.pack(pady=45,padx=50)
    entryadn=ctk.CTkEntry(master=framead,width=220,placeholder_text="AdminNumber")
    entryadn.pack(pady=20,padx=40)
    entryadp=ctk.CTkEntry(master=framead,width=220,placeholder_text="Password",show='*')
    entryadp.pack(pady=20,padx=40)
    buttonp=ctk.CTkCheckBox(master=framead,text="Show/Hide",command=show)
    buttonp.pack(pady=20,padx=15)
    buttonl=ctk.CTkButton(master=framead,text="Login",command=alogin)
    buttonl.pack(pady=20,padx=40)
    buttonback4=ctk.CTkButton(master=framead,text="Back",command=back)
    buttonback4.pack(pady=20,padx=15)

def customerlogin():
    global entry1,entry2
    newindow=Toplevel(window)
    newindow.geometry("700x700")
    newindow.title("Cutomer Loginpage")
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")
    def back():
        newindow.withdraw()
    def show():
        if entry2.cget('show')=='*':
            entry2.configure(show='')
        else:
            entry2.configure(show='*')
    frame1=ctk.CTkFrame(master=newindow,width=600,height=600,corner_radius=15,fg_color='light goldenrod')
    frame1.pack(pady=0,padx=0,fill="both",expand=True)
    img1=ImageTk.PhotoImage(Image.open("./DBMSPROJ/adminLogin1.png"))
    label4=tk.Label(newindow,image=img1)
    label4.image=img1
    label4.pack(pady=0,padx=0)
    label3=ctk.CTkLabel(master=frame1,text="Customer Login",font=("TkHeading",26,'bold'),text_color='black')
    label3.pack(pady=45,padx=50)
    entry1=ctk.CTkEntry(master=frame1,width=220,placeholder_text="AccountNumber")
    entry1.pack(pady=20,padx=40)
    entry2=ctk.CTkEntry(master=frame1,width=220,placeholder_text="Password",show='*')
    entry2.pack(pady=20,padx=40)
    button14=ctk.CTkCheckBox(master=frame1,text="Show/Hide",command=show)
    button14.pack(pady=20,padx=15)
    def close():
        newindow.withdraw()
    button3=ctk.CTkButton(master=frame1,text="Login",command=clogin)
    button3.pack(pady=20,padx=40)
    button4=ctk.CTkButton(master=frame1,text="Signup",command=csign)
    button4.pack(pady=20,padx=40)
    buttonback1=ctk.CTkButton(master=frame1,text="Exit",command=back)
    buttonback1.pack(pady=20,padx=15)

welcome()
window.mainloop()