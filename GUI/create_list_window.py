import tkinter as tk
import tkinter.ttk as ttk

from controllers.Videos_controller import controller
from models.model_video_lists import VideoList


class CreateListWindow(tk.Frame):
    columns_video = ["Id", "Title", "Director", "Rate"]

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.warning_shown = False
        # window display
        self.root = self.parent

        # Create get name frame
        self.name_frame = ttk.Frame(self.root)
        self.name_frame.pack(padx=10, pady=10)
        # Create a label for the search bar
        name_label = ttk.Label(self.name_frame, text="List Name: ")
        name_label.pack(side="left")
        # Create get name bar
        self.get_name = tk.Entry(self.name_frame, highlightthickness=1)
        self.get_name.pack(side="left", fill="x", expand=True)
        self.get_name.focus_set()

        """Display"""
        # Create a frame for the display
        main_display_frame = ttk.Frame(self.root)
        main_display_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Display 1
        self.all_videos_label = ttk.Label(main_display_frame, text="All videos")
        self.all_videos_label.grid(row=0, column=0, sticky="w")

        # Create Treeview
        self.all_videos = ttk.Treeview(main_display_frame, columns=self.columns_video, show="headings")

        # Configure Treeview columns
        self.all_videos.column("Id", width=30, anchor="center")
        self.all_videos.column("Rate", width=70, anchor="center")

        for col in self.columns_video:
            self.all_videos.heading(col, text=col)

        # Add a scrollbar for the Treeview
        self.all_videos_scrollbar = ttk.Scrollbar(main_display_frame, orient="vertical", command=self.all_videos.yview)

        # Configure the Treeview to use the scrollbar
        self.all_videos.configure(yscrollcommand=self.all_videos_scrollbar.set)

        # Place the Treeview and the scrollbar in the grid
        self.all_videos.grid(row=1, column=0, sticky="nsew")
        self.all_videos_scrollbar.grid(row=1, column=1, sticky="ns")

        self.display_video()
        # Display 2
        self.video_added_label = ttk.Label(main_display_frame, text="Video Added")
        self.video_added_label.grid(row=0, column=3, sticky="w")

        # Create Treeview
        self.video_added = ttk.Treeview(main_display_frame, columns=self.columns_video, show="headings")

        # Configure Treeview columns
        self.video_added.column("Id", width=30, anchor="center")
        self.video_added.column("Rate", width=70, anchor="center")

        for col in self.columns_video:
            self.video_added.heading(col, text=col)

        # Add a scrollbar for the Treeview
        self.video_added_scrollbar = ttk.Scrollbar(main_display_frame, orient="vertical",
                                                   command=self.video_added.yview)

        # Configure the Treeview to use the scrollbar
        self.video_added.configure(yscrollcommand=self.video_added_scrollbar.set)

        # Place the Treeview and the scrollbar in the grid
        self.video_added.grid(row=1, column=3, sticky="nsew")
        self.video_added_scrollbar.grid(row=1, column=4, sticky="ns")


        """BUTTONS"""
        # Create add button
        self.add_btn = ttk.Button(main_display_frame, text="Add Video", compound="left", command=self.add_video_function)
        # Change column and row parameters to place it between two Treeviews
        self.add_btn.grid(row=1, column=2, sticky="n", padx=10)

        # Create delete button
        self.del_btn = ttk.Button(main_display_frame, text="Remove Video", compound="left", command=self.remove_video_function)
        # Change column and row parameters to place it between two Treeviews
        self.del_btn.grid(row=1, column=2, sticky="s", padx=10)

        # Create create button
        self.create_btn = ttk.Button(self.root, text="Create", compound="left", command=self.create_function)
        self.create_btn.pack(side="right", padx=10, pady=10)


    def display_video(self):
        # Remove every children from the display
        for i in self.all_videos.get_children():  # return a list of child of objects on main_display
            self.all_videos.delete(i)  # remove that list from the display
            # For each data, add a new row to the display
        for video in controller.list_videos():  # For each data
            self.all_videos.insert("", "end", values=(
            video[0], video[1], video[2], "*" * video[3]))  # add a new row to the display

    detached_items = []
    def add_video_function(self):
        try:
            # Get the selected item ID from the source treeview
            selected_item = self.all_videos.selection()[0]
        except IndexError:
            return None
        # Get the values of the selected item
        values = self.all_videos.item(selected_item)["values"]
        # Get the video ID from the first value
        video_id = int(values[0])
        # Get the video title from the second value
        video_title = values[1]
        # Get the video director by calling the get_video_director method
        video_director = controller.get_video_director(video_id)
        # Get the video rate by calling the get_video_rate method
        video_rate = controller.get_video_rate(video_id)
        # Insert the values into the destination treeview
        self.video_added.insert("", "end", values=(video_id, video_title, video_director, "*" * video_rate))
        # Delete the selected item from the source treeview
        self.all_videos.delete(selected_item)


    def remove_video_function(self):
        try:
            # Get the selected item ID from the source treeview
            selected_item = self.video_added.selection()[0]
        except IndexError:
            return None
        # Get the values of the selected item
        values = self.video_added.item(selected_item)["values"]
        # Get the video ID from the first value
        video_id = int(values[0])
        # Get the video title from the second value
        video_title = values[1]
        # Get the video director by calling the get_video_director method
        video_director = controller.get_video_director(video_id)
        # Get the video rate by calling the get_video_rate method
        video_rate = controller.get_video_rate(video_id)
        # Insert the values into the destination treeview
        self.all_videos.insert("", "end", values=(video_id, video_title, video_director, "*" * video_rate))
        # Delete the selected item from the source treeview
        self.video_added.delete(selected_item)

    def create_function(self):
        video_list = []
        list_name = self.get_name.get()

        for line in self.video_added.get_children():
            video = self.video_added.item(line)["values"]
            video_list.append(str(video[0]))

        video_list = ", ".join(video_list)

        if not list_name:
            self.get_name.config(highlightbackground="red", highlightcolor="red")
            if not self.warning_shown:
                warning_label = tk.Label(self.name_frame, text="Name is required!", fg="red")
                warning_label.pack()
                self.warning_shown = True
            # change the color of the entry widget
        else:
            # do something with list_name and video_list
            VideoList.create_list(list_name, video_list)
            # destroy the window
            self.root.destroy()









