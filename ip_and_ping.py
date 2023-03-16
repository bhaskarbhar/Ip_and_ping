from tkinter import *
from tkinter import messagebox
import subprocess
    
def get_ip():
    ip_bytes = subprocess.check_output(['curl', 'ifconfig.me', '-s'])
    ip = ip_bytes.decode('utf-8')
    messagebox.showinfo("Your device' s ip","Ip: " + ip)

window = Tk()
window.title("Network tools")
window.geometry("650x650")
window.configure(bg = "#b83ba1")
button_ip= Button(window, text="Get your IP address", command= get_ip)
button_ip.configure(font= 100)
button_ip.place(x=230,y=250)

label_ping = Label(window, text = "Enter any ip \nor website name: ")
label_ping.configure(bg = "#b83ba1", font = 5)
label_ping.place(x=60,y=310)

ping_entry = Entry(window, font = 5)
ping_entry.place(x=230, y=330)
global entry_ping
entry_ping = str(ping_entry.get())


def get_ping():
    
    ping_output = subprocess.check_output(["ping", entry_ping])
    messagebox.showinfo("Ping data",ping_output)

button_ping= Button(window, text="Ping any ip or website", command = get_ping)
button_ping.configure(font= 100)
button_ping.place(x=230,y=380)

window.mainloop()
