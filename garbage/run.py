import win32gui
# import psutil

def get_current_program():
    window = win32gui.GetForegroundWindow()
    program = win32gui.GetWindowText(window)
    return program

last_program = None

while True:
    current_program = get_current_program()
    if current_program != last_program:
        last_program = current_program

        
        if len(current_program) > 0:

            print("Current program: ", current_program)






# for tracking other apps
    # process_list = psutil.process_iter()
    # for process in process_list:
    #     print(process)
    #     try:
    #         process_name = process.name()
    #         if process_name == "notepad.exe":
    #             print("Notepad is running!")
    #     except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
    #         pass
