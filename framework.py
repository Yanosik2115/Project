import tkinter as tk
from tkinter import Frame, Label, Place, filedialog
from play import AudioFile

root = tk.Tk()
songs = []

def addSong():
    for each in song_display.winfo_children():
        each.destroy()

    fileName = filedialog.askopenfilename(initialdir='~', title='Select Song You would like to add',
    filetypes=(('media_player', '*.mp3'),('all files', '*.*')))

    #songs.append(tk.Button(song_display, text=fileName.split('/')[-1], bg='white', command=playSong(fileName.split('/')[-1])).pack())
    songs.append(fileName.split('/')[-1])
    # print(fileName)

    # for song in songs:
    #     song

    for song in songs:
        new_button = tk.Button(song_display, text=song, bg='white', command=playSong(song)).pack()
        

    #songs.append(newButton)

    #label = tk.Label(song_display, text=song, bg='gray')
    #label.pack()

def playSong(song):
    pass
    #print(song)
    # a = AudioFile(song)
    # a.play()
    # a.close()

canvas = tk.Canvas(root, height=700, width=700, bg='#263D42')
canvas.pack()

song_display = tk.Frame(root, bg='white')
song_display.place(width=250, height=665, relx=0, rely=0.05)

buttons = tk.Frame(root, bg='green')
buttons.place(width=250, height=100, x=0, y=600)

openFile = tk.Button(root, text='Open File', fg='white', bg='#263D42', command=addSong)
openFile.pack(side='left')


root.mainloop()
