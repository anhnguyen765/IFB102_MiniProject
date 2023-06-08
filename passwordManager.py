# Import Libraries
from tkinter import *
import secrets
import string
import csv

# Functions
def showPassword():
    # Define available characters for a password
    letters = string.ascii_letters
    digits = string.digits
    specialChars = string.punctuation
    alphabet = letters + digits + specialChars

    global newPasswordLength # Take the input variable from users
    length = newPasswordLength.get()

    pwd = ''

    if len(length) == 0:
        pwd = 'Please choose a length'
    elif int(length) > 25:
        pwd = 'Please choose a shorter password'
    else:
        for i in range(int(length)):
            pwd +=''.join(secrets.choice(alphabet))
    
    # Display password
    newPassWordDisplayLabel.config(fg=element_colour)
    newPasswordDetail.config(text=pwd, fg=element_colour)
    
    newPasswordLength.delete(0,'end') # Delete the entered value of password length


def confirmPassword():
    password = str(newPasswordDetail['text'])
    account = str(newAccountInput.get()).lower()
    username = str(newUsernameInput.get())

    # Create warning window if missing values occur
    while len(account) == 0 or len(username) == 0:
        # Create warning screen
        warningScreen = Toplevel(screen)
        ## Set up window
        warningScreen.title('Error')
        warningScreen.config(bg='red')
        warningScreen.resizable(False,False)
        ## Elements
        if len(account) == 0: # Check the account field
            Label(warningScreen, text = 'Your account is missing',
                  font = subheader_font, fg='yellow', bg='red').pack(padx=5, pady=10)
        else:
            pass
        
        if len(username) == 0: # Check the username field
            Label(warningScreen, text = 'Your username is missing',
                  font = subheader_font, fg='yellow', bg='red').pack(padx=5,pady=10)
        else:
            pass
        ## Allow the pop up screen to show up
        warningScreen.mainloop()

    # Clear the fields
    newPasswordLength.delete(0, 'end')
    newAccountInput.delete(0,'end')
    newUsernameInput.delete(0,'end')

    #Input data into CSV file
    newPassword =[account, username, password]
    csv_file = open('password_manager.csv', 'a', newline='')
    writer = csv.writer(csv_file)
    writer.writerow(newPassword)
    csv_file.close()

def lookupPassword():
    global accountName
    global accountPassword
    global accountNameLabel
    global accountPasswordLabel

    account = findAccountEntry.get().lower()
    read_file = open('password_manager.csv', 'r')
    csv_reader = csv.reader(read_file)

    # Loop through the CSV file
    for row in csv_reader:
        # Compare the account name
        if account == row[0]:
            username = row[1]
            storedpwd = row[2]
            accountNameLabel.config(fg=element_colour)
            accountName.config(text=username, fg=element_colour)
            accountPasswordLabel.config(fg=element_colour)
            accountPassword.config(text=storedpwd, fg=element_colour)

# GUI
screen = Tk()

## GUI Element Configuration Variables
### Colours
primary_colour = '#0d1b2a'
secondary_colour = '#415a77'
element_colour = '#e0e1dd'
### Fonts
header_font = ('Arial', 18, 'bold')
subheader_font = ('Arial', 14, 'bold')
title_font = ('Arial',13,'underline')
text_font = ('Arial', 12, 'italic')


## GUI settings
screen.title('Password Manager')
screen.geometry('600x350')
screen.config(bg=primary_colour)
screen.columnconfigure(0, weight=5)
screen.columnconfigure(1, weight=5)
screen.rowconfigure(0, weight=1)
screen.rowconfigure(1, weight=9)

## Header
title = Label(screen, text='Password Storage',
              bg=primary_colour, fg=element_colour, 
              font=header_font)
title.grid(row=0, column=0, columnspan=2, pady=10)

## Body
body = Frame(screen, bg=secondary_colour, width=550, padx=10)
body.grid(row=1, column=0, columnspan=2, padx=25, pady=(0,15))
### Adding new password
newPass = Frame(body, width=200,
                bg = secondary_colour) # Set frame
newPass.grid(row=1, column=0, padx=10, pady=(15,0), sticky=N)
newPass.grid_columnconfigure(0, weight=3)
newPass.grid_columnconfigure(1, weight=7)

newPassTitle = Label(newPass, fg=element_colour,bg=secondary_colour,
                     text='Generate Password', font=subheader_font, padx=20)
newPassTitle.grid(row=0,column=0, columnspan=2, sticky=W)

newAccountLabel = Label(newPass, fg=element_colour, bg=secondary_colour,
                        text='Account For:',font=title_font, padx=20)
