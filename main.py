
# import tkinter
import tkinter as tk
from GUI.main_window import MainWindow
# import the controller object
# create a root window without the title argument
root = tk.Tk()
# set the title of the window to "Video Player"
root.title("Video Player")
# create an instance of the MainWindow class
app = MainWindow(root)
# pack the app frame
app.pack()
# start the main loop of the root window
app.mainloop()
