import tkinter as tk
from tkinter import ttk

class TimeEntryGUI:
    def __init__(self, master):
        self.master = master
        master.title("Time Entry")
        master.geometry("350x250")
        master.configure(bg="#880808")
        self.label_font = ("Arial", 12, "bold")

        # Center the window on the screen
        master.update_idletasks()
        x = (master.winfo_screenwidth() - master.winfo_reqwidth()) / 2.25
        y = (master.winfo_screenheight() - master.winfo_reqheight()) / 3.5
        master.geometry("+%d+%d" % (x, y))

        # Make the window non-resizeable
        master.resizable(False, False)

        # Focus on the window
        master.lift()
        master.attributes("-topmost", True)
        master.after_idle(master.attributes, "-topmost", False)

        # Create the time entry label and input field
        self.label = ttk.Label(master, text="How much time do you plan to spend?", font=self.label_font, foreground="white", background="#880808")
        self.label.pack(pady=15)

        time_var = tk.StringVar()


        def on_entry_click(event):
            if time_var.get() == 'Enter time in minutes':
                time_var.set('')

        def on_focusout(event):
            if time_var.get() == '':
                time_var.set('Enter time in minutes')

        self.time_entry = ttk.Entry(master, textvariable=time_var, width=25, font=("Helvetica", 14))
        self.time_entry.insert(0, 'Enter time in minutes')
        self.time_entry.bind('<FocusIn>', on_entry_click)
        self.time_entry.bind('<FocusOut>', on_focusout)
        self.time_entry.pack(pady=10)

        # Create the submit button
        style = ttk.Style()
        style.configure("CustomButton.TButton",
                        font=("Helvetica", 14),
                        foreground="black",
                        background="#FF5733",
                        borderwidth=0,
                        padx=20,
                        pady=10,
                        focuscolor="none",
                        focusthickness=0)

        submit_button = ttk.Button(master, text="Submit", style="CustomButton.TButton", command=self.submit)
        submit_button.pack(pady=20)

    def submit(self):
        time = self.time_entry.get()
        try:
            time = int(time)
        except: time = 5  # if time is not specified correctly, the default is 5 minutes.
        
        # cheatcode
        if time == 66:
            time = 9999999
        

        # for debugging
        # finally:
        #     print(type(time))


        print("You plan to spend", time, "minutes.")

root = tk.Tk()
gui = TimeEntryGUI(root)
root.mainloop()
