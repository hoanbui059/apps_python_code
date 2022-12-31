from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title('HoanBui - Currency Conversion')
root.geometry("500x500")

#Create  Tabs
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)

#Create two frames
currency_frame = Frame(my_notebook, width=480, height=480)
currency_frame.pack(fill="both", expand=1)

conversion_frame = Frame(my_notebook, width=480, height=480)
conversion_frame.pack(fill="both", expand=1)

#Add our tabs
my_notebook.add(currency_frame, text="Currencies")
my_notebook.add(conversion_frame, text="Conver")

#Disable 2nd tab
my_notebook.tab(1, state='disabled')

##################
# CURRENCY STUFF
##################

def lock():
    if not home_entry.get() or not conversion_entry.get() or not rate_entry.get():
        messagebox.showwarning("WARNING!", "YOU DIDN'T FILL OUT ALL THE FIELD")
    else:
        #Disable entry boxes
        home_entry.config(state="disabled")
        conversion_entry.config(state="disabled")
        rate_entry.config(state="disabled")

        #Enable tab
        my_notebook.tab(1, state='normal')

        #Change Tab Field
        amount_label.config(text=f'Amount of {home_entry.get()} To Convert To {conversion_entry.get()}')
        converted_label.config(text=f'Equals This Many {conversion_entry.get()}')
        convert_button.config(text=f'Convert From {home_entry.get()}')

def unlock():
    #Disable entry boxes
    home_entry.config(state="normal")
    conversion_entry.config(state="normal")
    rate_entry.config(state="normal")

    #Disable tab
    my_notebook.tab(1, state='disabled')

# Create Label Frame
home = LabelFrame(currency_frame, text="Your Home Currency")
home.pack(pady=20)

#Home currency entry box
home_entry = Entry(home, font=("Helvetica", 24))
home_entry.pack(pady=10, padx=10)

#Conversion Currency Frame
conversion = LabelFrame(currency_frame, text="Conversion Currency")
conversion.pack(pady=20)

#Convert to label
conversion_label = Label(conversion, text="Currency To Convert To...")
conversion_label.pack(pady=10)

#Convert to Entry
conversion_entry=Entry(conversion, font=("Helvetica", 24))
conversion_entry.pack(pady=10, padx=10)

#Rate label
rate_label = Label(conversion, text="Current Conversion Rate...")
rate_label.pack(pady=10)

#Rate Entry
rate_entry=Entry(conversion, font=("Helvetica", 24))
rate_entry.pack(pady=10, padx=10)

# Button Frame
button_frame = Frame(currency_frame)
button_frame.pack(pady=20)

# Create Buttons
lock_button = Button(button_frame, text="Lock", command=lock)
lock_button.grid(row=0, column=0, padx=10)

unlock_button = Button(button_frame, text="Unlock", command=unlock)
unlock_button.grid(row=0, column=1, padx=10)

##################
# CONVERSION STUFF
##################
def convert():
    #Clear Converted Entry Box
    converted_entry.delete(0, END)

    #Convert
    conversion = float(rate_entry.get()) * float(amount_entry.get())

    #Convert to two decimals
    conversion = round(conversion,2)

    #Add commas
    conversion = '{:,}'.format(conversion)

    #Update entry box
    converted_entry.insert(0, f'{conversion} VND')

def clear():
    amount_entry.delete(0, END)
    converted_entry.delete(0, END)

amount_label = LabelFrame(conversion_frame, text="Amount of US Dollar To Convert To Vietnam Dong")
amount_label.pack(pady=20)

#Entry Box For Amount
amount_entry = Entry(amount_label, font=("Helvetica", 24))
amount_entry.pack(padx=10, pady=10)

#Convert Button
convert_button = Button(amount_label, text="Convert From US Dollar", command=convert)
convert_button.pack(pady=20)

#Equals Frame
converted_label = LabelFrame(conversion_frame, text="Equals This Many Vietnam Dong")
converted_label.pack(pady=20)

#Converted entry
converted_entry = Entry(converted_label, font=("Helvetica", 24))
converted_entry.pack(padx=10, pady=10)

#Clear Button
clear_button = Button(conversion_frame, text="Clear", command=clear)
clear_button.pack(pady=20)

#Fake Label for spacing
spacer = Label(conversion_frame, text="", width=56)
spacer.pack()

root.mainloop()