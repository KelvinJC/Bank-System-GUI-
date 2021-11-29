from tkinter import *
import os
import random
from PIL import ImageTk, Image


# Main screen
master = Tk()
master.title("Banking App")
master.resizable(width= False, height = False)

# Functions

def generate_account_number():
    number = random.randint(1000000000, 9999999999)
    account_number = str(number)
    return account_number

def finish_reg():
    
    # Pull user registration entries from the register function
    name = temp_name.get()
    email = temp_email.get()
    phone = temp_phone.get()
    age = temp_age.get()
    gender = temp_gender.get()
    address = temp_address.get()
    password = temp_password.get()
    
    # Create array of all files in the same directory with this program's script. To be used during validation
    all_accounts = os.listdir()
    
    # Validation (user input): Ensure all fields are filled before registration progresses
    if name == "" or email == "" or phone == "" or age == "" or gender == "" or address == "" or password == "":
        notif.config(fg='red', text = 'All fields required')
        return
    
    
    # Create account number
    account_number = generate_account_number()
    
    # Validation (data store): Check if the name has already been used to register
    if account_number in all_accounts:
        # notif.config(fg='red', text = 'Account already exists.')
        finish_reg()

    else:
        notif.config(fg='green', text = 'Account has been created.')
        account_notif.config(fg='green', text = 'YOUR ACCOUNT NUMBER IS '+account_number)



        new_file = open(account_number, 'w')
        new_file.write(name+'\n')
        new_file.write(password+'\n')
        new_file.write(email+'\n')
        new_file.write(phone+'\n')
        new_file.write(age+'\n')
        new_file.write(gender+'\n')
        new_file.write(address+'\n')
        new_file.write(account_number+'\n')
        new_file.write('0')
        new_file.close()

        
        
def register():  
    
    # Variables
    global temp_name
    global temp_email
    global temp_phone
    global temp_age
    global temp_gender
    global temp_address
    global temp_password
    global notif
    global account_notif
    
    temp_name = StringVar()
    temp_email = StringVar()
    temp_phone = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_address = StringVar()
    temp_password = StringVar()
    
    # Register Screen
    register_screen = Toplevel(master)
    register_screen.title('Register')
    register_screen.resizable(width= False, height = False)

    # Labels
    Label(register_screen, text="Please enter your details below to register", font=('Calibri', 12)).grid(row=0,sticky=N, pady=10)
    Label(register_screen, text="Name", font=('Calibri', 12)).grid(row=1,sticky=W)
    Label(register_screen, text="Email", font=('Calibri', 12)).grid(row=2,sticky=W)
    Label(register_screen, text="Phone", font=('Calibri', 12)).grid(row=3,sticky=W)
    Label(register_screen, text="Age", font=('Calibri', 12)).grid(row=4,sticky=W)
    Label(register_screen, text="Gender", font=('Calibri', 12)).grid(row=5,sticky=W)
    Label(register_screen, text="Address", font=('Calibri', 12)).grid(row=6,sticky=W)
    Label(register_screen, text="Password", font=('Calibri', 12)).grid(row=7,sticky=W)

    notif = Label(register_screen, font=('Calibri', 12))
    notif.grid(row=9,sticky=N, pady=10)
    account_notif = Label(register_screen, font=('Calibri', 12, 'bold italic'))
    account_notif.grid(row=10,sticky=N, pady=10)
    
    # Entries
    Entry(register_screen, textvariable=temp_name).grid(row=1, column=0)
    Entry(register_screen, textvariable=temp_email).grid(row=2, column=0)
    Entry(register_screen, textvariable=temp_phone).grid(row=3, column=0)
    Entry(register_screen, textvariable=temp_age).grid(row=4, column=0)
    Entry(register_screen, textvariable=temp_gender).grid(row=5, column=0)
    Entry(register_screen, textvariable=temp_address).grid(row=6, column=0)
    Entry(register_screen, textvariable=temp_password, show='*').grid(row=7, column=0)

    # Buttons
    Button(register_screen, text='Register', command= finish_reg, font=('Calibri', 12)).grid(row=8, sticky=N, pady=10)


