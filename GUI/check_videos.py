from controllers.Videos_controller import controller

import tkinter as tk
import tkinter.ttk as ttk



class CheckVideos(tk.Frame):
    columns = ["Id", "Title", "Director", "Rate"]

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        # Create a grid layout manager
        # Set the geometry of the new window
        self.grid()

        # Create a frame for the search bar
        self.search_frame = ttk.Frame(self)
        self.search_frame.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Create a label for the search bar
        search_label = ttk.Label(self.search_frame, text="Search by:")
        search_label.grid(row=0, column=0)

        # Create entry widget
        self.search_entry = ttk.Entry(self.search_frame)
        self.search_entry.grid(row=0, column=1)

        # Create a list of search options
        search_options = ["Title", "Director", "Rate", "Id"]
        # Create a variable to store the selected option
        self.selected_option = tk.StringVar()
        # Set the default value of the variable to the first option
        self.selected_option.set(search_options[0])
        # Create a Combobox for the search options
        self.search_combobox = ttk.Combobox(self.search_frame, textvariable=self.selected_option, values=search_options)
        self.search_combobox.config(width=10)
        self.search_combobox.grid(row=0, column=2)


        # Create a button to check a video
        btn_check_video = ttk.Button(self.search_frame, text="Search", compound="left",
                                     command=lambda: self.update_search_mode(self.search_combobox.get()))
        btn_check_video.config(width=15)
        btn_check_video.grid(row=0, column=3)

        # Create a frame for the buttons
        button_frame = ttk.Frame(self)
        button_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10)



        # Create a button to list all items
        btn_check_video = ttk.Button(button_frame, text="Check_video", compound="left",
                                  command=self.check_video)
        btn_check_video.config(width=15)
        btn_check_video.grid(row=0, column=2)

        # Create a button to list all items
        btn_list_all = ttk.Button(button_frame, text="List All", compound="left",
                                  command=self.list_all)
        btn_list_all.config(width=15)
        btn_list_all.grid(row=0, column=0)

        # Create Treeview
        self.main_display = ttk.Treeview(self, columns=self.columns, show="headings")
        self.main_display.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        self.main_display.column("Id", width=30, anchor="center")
        self.main_display.column("Rate", width=70, anchor="center")

        # Configure Treeview columns
        for col in self.columns:
            self.main_display.heading(col, text=col)

        self.main_display.bind("<Button-1>", self.on_click)

        # Create Listbox widget
        self.listbox = tk.Listbox(self)
        self.listbox.grid(row=1, column=4, rowspan=2, padx=10, pady=10)
        # Insert data

    def on_click(self, event):
        # get the Treeview widget
        tree = event.widget
        # get the clicked area
        x, y = event.x, event.y
        # get the row at the clicked position
        row = tree.identify_row(y)
        # if the row is empty (outside of the Treeview widget)
        if not row:
            # clear the current selection
            tree.selection_remove(tree.selection())

    def list_all(self):
        # Remove every children from the display
        for i in self.main_display.get_children(): # return a list of child of objects on main_display
            self.main_display.delete(i) # remove that list from the display
            # For each data, add a new row to the display
        for video in controller.list_videos(): # For each data
            self.main_display.insert("", "end", values=(video[0], video[1], video[2], "*" * int(video[3]))) # add a new row to the display

    def check_video(self):
        # get the selected video ids from the treeview
        video_ids = self.main_display.selection()
        # clear the listbox
        self.listbox.delete(0, tk.END)
        # loop over each video id in the tuple
        if not video_ids:
            warning_label = tk.Label(self.search_frame, text="Please choose a list to delete", fg="red")
            warning_label.grid(row=1, column=1)
            warning_label.after(1000, warning_label.destroy)
            return

        for video_id in video_ids:
            # get the values of the video item
            values = self.main_display.item(video_id, "values")
            try:
                # get the video key from the values
                video_key = int(values[0])
            except IndexError:
                # if there is no value, skip this video
                continue
            # check if the video key is valid
            video_title, video_director, video_rate, video_plays = controller.check_video(video_key)
            # insert a blank line between each video
            self.listbox.insert(tk.END, "")
            # insert the video details into the listbox
            self.listbox.insert(tk.END, video_title)
            self.listbox.insert(tk.END, video_director)
            self.listbox.insert(tk.END, "Rate: " + str(video_rate))
            self.listbox.insert(tk.END, "Plays: " + str(video_plays))





    def update_search_mode(self, selected_mode):
        # Clear the treeview widget
        self.main_display.delete(*self.main_display.get_children())
        # get input from user
        search_value = self.search_entry.get()
        if not search_value:
            warning_label = tk.Label(self.search_frame, text="Please enter a search value", fg="red")
            warning_label.grid(row=1, column=1)
            warning_label.after(1000, warning_label.destroy)
            return
        # Perform the search based on the selected mode and update the display
        # if the selected mode is "Title":
        if selected_mode == "Title":
            # Perform the search and update the display
            try:
                for video in controller.find_videos_by_title(search_value):
                    self.main_display.insert("", "end", values=(video[0], video[1], video[2], "*" * int(video[3])))
            except TypeError:
                    self.main_display.insert("", "end", values=("", "None", "", ""))

        # if the selected mode is "Id":
        elif selected_mode == "Id":
            try:
                search_value = int(search_value)
                for video in controller.find_videos_by_id(search_value):
                    self.main_display.insert("", "end", values=(video[0], video[1], video[2], "*" * int(video[3])))
            except ValueError:
                warning_label = tk.Label(self.search_frame, text="Please enter a valid integer!", fg="red")
                warning_label.grid(row=1, column=1)
                warning_label.after(1000, warning_label.destroy)
            except IndexError:
                warning_label = tk.Label(self.search_frame, text=f"There's no {search_value}th video!", fg="red")
                warning_label.grid(row=1, column=1)
                warning_label.after(1000, warning_label.destroy)
            except TypeError:
                    self.main_display.insert("", "end", values=("", "None", "", ""))
        # if the selected mode is "Director":
        elif selected_mode == "Director":
            try:
                for video in controller.find_videos_by_director(search_value):
                    self.main_display.insert("", "end", values=(video[0], video[1], video[2], "*" * int(video[3])))
            except TypeError:
                    self.main_display.insert("", "end", values=("", "None", "", ""))

        # if the selected mode is "Rate":
        elif selected_mode == "Rate":
            try:
                search_value = int(search_value)
                for video in controller.find_videos_by_rate(search_value):
                    self.main_display.insert("", "end", values=(video[0], video[1], video[2], "*" * int(video[3])))
            except ValueError:
                warning_label = tk.Label(self.search_frame, text="Please enter a valid integer!", fg="red")
                warning_label.grid(row=1, column=1)
                warning_label.after(1000, warning_label.destroy)
            except IndexError:
                warning_label = tk.Label(self.search_frame, text=f"There's no {search_value} rate !", fg="red")
                warning_label.grid(row=1, column=1)
                warning_label.after(1000, warning_label.destroy)
            except TypeError:
                warning_label = tk.Label(self.search_frame, text=f"There's no {search_value} rate !", fg="red")
                warning_label.grid(row=1, column=1)
                warning_label.after(1000, warning_label.destroy)






