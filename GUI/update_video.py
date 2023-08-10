from controllers.Videos_controller import controller
from models.model_videos import Videos

import tkinter as tk
import tkinter.ttk as ttk

from GUI.update_window import UpdateWindow





class UpdateVideo(tk.Frame):
    columns = ["Id", "Title", "Director", "Rate"]

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        # Create a grid layout manager

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

        btn_list_all = ttk.Button(self.search_frame, text="Refresh",
                                  command= self.list_all)
        btn_list_all.grid(row=0, column=4)

        # Create a frame for the buttons
        button_frame = ttk.Frame(self)
        button_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10)



        # Create a button to list all items
        del_btn = ttk.Button(button_frame, text="Delete", compound="left",
                                  command=self.delete_function)
        del_btn.config(width=15)
        del_btn.grid(row=0, column=2)

        # Create a button to list all items
        btn_list_all = ttk.Button(button_frame, text="Update", compound="left",
                                  command=self.combine)
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

        self.list_all()

    def list_all(self):
        # Remove every children from the display
        for i in self.main_display.get_children():
            self.main_display.delete(i)
            # For each data, add a new row to the display
        for video in controller.list_videos():
            self.main_display.insert("", "end", values=(video[0], video[1], video[2], "*" * video[3]))

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

    def update_window_frame_display(self):
        item_id = self.main_display.focus()
        if item_id:
            # create a Toplevel widget
            new_window = tk.Toplevel(self)
            # create a CheckVideo frame inside the new window
            check_video_frame = UpdateWindow(new_window, self)
            # create name
            new_window.title("Update")
            check_video_frame.grid()

    def info_for_chosen_video(self):
        try:
            item_id = self.main_display.focus()
            item = self.main_display.item(item_id, "values")
            try:
                item = int(item[0])

            except ValueError:
                item = -1

            video_title = controller.get_video_title(item)
            video_director = controller.get_video_director(item)
            video_rate = controller.get_video_rate(item)
            video_play = controller.get_video_play(item)

            return video_title, video_director, video_rate, video_play, item
        except IndexError:
            warning_label = tk.Label(self.search_frame, text="PLease choose a video to optimize", fg="red")
            warning_label.grid(row=1, column=1)
            warning_label.after(1000, warning_label.destroy)

    # help 2 functions run at the same button
    def combine(self):
        self.update_window_frame_display()
        self.info_for_chosen_video()

    def delete_function(self):
        selected_items = self.main_display.selection()
        # check if there is video to delete
        if not selected_items:
            warning_label = tk.Label(self.search_frame, text="Please choose a video to delete", fg="red")
            warning_label.grid(row=1, column=1)
            warning_label.after(1000, warning_label.destroy)
            return

        for item in selected_items:
            try:
                video_id = int(self.main_display.item(item)["values"][0])
            except ValueError:
                video_id = -1
            is_deleted = Videos.delete_video(video_id)

            if is_deleted:
                self.main_display.delete(item)


'''if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()  # create a TK object
    UpdateVideo(window)  # open the CheckVideo GUI
    window.mainloop()'''