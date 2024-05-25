from tkinter import *

# Creating a window
window = Tk()
window.geometry('650x400')
window.title("DataFlair Website Blocker")

heading = Label(window, text='Website Blocker', font='arial')
heading.pack()

host_path = r'C:\Windows\System32\drivers\etc\hosts'  # Use raw string to escape backslashes
ip_address = '127.0.0.1'

label1 = Label(window, text='Enter Website:', font='arial 13 bold')
label1.place(x=5, y=60)

enter_Website = Entry(window, font='arial', width=40)  # Use Entry widget instead of Text
enter_Website.place(x=140, y=60)

def block_website():
    website = enter_Website.get()
    with open(host_path, 'r+') as host_file:
        file_content = host_file.read()
        if website in file_content:
            display = Label(window, text='Already Blocked', font='arial')
            display.place(x=200, y=200)
        else:
            host_file.write(ip_address + " " + website + '\n')
            Label(window, text="Blocked", font='arial').place(x=230, y=200)

def unblock_website():
    website = enter_Website.get()
    with open(host_path, 'r+') as host_file:
        file_content = host_file.readlines()
        with open(host_path, 'w') as f:
            for line in file_content:
                if website not in line:
                    f.write(line)
            Label(window, text="Unblocked", font='arial').place(x=350, y=200)

block_button = Button(window, text='Block', font='arial', pady=5, command=block_website, width=6, bg='royal blue1', activebackground='grey')
block_button.place(x=230, y=150)

unblock_button = Button(window, text='Unblock', font='arial', pady=5, command=unblock_website, width=6, bg='royal blue1', activebackground='grey')
unblock_button.place(x=350, y=150)

window.mainloop()