def login_session():
    global login_number
    
    all_accounts = os.listdir()
    login_number = temp_login_number.get()
    login_password = temp_login_password.get() 
    
    # Validation process: Check if login name and login password match with stored account name and password
    if login_number in all_accounts:
        file = open(login_number, "r")
        file_data = file.read()
        file.close()
        file_data = file_data.split('\n')
        password = file_data[1]
        # Account Dashboard
        if login_password == password:
            login_screen.destroy()
            # Identify name to be used in welcome message
            name = file_data[0]
            account_dashboard = Toplevel(master)
            account_dashboard.title('Dashboard')
            account_dashboard.resizable(width= False, height = False)

            # Labels
            Label(account_dashboard, text='Account Dashboard', font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
            Label(account_dashboard, text='Welcome '+name+'!', fg='green', font=('Calibri', 12)).grid(row=1, sticky=N, pady=10)
            # Buttons
            Button(account_dashboard, text='Personal Details', font=('Calibri', 12), width=30, command= personal_details).grid(row=2, sticky=N, pady=10, padx=10)
            Button(account_dashboard, text='Deposit', font=('Calibri', 12), width=30, command= deposit).grid(row=3, sticky=N, pady=10, padx=10)
            Button(account_dashboard, text='Withdraw', font=('Calibri', 12), width=30, command = withdraw).grid(row=4, sticky=N, pady=10)
            Label(account_dashboard).grid(row=5, sticky=N, pady=10)

        else:
            login_notif.config(fg='red', text = 'Password incorrect!')
            #temp_login_password.delete(0, END) # Intent - A function to clear the password box after a wrong entry. Output- "AttributeError: 'StringVar' object has no attribute 'delete'  "
        return
    else:
        login_notif.config(fg='red', text = 'No account found!')

def personal_details():
    # Variables
    file = open(login_number, 'r')
    file_data = file.read()
    file.close()
    user_details = file_data.split('\n')
    details_name = user_details[0]
    details_email = user_details[2]
    details_phone = user_details[3]
    details_age = user_details[4]
    details_gender = user_details[5]
    details_address = user_details[6]
    details_account_number = user_details[7]
    details_balance = user_details[8]
    
    # Personal details screen
    personal_details_screen = Toplevel(master)
    personal_details_screen.title('Personal Details')
    personal_details_screen.geometry("280x300")
    personal_details_screen.resizable(width= False, height = False)

    
    # Labels
    Label(personal_details_screen, text='Personal Details', fg = 'blue',font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    Label(personal_details_screen, text='Name : '+details_name, font=('Calibri', 12)).grid(row=1, sticky=W)
    Label(personal_details_screen, text='Email : '+details_email, font=('Calibri', 12)).grid(row=2, sticky=W)
    Label(personal_details_screen, text='Phone Number : '+details_phone, font=('Calibri', 12)).grid(row=3, sticky=W)
    Label(personal_details_screen, text='Age : '+details_age, font=('Calibri', 12)).grid(row=4, sticky=W)
    Label(personal_details_screen, text='Gender : '+details_gender, font=('Calibri', 12)).grid(row=5, sticky=W)
    Label(personal_details_screen, text='Address : '+details_address, font=('Calibri', 12)).grid(row=6, sticky=W)
    Label(personal_details_screen, text='Account Number : '+details_account_number, font=('Calibri', 12)).grid(row=7, sticky=W)
    Label(personal_details_screen, text='Balance : $'+details_balance, font=('Calibri', 12)).grid(row=8, sticky=W)
    
    # Button
    Button(personal_details_screen, text='Edit details', font=('Calibri', 12), command = edit_personal_details).grid(row=9,sticky=N, pady=15)
    
    
def edit_personal_details():
    # Variables
    global name_edit
    global email_edit
    global phone_edit
    global address_edit
    global edit_details_notif
    
    name_edit = StringVar()
    email_edit = StringVar()
    phone_edit = StringVar()
    address_edit = StringVar()
    
    # Edit Personal Details Screen
    edit_personal_details_screen = Toplevel(master)
    edit_personal_details_screen.title('Edit Personal Details')
    edit_personal_details_screen.geometry('400x200')
    edit_personal_details_screen.resizable(width= False, height = False)

    # Labels
    Label(edit_personal_details_screen, text="Please enter your new details", font=('Calibri', 12)).grid(row=0,sticky=N, pady=10)
    Label(edit_personal_details_screen, text="Name", font=('Calibri', 12)).grid(row=1,sticky=W)
    Label(edit_personal_details_screen, text="Email", font=('Calibri', 12)).grid(row=2,sticky=W)
    Label(edit_personal_details_screen, text="Phone Number", font=('Calibri', 12)).grid(row=3,sticky=W)
    Label(edit_personal_details_screen, text="Address", font=('Calibri', 12)).grid(row=4,sticky=W)
    
    edit_details_notif = Label(edit_personal_details_screen, font=('Calibri', 12))
    edit_details_notif.grid(row=7, sticky=N, pady=5)    
 
      
    # Entries
    Entry(edit_personal_details_screen, textvariable=name_edit).grid(row=1, column=1)
    Entry(edit_personal_details_screen, textvariable=email_edit).grid(row=2, column=1)
    Entry(edit_personal_details_screen, textvariable=phone_edit).grid(row=3, column=1)
    Entry(edit_personal_details_screen, textvariable=address_edit).grid(row=4, column=1)

    # Buttons
    Button(edit_personal_details_screen, text='Save', command= finish_edit_details, font=('Calibri', 12)).grid(row=5, column=1, sticky=N, pady=5)
 

   

def deposit():
    #Variables
    global amount
    global deposit_notif
    global current_balance_label
    global deposit_amount_entry
    
    amount = StringVar()
    file = open(login_number, 'r')
    file_data = file.read()
    file.close()
    user_details = file_data.split('\n')
    details_balance = user_details[8]
    
    # Deposit screen
    deposit_screen = Toplevel(master)
    deposit_screen.title('Deposit')
    deposit_screen.geometry('400x200')
    deposit_screen.resizable(width= False, height = False)

    
    # Labels
    Label(deposit_screen, text='Deposit', font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    
    current_balance_label = Label(deposit_screen, text='Current Balance : $'+details_balance, font=('Calibri', 12))
    current_balance_label.grid(row=1, sticky=W)
    
    Label(deposit_screen, text='Amount : ', font=('Calibri', 12)).grid(row=2, sticky=W)
    
    deposit_notif = Label(deposit_screen, font=('Calibri', 12))
    deposit_notif.grid(row=4, sticky=N, pady=5)

    # Entry
    deposit_amount_entry = Entry(deposit_screen, textvariable=amount)
    deposit_amount_entry.grid(row=2, column=1)
    
    # Button
    Button(deposit_screen, text='Make Deposit', font=('Calibri', 12), command=finish_deposit).grid(row=3, column=1, sticky=N, pady=5)

def finish_deposit():
    # Validation: Check for mis-types or errors in amount entries 
    try:
        if amount.get() == "":
            deposit_notif.config(text='Amount is required!', fg = 'red')
            return
        if float(amount.get()) <= 0:
            deposit_notif.config(text='Zero or negative currency is not accepted', fg = 'red')
            return
    
        
    # to handle the event of user entering a string as deposit        
    except ValueError:
        deposit_notif.config(text='Please enter only numbers as amount', fg = 'red')
    else:
        file = open(login_number, 'r+')   # file is opened in r+ mode to accomodate future write operation
        file_data = file.read()
        details = file_data.split('\n')
        current_balance = details[8]
        # updated_balance = current_balance         # seems redundant
        updated_balance = float(current_balance) + float(amount.get()) # inputs are converted to float before addition. In next line, output converted back to a string
        file_data       = file_data.replace(current_balance, str(updated_balance)) # spacing the assignment operator just for better code readability
        
        # following functions locate the start of the file, remove its current content and replace it with updated content
        file.seek(0)
        file.truncate(0)
        file.write(file_data)
        file.close()
        
        current_balance_label.config(text='Current Balance : $'+str(updated_balance), fg = 'green')
        deposit_notif.config(text='Balance Updated', fg = 'green')
        deposit_amount_entry.delete(0, END)


def withdraw():
    # Variables
    global withdraw_amount
    global withdraw_notif
    global current_balance_label
    global withdraw_amount_entry
    
    withdraw_amount = StringVar()
    file = open(login_number, 'r')
    file_data = file.read()
    file.close()
    user_details = file_data.split('\n')
    details_balance = user_details[8]
    
    # Withdraw screen
    withdraw_screen = Toplevel(master)
    withdraw_screen.title('Withdraw')
    #withdraw_screen.geometry('400x200')
    withdraw_screen.resizable(width= False, height = False)
    
    # Labels
    Label(withdraw_screen, text='Withdraw', font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    current_balance_label = Label(withdraw_screen, text='Current Balance : $'+details_balance, font=('Calibri', 12))
    current_balance_label.grid(row=1, sticky=W)
    Label(withdraw_screen, text='Amount : ', font=('Calibri', 12)).grid(row=2, sticky=W)
    withdraw_notif = Label(withdraw_screen, font=('Calibri', 12))
    withdraw_notif.grid(row=4, sticky=N, pady=5)

    # Entry
    withdraw_amount_entry = Entry(withdraw_screen, textvariable=withdraw_amount)
    withdraw_amount_entry.grid(row=2, column=1)
    
    # Button
    Button(withdraw_screen, text='Make withdrawal', font=('Calibri', 12), command=finish_withdraw).grid(row=3, column=1, sticky=N, pady=5)

def finish_withdraw():
    # Validation: Check for mis-types or errors in amount entries 
    try:
        if withdraw_amount.get() == "":
            withdraw_notif.config(text='Amount is required!', fg = 'red')
            return
        
        if float(withdraw_amount.get()) <= 0:
            withdraw_notif.config(text='Zero or negative currency is not accepted', fg = 'red')
            return
    
        
    # to handle the event of user entering a string as deposit        
    except ValueError:
        withdraw_notif.config(text='Please enter only numbers as amount', fg = 'red')
    else:
        file = open(login_number, 'r+')   # file is opened in r+ mode to accomodate future write operation
        file_data = file.read()
        details = file_data.split('\n')
        current_balance = details[8]
        
        if float(withdraw_amount.get()) > float(current_balance):
            withdraw_notif.config(text='Insufficient Funds!', fg = 'red')
            return
            
        
        updated_balance = current_balance
        updated_balance = float(updated_balance) - float(withdraw_amount.get()) # inputs are converted to float before addition. In next line, output converted back to a string
        file_data       = file_data.replace(current_balance, str(updated_balance)) # spacing the assignment operator just for better code readability
        
        
        # following functions locate the start of the file, remove its current content and replace it with updated content
        file.seek(0)
        file.truncate(0)
        file.write(file_data)
        file.close()
        
        current_balance_label.config(text='Current Balance : $'+str(updated_balance), fg = 'green')
        withdraw_notif.config(text='Balance Updated', fg = 'green')
        withdraw_amount_entry.delete(0, END)
  
    
def login():
    # Variables
    global temp_login_number
    global temp_login_password
    global login_notif
    global login_screen
    
    temp_login_number = StringVar()
    temp_login_password = StringVar()
    
    # Login screen
    login_screen = Toplevel()
    login_screen.title('Login')
    login_screen.resizable(width= False, height = False)

    # Labels
    Label(login_screen, text = 'Login to your account', font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    Label(login_screen, text = 'Account Number', font=('Calibri', 12)).grid(row=1, sticky=W)
    Label(login_screen, text = 'Password', font=('Calibri', 12)).grid(row=2, sticky=W)
    login_notif = Label(login_screen, font=('Calibri', 12))
    login_notif.grid(row=4, sticky=N)
    
    # Entry
    Entry(login_screen, textvariable=temp_login_number).grid(row=1, column=1, padx=5)
    Entry(login_screen, textvariable=temp_login_password, show='*').grid(row=2, column=1, padx=5)
    
    # Buttons
    Button(login_screen, text = 'Login', font=('Calibri', 12), width=10, command=login_session).grid(row=3, column = 1, sticky=N, pady=15) 


# Image import 
img = Image.open("Screenshot_20210514-171451_Instagram (2).jpg") 
img = img.resize((323,400))

# there is the need to specify the master tk instance since ImageTK is a second instance of tkinter
img = ImageTk.PhotoImage(img, master=master)

# Labels
Label(master, text = "Vieden Bank", fg = "white", bg = "dark blue", width = 25, font=("Arial black", 14)).grid(row=0,sticky=N)
Label(master, text = "The most secure bank you've probably used !", fg = "white", bg = "dark blue", width = 41, font=("Calibri", 12, 'italic')).grid(row=1,sticky=N)

#Label(master, text = , font=("Calibri", 12)).grid(row=1,sticky=N)
Label(master, image=img).grid(row=2,sticky=N)

# Buttons
Button(master, text="Register", font=("Calibri", 12), width = 20, command=register).grid(row=3, sticky=N)
Button(master, text="Login", font=("Calibri", 12), width = 20, command=login).grid(row=4, sticky=N, pady=10)

master.mainloop()
