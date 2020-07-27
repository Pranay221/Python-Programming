from pytube import YouTube
from tkinter import *

root=Tk()
root.title("YouTube Video Downloader Application")
root.geometry("400x350")

def download():
    try:
        myVar.set("Downloading...")
        root.update()
        YouTube(link.get()).streams.first().download()
        link.set("Video Downloaded Successfully.")
    except Exception as e:
        myVar.set("Mistake")
        root.update()
        link.set("Enter correct link")

myVar = StringVar()
Label(root, text="Welcome to YouTube\nDownloaderApplication", font="Consolas 15 bold").pack()
myVar.set("Enter the link below")
Entry(root, textvariable=myVar, width=40).pack(pady=10)
link= StringVar()
Entry(root, textvariable=link, width=40).pack(pady=10)
Button(root, text="Download Video", command=download).pack()

mainloop()