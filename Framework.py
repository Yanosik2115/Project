from fileinput import filename, nextfile
from operator import index
import shutil
from tkinter import *
import os
from tkinter import filedialog
from numpy import place
import pygame
from Any2mp3 import Converter

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

        self.play_but = Button(
            self.control_panel, text="PLAY", command=self.play_stop_but
        )
        self.play_but.pack(side=TOP)

        next_but = Button(self.control_panel, text='>', command=self.next_but)
        next_but.pack(side=RIGHT)

        openFile = Button(
            self.control_panel,
            text="Open File",
            fg="white",
            bg="#263D42",
            command=self.add_song,
        )
        openFile.place(x=0, y=67)

        self.show_playlist()

    def play_stop_but(self):
        if not self.status.get():
            self.track.set(self.playlist.get(ACTIVE))
            self.status.set("-Playing")
            pygame.mixer.music.load(self.playlist.get(ACTIVE))
            pygame.mixer.music.play()
        elif self.playlist.get(ACTIVE) != self.track.get():
            self.track.set(self.playlist.get(ACTIVE))
            self.status.set("-Playing")
            pygame.mixer.music.load(self.playlist.get(ACTIVE))
            pygame.mixer.music.play()
        elif (
            self.status.get() == "-Playing"
            and self.playlist.get(ACTIVE) == self.track.get()
        ):
            self.status.set("-Paused")
            pygame.mixer.music.pause()
        elif self.status.get() == "-Paused":
            self.status.set("-Playing")
            pygame.mixer.music.unpause()

        if self.status.get() == "-Playing":
            self.play_but.config(text="STOP")
        else:
            self.play_but.config(text="PLAY")

    def next_but(self):
        next_song = self.playlist.get(self.playlist.index(ACTIVE) + 1)
        self.track.set(next_song)
        self.status.set("-Playing")
        self.playlist.activate(self.playlist.index(ACTIVE) + 1)
        pygame.mixer.music.load(next_song)
        pygame.mixer.music.play()
        print(self.playlist.get(ACTIVE))
        print(self.track.get())
        #print(self.playlist.index(ACTIVE))

    def show_playlist(self):
        self.playlist.delete(0, END)

        self.songtrack = os.listdir()
        for num, track in enumerate(self.songtrack):
            self.playlist.insert(num, track)
        print(self.playlist.get(0))

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
        dst = "/home/yanosik2115/Py/Project/Songs/"

        if not fileName.endswith(".mp3"):
            Converter(fileName)
        else:
            shutil.copyfile(src, "%s%s" % (dst, src.split("/")[-1]))

        self.show_playlist()

FrameWork(root)
root.mainloop()
