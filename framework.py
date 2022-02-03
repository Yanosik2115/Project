from fileinput import filename
import shutil
from tkinter import *
import os
from tkinter import filedialog

from numpy import place
from Any2mp3 import convertToWav
import pygame

root = Tk()

class FrameWork:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Music Player")
        pygame.init()
        pygame.mixer.init()

        canvas = Canvas(root, height=700, width=700, bg="#263D42")
        canvas.pack()

        songs_display = Frame(root, bg="white")
        songs_display.place(width=250, height=665, relx=0, rely=0.05)

        self.control_panel = LabelFrame(root, bg="green")
        self.control_panel.place(width=250, height=100, x=0, y=600)

        os.chdir("../Project/Songs")
        songtrack = os.listdir()

        scrol = Scrollbar(songs_display, orient=VERTICAL)
        self.playlist = Listbox(
            songs_display,
            height=27,
            yscrollcommand=scrol.set,
            selectbackground="gold",
            selectmode=SINGLE,
            font=("times new roman", 12, "bold"),
            bg="silver",
            fg="navyblue",
            bd=5,
            relief=GROOVE,
        )

        scrol.pack(side=RIGHT, fill=BOTH)
        scrol.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)

        self.track = StringVar()
        self.status = StringVar()

        for track in songtrack:
            self.playlist.insert(END, track)

        play_but = Button(self.control_panel, text="PLAY", command=self.play)
        play_but.pack(side="right")
        openFile = Button(
            self.control_panel,
            text="Open File",
            fg="white",
            bg="#263D42",
            command=self.add_song,
        )
        openFile.pack(side="left")

    def play(self):
        self.track.set(self.playlist.get(ACTIVE))
        self.status.set("-Playing")
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        pygame.mixer.music.play()

    def stop(self):
        self.status.set("-Stopped")
        pygame.mixer.music.stop()

    def pause(self):
        self.status.set("-Paused")
        pygame.mixer.music.pause()

    def unpause(self):
        self.status.set("-Playing")
        pygame.mixer.music.unpause()

    def add_song(self):
        fileName = filedialog.askopenfilename(
            initialdir="~/Py/Project/",
            title="Select Song You would like to add",
            filetypes=(
                ("media_player", "*.mp3"),
                ("all files", "*.*"),
            ),
        )
        src = fileName
        dst = '/home/yanosik2115/Py/Project/Songs/'
        shutil.copyfile(src, '%s%s' % (dst,src.split('/')[-1]))
    

FrameWork(root)

root.mainloop()
