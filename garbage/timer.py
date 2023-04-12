import psutil
import time

process_name = "notepad.exe"
total_time = 0

for proc in psutil.process_iter():
    if proc.name() == process_name:
        process = psutil.Process(proc.pid)
        start_time = process.create_time()
        total_time += time.time() - start_time

print("Time spent in", process_name, ": ", total_time, "seconds")

import win32gui
import time

time.sleep(2)

def get_current_program():
    window = win32gui.GetForegroundWindow()
    program = win32gui.GetWindowText(window)
    return program

current_program = get_current_program()
print("Current program: ", current_program)
