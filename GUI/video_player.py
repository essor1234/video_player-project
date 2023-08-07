import tkinter as tk
import tkinter.ttk as ttk

from GUI.check_videos import CheckVideos
from GUI.create_video_list import CreateVideoList
from GUI.update_video import UpdateVideo

class VideoPlayer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


        # button frame
        self.main_frame = ttk.Frame(self)
        self.main_frame.grid(column=0, row=0)

        # check video button
        self.check_video_btn = ttk.Button(self.main_frame, text="Check Videos", command=self.check_video_frame_display)
        self.check_video_btn.config(width=25)
        self.check_video_btn.grid(row=0, column=0, padx=5, pady=5)

        # create video list button
        self.create_list_btn = ttk.Button(self.main_frame, text="Create Video List", command=self.create_video_list_frame_display)
        self.create_list_btn.config(width=25)
        self.create_list_btn.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        # Update Videos button
        self.update_video_btn = ttk.Button(self.main_frame, text="Update Videos", command=self.update_video_frame_display)
        self.update_video_btn.config(width=25)
        self.update_video_btn.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")




    def check_video_frame_display(self):
        # create a Toplevel widget
        new_window = tk.Toplevel(self.master)
        # create a CheckVideo frame inside the new window
        check_video_frame = CheckVideos(new_window)
        # create name
        new_window.title("Check Video")
        # pack the CheckVideo frame
        check_video_frame.pack()

    def create_video_list_frame_display(self):
        # create a Toplevel widget
        new_window = tk.Toplevel(self)
        # create a CheckVideo frame inside the new window
        check_video_frame = CreateVideoList(new_window)
        # create name
        new_window.title("Create Video List")
        # pack the CheckVideo frame
        check_video_frame.pack()

    def update_video_frame_display(self):
        # create a Toplevel widget
        new_window = tk.Toplevel(self)
        # create a CheckVideo frame inside the new window
        check_video_frame = UpdateVideo(new_window)
        # create name
        new_window.title("Update Videos")
        # pack the CheckVideo frame
        check_video_frame.pack()
