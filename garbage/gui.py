import tkinter as tk
from tkinter import ttk

class TimeEntryGUI:
    def __init__(self, master):
        self.master = master
        master.title("Time Entry")
        master.geometry("300x250")
        master.configure(bg="#880808")
        self.label_font = ("Arial", 14, "bold")

        # Center the window on the screen
        x = (master.winfo_screenwidth() - master.winfo_reqwidth()) / 2
        y = (master.winfo_screenheight() - master.winfo_reqheight()) / 3.5
        master.geometry("+%d+%d" % (x, y))

        # Make the window non-resizeable
        master.resizable(False, False)

        # Create the time entry label and input field
        self.label = ttk.Label(master, text="How much time do you plan to spend?", font=self.label_font, foreground="white", background="#880808")
        self.label.pack(pady=15)

        self.time_entry = ttk.Entry(master, width=20, font=self.label_font)
        self.time_entry.pack(pady=10)

        # Create the submit button
        self.submit_button = ttk.Button(master, text="Submit", command=self.submit)
        self.submit_button.pack(pady=20)

    def submit(self):
        time = self.time_entry.get()
        print("You plan to spend", time, "minutes.")

root = tk.Tk()
gui = TimeEntryGUI(root)
root.mainloop()
