import tkinter as tk
from tkinter import Frame, Label, Place, filedialog
from play import AudioFile

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

    for i in songs:
         button.append(tk.Button(
            song_display, text=i, bg="white", command=lambda j=i: AudioFile(i).play()
        ).pack())
         print(i)

def addSong():
    fileName = filedialog.askopenfilename(
        initialdir="~",
        title="Select Song You would like to add",
        filetypes=(("media_player", "*.mp3"), ("all files", "*.*")),
    )
    songs.append(fileName.split("/")[-1])
    showButtons()
    

openFile = tk.Button(
    root, text="Open File", fg="white", bg="#263D42", command=addSong
)
openFile.pack(side="left")

root.mainloop()
