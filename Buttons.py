from tkinter import *
from framework import FrameWork 
from play import ButtonsControl

class Buttons:
    def __init__(self) -> None:
        self.fw = FrameWork()
        self.bc = ButtonsControl()

    def but(self):
        play_but = Button(self.fw.control_panel, text='PLAY', command=self.bc.play())

        openFile = Button(
            self.fw.control_panel, text="Open File", fg="white", bg="#263D42", command=addSong
        )
        openFile.pack(side="left")

