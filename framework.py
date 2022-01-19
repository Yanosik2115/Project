import queue
import tkinter as tk
from tkinter import Frame, Label, Place, filedialog
from converter import convertToWav
from play import AudioFile, PlayQueue
from queue import Queue

root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

song_display = tk.Frame(root, bg="white")
song_display.place(width=250, height=665, relx=0, rely=0.05)

_buttons = tk.Frame(root, bg="green")
_buttons.place(width=250, height=100, x=0, y=600)

songs = []

def showButtons():
    
    button = []
    for each in song_display.winfo_children():
        each.destroy() 
    pq = PlayQueue()
    for i in songs:
        
        button.append(
            tk.Button(
                song_display, text=i, bg="white", command=lambda j=i: pq.threading(i)
            ).pack()
        )
        print(i)


def addSong():
    fileName = filedialog.askopenfilename(
        initialdir="~/Py/Project/",
        title="Select Song You would like to add",
        filetypes=(("media_player", "*.mp3"), ("all files", "*.*")),
    )
    if fileName.endswith(".mp3"):
        fileName = fileName.split("/")[-1]
        convertToWav(fileName)
        fileName = fileName.split(".")[0] + ".wav"
        print(fileName)

    print(fileName)
    songs.append(fileName.split("/")[-1])
    showButtons()


openFile = tk.Button(root, text="Open File", fg="white", bg="#263D42", command=addSong)
openFile.pack(side="left")

root.mainloop()
