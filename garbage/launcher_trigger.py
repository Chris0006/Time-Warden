import win32gui
import win32process
import psutil
import os
import signal


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
                print("Launched program: ", current_program, program_name)
                
                pid = current_program

                try:
                    #TODO: time
                    import time
                    time.sleep(10)
                    # os.kill(pid, 0) # check if the process exists
                    os.kill(pid, signal.SIGTERM) # send SIGTERM signal to kill the process
                    print(f"Process with PID {pid} has been terminated.")
                except OSError as e:
                    print(f"Process with PID {pid} cannot be terminated:", e)