newAccountLabel.grid(row=1,column=0,columnspan=2, sticky=W)

account = StringVar()
newAccountInput = Entry(newPass,font=text_font,bg=element_colour,
                        fg=primary_colour, textvariable=account)
newAccountInput.grid(row=2, column=0, columnspan=2)

newUsernameLabel = Label(newPass, fg=element_colour, bg=secondary_colour,
                         text='Enter Username:', font=title_font, padx=20)
newUsernameLabel.grid(row=3, column=0, columnspan=2, sticky=W)

newUsernameInput = Entry(newPass,font=text_font,bg=element_colour,
                        fg=primary_colour)
newUsernameInput.grid(row=4, column=0, columnspan=2)

newPasswordLengthLabel = Label(newPass, fg=element_colour, bg=secondary_colour,
                         text='Select password length:', font=title_font, padx=20)
newPasswordLengthLabel.grid(row=5, column=0, columnspan=2, sticky=W)

newPasswordLength = Entry(newPass,font=text_font,bg=element_colour,
                        fg=primary_colour, width=4)
newPasswordLength.grid(row=6,column=0,padx=(12,0), pady=(5,5))

newPasswordButton = Button(newPass, text='Generate Password',
                           fg=secondary_colour,bg=element_colour,
                           activebackground= secondary_colour,
                           activeforeground= element_colour,
                           font=('Arial',8), justify=RIGHT,
                           command=showPassword)
newPasswordButton.grid(row=6, column=1, pady=(5,5),padx=(4,0))

newPassWordDisplayLabel = Label(newPass, fg=secondary_colour, bg=secondary_colour,
                         text='Your password:', font=title_font, padx=20)
newPassWordDisplayLabel.grid(row=7, column=0, columnspan=2, sticky=W)

newPasswordDetail = Label(newPass, fg=secondary_colour, bg=secondary_colour,
                         text='Your generated password', font=('Arial', 11, 'italic'))
newPasswordDetail.grid(row=8, column=0, columnspan=2)

newPasswordConfirmation = Button(newPass, text='Confirm Password',
                                 fg=secondary_colour, bg=element_colour,
                                 activebackground=secondary_colour,
                                 activeforeground=element_colour,
                                 font=('Arial',8), command=confirmPassword)
newPasswordConfirmation.grid(row=9, column=0, columnspan=2, pady=(0,25))

### Find stored password
findPass = Frame(body, width=200, bg=secondary_colour)
findPass.grid(row=1, column=1, padx=10, pady=(15,0), sticky=N)
findPass.grid_columnconfigure(0, weight=1)
findPass.grid_columnconfigure(1, weight=9)

findPassTitle = Label(findPass, fg=element_colour, bg=secondary_colour,
                      text='Find Password', font=subheader_font)
findPassTitle.grid(row=0,column=0, columnspan=2)

findAccountLabel = Label(findPass, fg=element_colour, bg=secondary_colour,
                         text='Account:', font=text_font)
findAccountLabel.grid(row=1, column=0, sticky=E, padx=(20,5))

findAccountEntry = Entry(findPass,font=text_font,bg=element_colour,
                        fg=primary_colour, width=15)
findAccountEntry.grid(row=1, column=1,sticky=W, padx=(5,20))

findAccountButton = Button(findPass, fg=secondary_colour, bg=element_colour,
                           activebackground=secondary_colour,
                           activeforeground=element_colour,
                           font=('Arial',8), padx=10,
                           text='Find Password', command=lookupPassword)
findAccountButton.grid(row=2, column=0, columnspan=2, pady=(10,5))

accountNameLabel = Label(findPass, font=text_font,
                    text='Your username is: ', padx=20,
                    fg=secondary_colour, bg=secondary_colour)
accountNameLabel.grid(row=3, column=0, columnspan=2, pady=(1,1), sticky=W)

accountName = Label(findPass,font=text_font,
                    text='username', fg=secondary_colour,
                    bg = secondary_colour, padx=20)
accountName.grid(row=4, column=0, columnspan=2, pady=(1,5))

accountPasswordLabel = Label(findPass, font=text_font,
                             text='Your password is:', padx=20,
                             fg=secondary_colour, bg=secondary_colour)
accountPasswordLabel.grid(row=5, column=0, columnspan=2, pady=(1,1), sticky=W)

accountPassword = Label(findPass, font=text_font,
                        text='password', fg=secondary_colour,
                        bg=secondary_colour, padx=20)
accountPassword.grid(row=6,column=0, columnspan=2, pady=(1,5))

# Start the event loop to detect user inputs
screen.mainloop() 

