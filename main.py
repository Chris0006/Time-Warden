# Functionality
import win32gui
import win32process
import psutil
import os
import signal

# GUI
import tkinter as tk
from tkinter import ttk

# Timer
import time

# Sound
import pygame # pygame is used for (game) sound

# Threading
import threading # allows to track many program simultaneously

def get_current_program():
    window = win32gui.GetForegroundWindow()
    pid = win32process.GetWindowThreadProcessId(window)[1]
    return pid

last_program = None
running_pids = [p.pid for p in psutil.process_iter()]

while True:
    current_program = get_current_program()
    if current_program != last_program:
        last_program = current_program
        if current_program not in running_pids:
            running_pids.append(current_program)
            program_name = win32gui.GetWindowText(win32gui.GetForegroundWindow())

            if len(program_name) > 0:
                # print("Launched program: ", current_program, program_name)
                
                def new_thread(pid, program_name):
                    try:
                        #GUI / Provide Time

                        ###############################################

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

                                self.label = ttk.Label(master, text=f'Program: {program_name}', font=self.label_font, foreground="white", background="#880808")
                                self.label.pack(pady=15)

                            def submit(self):
                                timer = self.time_entry.get()
                                try:
                                    timer = int(timer)
                                except: timer = 5  # if time is not specified correctly, the default is 5 minutes.
                                
                            
                                

                                # for debugging
                                # finally:
                                #     print(type(time))

                                # print("You plan to spend", timer, "minutes.")



                                # TIMER / TERMINATE TASK
                                ################################

                                # cheatcode
                                if timer == 0:
                                    self.master.destroy()
                                else:
                                    def end_process():
                                        # os.kill(pid, 0) # check if the process exists

                                        #########################################################

                                        class SessionExpiredGUI:
                                            def __init__(self, master):
                                                self.master = master
                                                master.title("Session Expired")
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

                                                # Create the label
                                                self.label = ttk.Label(master, text="Your session has expired.", font=self.label_font, foreground="white", background="#880808")
                                                self.label.pack(pady=15)

                                                # Create the continue button
                                                continue_style = ttk.Style()
                                                continue_style.configure("CustomContinue.TButton",
                                                    font=("Arial", 12),
                                                    foreground="#2E3840",
                                                    background="#880808",
                                                    borderwidth=0,
                                                    padx=20,
                                                    pady=10,
                                                    focuscolor="none",
                                                    focusthickness=0)
                                                continue_button = ttk.Button(master, text="Continue", style="CustomContinue.TButton", command=self.continue_session)
                                                continue_button.pack(pady=20)

                                                # Create the end session button
                                                endbtn_style = ttk.Style()
                                                endbtn_style.configure("CustomEndBtn.TButton",
                                                    font=("Arial", 14),
                                                    foreground="#2E3840",
                                                    background="#880808",
                                                    borderwidth=0,
                                                    padx=40,
                                                    pady=20,
                                                    focuscolor="none",
                                                    focusthickness=0)
                                                end_button = ttk.Button(master, text="End Session", style="CustomEndBtn.TButton", command=self.end_session)
                                                end_button.pack(pady=5)

                                                self.label = ttk.Label(master, text=f'Program: {program_name}', font=self.label_font, foreground="white", background="#880808")
                                                self.label.pack(pady=15)

                                            def continue_session(self):
                                                self.master.destroy()
                                                pygame.init() # Initialize Pygame
                                                file_name = "game_over.mp3" # Set the file name
                                                pygame.mixer.music.load(file_name) # Load the file
                                                pygame.mixer.music.play() # Play the file

                                                while pygame.mixer.music.get_busy(): # Wait for the file to finish playing
                                                    pass

                                                pygame.quit() # Quit Pygame
                                                

                                            def end_session(self):
                                                try:
                                                    self.master.destroy()
                                                    os.kill(pid, signal.SIGTERM) # send SIGTERM signal to kill the process
                                                    # print(f"Process with PID {pid} has been terminated.") 
                                                except Exception as f: print(f)

                                        root = tk.Tk()
                                        gui = SessionExpiredGUI(root)
                                        root.mainloop()

                                        #########################################################

                                        # os.kill(pid, signal.SIGTERM) # send SIGTERM signal to kill the process
                                        # print(f"Process with PID {pid} has been terminated.") 
                                                                    
                                    self.master.destroy()
                                    time.sleep(timer*60) # turn minutes into seconds
                                    end_process()
                                #################################



                        root = tk.Tk()
                        gui = TimeEntryGUI(root)
                        root.mainloop()

                        ################################################

                    except OSError as e:
                        pass
                        # print(f"Process with PID {pid} cannot be terminated:", e)
                threads = []
                t = threading.Thread(target=new_thread, args=(current_program, program_name))
                threads.append(t)
                t.start()

                # print("Thread finished")