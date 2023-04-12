import win32gui
import psutil

def get_current_program():
    window = win32gui.GetForegroundWindow()
    program = win32gui.GetWindowText(window)
    return program

last_program = None

while True:
    current_program = get_current_program()
    if current_program != last_program:
        last_program = current_program
        
        print("Current program: ", current_program)

        
    # process_list = psutil.process_iter()
    # for process in process_list:
    #     try:
    #         process_name = process.name()
    #         if process_name == "notepad.exe":
    #             print("Notepad is running!")
    #     except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
    #         pass
