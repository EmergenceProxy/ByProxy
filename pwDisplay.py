#Purpose: Simple user interface program to store passwords in an encrypted format
# maybe add bill manager.
#Run with: python .\pwDisplay.py
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.simpledialog import askstring, askinteger
from tkinter import scrolledtext
import accountBook
import customDiag


myaccountBook = accountBook.myAccountBook()

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Bean Files", "*.bean"),("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        myaccountBook.load(text)
        myaccountBook.setSessionFile(filepath)
        #myaccountBook.addEntry()

    updateTextField(txt_display, displayAccountBook(""))
    updateTextField(txt_edit, myaccountBook.toString())
   
    window.title(f"Bean Password Manager - {filepath}")
#####################################################################
def save_file():
    """Save the current file as a new file."""
    if verifySettings():
        filepath = asksaveasfilename(
            defaultextension="bbt_pwManDataTemp.bean",
            filetypes=[("Bean Files", "*.bean"),("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, mode="w", encoding="utf-8") as output_file:
            text = txt_edit.get("1.0", tk.END)
            output_file.write(text)
        window.title(f"Bean Password Manager - {filepath}")
#####################################################################
#####################################################################
def add_entry():
    title = "Data Entry"
    
    account = askstring(title, "Please enter account holding site: ")
    output = "Site Account created with: "+account
    #txt_display.configure(text=output)
    #txt_display.update()
    updateTextField(txt_display, output)
    
    
    username = askstring(title, "Please enter username: ")
    output += "\nUsername: "+username
    #txt_display.configure(text=output)
    #txt_display.update()
    updateTextField(txt_display, output)
    
    password = askstring(title, "Please enter password: ", show="*")
    output += "\nPassword: "+password
    updateTextField(txt_display, output)
    
    myaccountBook.setAccountKey(myaccountBook.getSessionKey())
    output += "\nAdd Entry: "+myaccountBook.addEntry(account,username,password)+"\n\n"
    updateTextField(txt_display, output+displayAccountBook(""))
    
    #txt_edit.delete("1.0","end")
    #txt_edit.insert(tk.END, myaccountBook.toString())
    #txt_edit.update()
    updateTextField(txt_edit, myaccountBook.toString())
#####################################################################
def remove_entry():
    title = "Remove Entry"
    
    selection = askinteger(title, "Please Select the account you wish to remove: ")
    #account = askstring(title, "Please enter the account you wish to remove: ")
    output = "Site Account created with: "+str(selection)
    myaccountBook.removeEntry(selection)
    updateTextField(txt_display, displayAccountBook(""))
    updateTextField(txt_edit, myaccountBook.toString())
    
def show_PWs():
    updateTextField(txt_display, displayAccountBook("show"))
    updateTextField(txt_edit, myaccountBook.toString())
def hide_PWs():
    updateTextField(txt_display, displayAccountBook(""))
    updateTextField(txt_edit, myaccountBook.toString())
def show_options():
    #myaccountBook.editEntry()
    def dismiss ():
        dlg.grab_release()
        dlg.destroy()

    dlg = tk.Toplevel(window)
    tk.Button(dlg, text="Done", command=dismiss).grid()
    dlg.protocol("WM_DELETE_WINDOW", dismiss) # intercept close button
    dlg.transient(window)   # dialog window is related to main
    dlg.wait_visibility() # can't grab until window appears, so we wait
    #dlg.grab_set()        # ensure all input goes to our window
    dlg.wait_window()     # block until window is destroyed
#####################################################################
def displayAccountBook(vision):
    print("---pwDisplay: displayAccountBook(): start")
    output = "Account Email: "+ str(myaccountBook.getAccountEmail()) +"\n"
    output += "Account Key: "+ myaccountBook.getAccountKey() +"\n"
    output += "Session Key: "+ myaccountBook.getSessionKey() +"\n"
    output += "Session File: "+ myaccountBook.getSessionFile() +"\n"
    
    entryCount = 1
    tempEntryList = myaccountBook.getAccountEntryList()
    for account in tempEntryList:
        output += "###################\n"
        output += "Entry "+str(entryCount)+":"+ str(len(tempEntryList)) +":\n"
        output += "     Entry AccountHolder: "+ account.getAccountHolder() +"\n"
        output += "     Entry Username: "+ account.getUsername() +"\n"
        output += "     Entry Email: "+ account.getEmail() +"\n"
        print("---pwDisplay: displayAccountBook(): vision == show? " , (vision == "show") )
        if vision == "show":
            output += "     Entry Password: "+ account.getDecPassword(myaccountBook.getAccountKey()).decode("utf-8") +"\n"
        else:
            output += "     Entry Password: "+ account.getPassword() +"\n"
        entryCount += 1
    return output
#####################################################################
def verifySettings():
    title = "Account Data Entry"
    if len(myaccountBook.getAccountEmail()) <= 7:
        account = askstring(title, "Please enter an email for your account: ")
        myaccountBook.setAccountEmail(account)
        updateTextField(txt_display, displayAccountBook(""))
        updateTextField(txt_edit, myaccountBook.toString())
    if len(myaccountBook.getAccountKey()) <= 7:
        myaccountBook.setAccountKey(myaccountBook.getSessionKey())
        updateTextField(txt_display, displayAccountBook(""))
        updateTextField(txt_edit, myaccountBook.toString())

    return True
#####################################################################
def updateTextField(txt_Field, text):
    txt_Field.configure(state ='normal')
    #txt_Field.update()
    txt_Field.delete("1.0",tk.END)
    txt_Field.update()
    txt_Field.insert(tk.END, text)
    txt_Field.update()
    txt_Field.configure(state ='disabled')
    #txt_Field.update()

#####################################################################
def createButtons(frm_buttons):
    btn_open = tk.Button(frm_buttons, text="Open", command=open_file)
    btn_save = tk.Button(frm_buttons, text="Save As...", command=save_file)
    btn_add = tk.Button(frm_buttons, text="Add", command=add_entry)
    btn_remove = tk.Button(frm_buttons, text="Remove", command=remove_entry)
    btn_show = tk.Button(frm_buttons, text="Show", command=show_PWs)
    btn_hide = tk.Button(frm_buttons, text="Hide", command=hide_PWs)
    btn_options = tk.Button(frm_buttons, text="Options", command=show_options)

    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btn_save.grid(row=1, column=0, sticky="ew", padx=5)
    btn_add.grid(row=2, column=0, sticky="ew", padx=5)
    btn_remove.grid(row=3, column=0, sticky="ew", padx=5)
    btn_show.grid(row=4, column=0, sticky="ew", padx=5)
    btn_hide.grid(row=5, column=0, sticky="ew", padx=5)
    btn_options.grid(row=6, column=0, sticky="ew", padx=5)
#####################################################################

#####################################################################
#####################################################################
#####################################################################
#MAIN
window = tk.Tk()
window.title("Bean Password Manager")

window.rowconfigure(0, minsize=100, weight=1)
window.columnconfigure(1, minsize=100, weight=1)

display_frame = tk.LabelFrame(window, text="Display Windows", padx=10,pady=20, background="gray")
#display_frame.pack(fill="both", expand="yes")


#txt_display = tk.Label(display_frame, height=15, width=50, anchor="nw", justify="left",font=("Arial", 16),background="black", foreground="red",text="Display",wraplength=600)
txt_display = scrolledtext.ScrolledText(display_frame,   
                                      wrap = tk.WORD,  
                                      width = 80,  
                                      height = 20,  
                                      background="black", foreground="red",
                                      font = ("Times New Roman", 
                                              15)) 
txt_edit = tk.Text(    display_frame, height=3, width=50,                             font=("Arial", 12),background='#662220', foreground="green")
#widget2.config(background='#000000')

txt_display.grid(row=0, column=0, sticky="nwe")
txt_edit.grid(row=1, column=0, sticky="nwe")

#txt_display.configure(text="Display")
txt_display.insert(tk.END, displayAccountBook(""))
txt_display.configure(state ='disabled')
#txt_display.configure(state ='enabled')
#txt_display.configure(wraplength=1000)
#txt_display.update()


txt_edit.insert(tk.END, myaccountBook.toString())


frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
createButtons(frm_buttons)


#Set positions for mainwindow
frm_buttons.grid(row=0, column=0, sticky="ns")
display_frame.grid(row=0,column=1, sticky="news")
#txt_display.grid(row=0, column=1, sticky="nsew")
#txt_edit.grid(row=1, column=1, sticky="nsew")



window.mainloop()