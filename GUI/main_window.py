import tkinter as tk

from GUI.video_player import VideoPlayer

class MainWindow(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        self.show_video_player_frame()

    def show_frame(self, frame_classname):
        frame = frame_classname(self.container, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def show_video_player_frame(self):
        self.show_frame(VideoPlayer)

