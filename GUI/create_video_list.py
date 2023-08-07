from controllers.Videos_controller import controller
from models.model_videos import Videos
from models.model_video_lists import VideoList


import tkinter as tk
import tkinter.ttk as ttk

from GUI.create_list_window import CreateListWindow
from GUI.list_option_window import ListOptionWindow


class CreateVideoList(tk.Frame):
    columns_list = ["Id", "Title", "Length"]
    columns_video = ["Id", "Title", "Director", "Rate"]

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.parent = parent

        # Create a grid layout manager
        self.grid()

        # Create frame for search bar
        self.search_frame = ttk.Frame(self)
        self.search_frame.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Create a label for the search bar
        search_label = ttk.Label(self.search_frame, text="Search by:")
        search_label.grid(row=0, column=0)

        # Create entry widget
        self.search_entry = ttk.Entry(self.search_frame)
        self.search_entry.grid(row=0, column=1)

        # Create a list of search options
        search_options = ["Id", "Title"]
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
        # List all button
        self.list_all_btn = ttk.Button(self.search_frame, text="List All", command=self.list_all)
        self.list_all_btn.grid(row=0, column=4)



        """Display"""
        # LIST DISPLAY
        # Create a frame for the display
        main_display_frame = ttk.Frame(self)
        main_display_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=10 )

        # Create label of list_display_label
        self.list_display_label = ttk.Label(main_display_frame, text="My Lists")
        self.list_display_label.grid(row=1, column=0, sticky="w")
        # Create Treeview
        self.list_display = ttk.Treeview(main_display_frame, columns=self.columns_list, show="headings")
        self.list_display.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        # Configure Treeview columns
        self.list_display.column("Id", width=30, anchor="center")
        self.list_display.column("Length", width=70, anchor="center")
        for col in self.columns_list:
            self.list_display.heading(col, text=col)
        # Bind the function to the double click event
        self.list_display.bind("<Double-1>", self.video_in_list_display )
        self.list_display.bind("<Button-1>", self.on_click)


        # VIDEO IN LIST
        self.video_display_label = ttk.Label(main_display_frame, text="Videos in list")
        self.video_display_label.grid(row=1, column=6, sticky="w")
        # Create Treeview
        self.video_display = ttk.Treeview(main_display_frame, columns=self.columns_video, show="headings")
        self.video_display.grid(row=2, column=6, columnspan=3, padx=10, pady=10)
        # Configure Treeview columns
        self.video_display.column("Id", width=30, anchor="center")
        self.video_display.column("Rate", width=70, anchor="center")
        for col in self.columns_video:
            self.video_display.heading(col, text=col)

        """BUTTONS"""
        # Create frame for buttons
        self.button_frame = ttk.Frame(self)
        self.button_frame.grid(row=2, column=0)
        # Create list button
        self.create_list = ttk.Button(self.button_frame, text="New List", compound="left", command=self.create_list_window_frame_display)
        self.create_list.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="w")
        self.create_list.config(width=50)
        # Play button
        self.play_button = ttk.Button(self.button_frame, text="Play", compound="left", command=self.increase_plays)
        self.play_button.grid(row=0, column=6, columnspan=3, padx=10, pady=10, sticky="w")
        self.play_button.config(width=25)
        # List change button
        self.list_change = ttk.Button(self.button_frame, text="List Option", compound="left", command=self.combine)
        self.list_change.grid(row=0, column=9, columnspan=3, padx=10, pady=10, sticky="w")
        self.list_change.config(width=25)
        # Delete list button
        self.delete_list = ttk.Button(self.button_frame, text="Delete List", compound="left", command=self.delete_function)
        self.delete_list.grid(row=0, column=12, columnspan=3, padx=10, pady=10, sticky="w")
        self.delete_list.config(width=50)

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

    def increase_plays(self):
        selected_items = self.list_display.selection()
        if not selected_items:
            warning_label = tk.Label(self.search_frame, text="Please choose a list to play", fg="red")
            warning_label.grid(row=1, column=1)
            warning_label.after(1000, warning_label.destroy)
            return

        for item in selected_items:
            try:
                list_id = int(self.list_display.item(item)["values"][0])
            except ValueError:
                list_id =-1
                warning_label = tk.Label(self.search_frame, text="PLease choose a list to optimize", fg="red")
                warning_label.grid(row=1, column=1)
            # call the plays_count() method with the list id variable as an argument only once
            Videos.plays_count(list_id)
            warning_label = tk.Label(self.search_frame, text=f"All videos in list {list_id} have been playing", fg="green")
            warning_label.grid(row=1, column=1)
            warning_label.after(700, warning_label.destroy)



    def update_search_mode(self, selected_mode):
        # Clear the treeview widget
        self.list_display.delete(*self.list_display.get_children())

        search_value = self.search_entry.get()
        # Perform the search based on the selected mode and update the display
        if not search_value:
            warning_label = tk.Label(self.search_frame, text="Please enter a search value", fg="red")
            warning_label.grid(row=1, column=1)
            warning_label.after(1000, warning_label.destroy)
            return
        # if the selected mode is "Title":
        if selected_mode == "Title":
            # Perform the search and update the display
            for list in controller.find_list_by_title(search_value):
                self.list_display.insert("", "end", values=(list[0], list[1], list[2]))
        # if the selected mode is "Id":
        elif selected_mode == "Id":
            try:
                search_value = int(search_value)
                for list in controller.find_list_by_id(search_value):
                    # If it is a list, access the elements as usual
                    self.list_display.insert("", "end", values=(list[0], list[1], list[2]))
            except ValueError:
                warning_label = tk.Label(self.search_frame, text="Please enter a valid integer!", fg="red")
                warning_label.grid(row=1, column=1)
            except IndexError:
                warning_label = tk.Label(self.search_frame, text=f"There's no {search_value}th video!", fg="red")
                warning_label.grid(row=1, column=1)
                warning_label.after(700, warning_label.destroy)

    def create_list_window_frame_display(self):
        # create a Toplevel widget
        new_window = tk.Toplevel(self)
        # create a CheckVideo frame inside the new window
        check_video_frame = CreateListWindow(new_window)
        # create name
        new_window.title("New List")
        # pack the CheckVideo frame
        check_video_frame.pack()

    #TODO: work on this
    def list_option_window_frame_display(self):
            selected_items = self.list_display.focus()
            if selected_items:
                # create a Toplevel widget
                new_window = tk.Toplevel(self)
                # create a CheckVideo frame inside the new window
                # In create_video_list.py
                check_video_frame = ListOptionWindow(new_window, self)  # Pass self as an argument
                # create name
                new_window.title("List Option")
                # pack the CheckVideo frame
                check_video_frame.pack()


    def info_for_chosen_list(self):
        try:
            item_id = self.list_display.focus()
            item = self.list_display.item(item_id, "values")
            try:
                list_id = int(item[0])
                list_title = item[1]
            except ValueError:
                list_id = -1
                list_title = "None"

            return list_id, list_title
        except IndexError:
            warning_label = tk.Label(self.search_frame, text="PLease choose a list to optimize", fg="red")
            warning_label.grid(row=1, column=1)
            warning_label.after(1000, warning_label.destroy)

    # allow using 2 function in the same button
    def combine(self):
        self.list_option_window_frame_display()
        self.info_for_chosen_list()

    def video_in_list_display(self, event):
        self.video_display.delete(*self.video_display.get_children())
        # get the selected item from the event widget
        item_id = event.widget.focus()
        item = event.widget.item(item_id, "values")
        try:
            list_id = item[0]
        except ValueError:
            list_id = -1
        for video in controller.display_videos_in_list(list_id):
            self.video_display.insert("", "end", values=(video[0], video[1], video[2], "*" * int(video[3])))

    def delete_function(self):
            selected_items = self.list_display.selection()
            if not selected_items:
                warning_label = tk.Label(self.search_frame, text="Please choose a list to delete", fg="red")
                warning_label.grid(row=1, column=1)
                warning_label.after(1000, warning_label.destroy)
                return
            for item in selected_items:
                try:
                    list_id = int(self.list_display.item(item)["values"][0])
                except ValueError:
                    list_id = -1
                    warning_label = tk.Label(self.search_frame, text="Please choose a list to delete", fg="red")
                    warning_label.grid(row=1, column=1)
                    warning_label.after(1000, warning_label.destroy)

                is_deleted = VideoList.delete_list(list_id)

                if is_deleted:
                    self.list_display.delete(item)
                    for video in self.video_display.get_children():
                        self.video_display.delete(video)


    def list_all(self):
        # Remove every children from the display
        for i in self.list_display.get_children(): # return a list of child of objects on main_display
            self.list_display.delete(i) # remove that list from the display
            # For each data, add a new row to the display
        for item in controller.list_list(): # For each data
            self.list_display.insert("", "end", values=(item[0], item[1], item[3])) # add a new row to the display



'''if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()  # create a TK object
    CreateVideoList(window)  # open the CheckVideo GUI
    window.mainloop()'''