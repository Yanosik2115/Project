from fileinput import filename
import shutil
from tkinter import *
import os
from tkinter import filedialog
from matplotlib.pyplot import text

from numpy import place
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

        play_but = Button(self.control_panel, text="PLAY", command=self.test)
        play_but.place(x=0, y=0)

        stop_but = Button(self.control_panel, text="STOP", command=self.stop)
        stop_but.place(x=60, y=0)

        pause_but = Button(self.control_panel, text="PAUSE", command=self.pause)
        pause_but.place(x=120, y=0)

        unpause_but = Button(self.control_panel, text="UNPAUSE", command=self.unpause)
        unpause_but.place(x=180, y=0)

        openFile = Button(
            self.control_panel,
            text="Open File",
            fg="white",
            bg="#263D42",
            command=self.add_song,
        )
        openFile.place(x=0, y=67)

        self.show_playlist()

    def play(self):
        self.track.set(self.playlist.get(ACTIVE))
        self.status.set("-Playing")
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        pygame.mixer.music.play()

    def stop(self):
        self.status.set("-Stopped")
        pygame.mixer.music.stop()
    
    def test(self):
        if not self.track.get():
            self.track.set(self.playlist.get(ACTIVE))
            self.status.set("-Playing")
            pygame.mixer.music.load(self.playlist.get(ACTIVE))
            pygame.mixer.music.play()
        elif self.status.get() == '-Unpaused' or self.status.get() == '-Playing':
            self.status.set("-Paused")
            pygame.mixer.music.pause()
        elif self.status.get() == '-Paused':
            self.status.set("-Playing")
            pygame.mixer.music.unpause()
        print(self.playlist.get(ACTIVE))



    def pause(self):
        self.status.set("-Paused")
        pygame.mixer.music.pause()

    def unpause(self):
        self.status.set("-Playing")
        pygame.mixer.music.unpause()

    def show_playlist(self):
        self.playlist.delete(0, END)

        self.songtrack = os.listdir()
        for track in self.songtrack:
            self.playlist.insert(END, track)

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
        shutil.copyfile(src, "%s%s" % (dst, src.split("/")[-1]))

        self.show_playlist()


FrameWork(root)
root.mainloop()
