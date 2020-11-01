import pyshorteners
import pyperclip
from tkinter import*

window=Tk()
window.geometry("500x300")
window.title("URL SHORTENER")
window.configure(bg="#edb51a")
url = StringVar()
url_address = StringVar()

def urlshortener():
    url_entered= url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(url_entered)
    url_address.set(url_short)
def copyurl():
    url_short= url_address.get()
    pyperclip.copy(url_short)
Label(window,text="URL Shortener",font=("airel",19),bg="#edb51a",padx=10,pady=10).place(x=140,y=40)
Label(window,text="Enter the URL :",bg="#edb51a").place(x=50,y=100)
Entry(window,textvariable= url).place(x=140,y=100,width=200)
Button(window,text="Generate Short URL",command=urlshortener,activebackground="#011417",activeforeground="white",
       bg="#ebfa48").place(x=180,y=133)
Label(window,text="Short URL :",bg="#edb51a").place(x=69,y=170)
Entry(window,textvariable=url_address).place(x=140,y=170,width=200)
Button(window,text="Copy Short URL",command=copyurl,activebackground="#011417",activeforeground="white",
       bg="#ebfa48").place(x=186,y=200)
window.mainloop()