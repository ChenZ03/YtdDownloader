from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from pytube import YouTube

FolderName = ''


# FUNC
def find():
    global DLink
    ytl = DLink.get()
    yt = YouTube(ytl)
    link.config(text="Video : " + yt.title)


def folder():
    global FolderName
    FolderName = filedialog.askdirectory()
    if len(FolderName) > 1:
        ft.config(text=FolderName, fg="green")

    else:
        ft.config(text="Please choose folder!", fg="red")


def download():
    choice = yChoices.get()
    video = DLink.get()
    ytl = DLink.get()
    yt = YouTube(ytl)

    if len(video) > 1:
        if choice == choices[0]:
            vid = yt.streams.filter(adaptive=True).first()
            load.config(text="Downloading....")
            vid.download(FolderName)
        elif choice == choices[1]:
            vid = yt.streams.filter(progressive=True).first()
            load.config(text="Downloading......")
            vid.download(FolderName)
        elif choice == choices[2]:
            vid = yt.streams.filter(progressive=True).last()
            load.config(text="Downloading......")
            vid.download(FolderName)
        elif choice == choices[3]:
            vid = yt.streams.filter(only_audio=True).first()
            load.config(text="Downloading......")
            vid.download(FolderName)

    else:
        load.config(text="Choose another link")


# TKINTER WINDOW (GUI)
window = Tk()
window.title("Youtube Video Downloader")
window.grid_columnconfigure(0, weight=3)
window.geometry("500x600")
title = Label(window, text="Download your video here : ", fg="black", font=("Arial", 20))
title.grid(pady=10)
DLabel = Label(window, text=" YT Link :", fg="black", font=("Arial", 14))
DLabel.grid(column=0, row=2, padx=10, pady=5)
DLink = Entry(window, width=60)
DLink.grid()
DLink.focus_set()
Find = Button(window, text="Find link", fg="white", bg="blue", height=1, width=10, command=find)
Find.grid(column=0, row=4, padx=10, pady=10)
link = Label(window, text=" Video : ", fg="blue", font=("Arial", 10))
link.grid(column=0, row=5, padx=10, pady=5)
Folder = Button(window, text="CHOOSE FOLDER", fg="white", bg="blue", height=2, width=25, command=folder)
Folder.grid(column=0, row=6, padx=10, pady=20)
ft = Label(window, text=" Directory :", fg="blue", font=("Arial", 14))
ft.grid(column=0, row=7, pady=10)
format = Label(window, text=" File Format :", fg="black", font=("Arial", 10))
format.grid(column=0, row=8)
choices = ["1080p", "720p", "144p", "audio"]
yChoices = ttk.Combobox(window, values=choices)
yChoices.grid(column=0, row=9)
yChoices.current(1)
Download = Button(window, text="DOWNLOAD", font=("Arial", 16), fg="black", bg="grey", height=3, width=30, command=download)
Download.grid(column=0, row=10, padx=10, pady=50)
load = Label(window, text=" LOADING ", fg="black", font=("Arial", 10))
load.grid(column=0, row=11)
window.mainloop()

