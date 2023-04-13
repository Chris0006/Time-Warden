import sys
import os
import subprocess
import shutil
import argparse

parser = argparse.ArgumentParser(description='Example script with persistency flag.')
parser.add_argument('--persistency', action='store_true', help='If specified TimeWarden will run on startup')

args = parser.parse_args()

if args.persistency:
    persistency = True
else:
    persistency = False


program_name = "TimeWarden.exe"

current_dir = os.getcwd()
command = f'pyinstaller --noconfirm --onefile --windowed --add-data "{current_dir}/sounds;sounds/" --add-data "{current_dir}/images;images" --icon "{current_dir}/images/program_icon.ico" "{current_dir}/main.py"'
result = subprocess.run(command, shell=True, capture_output=True, text=True)


# remove unncessesary folders
def folder_removal(folder_path):
    if os.path.exists(folder_path):
        try:
            # delete the folder and its contents recursively
            shutil.rmtree(folder_path)
            # print(f"{folder_path} and its contents have been removed successfully!")
        except OSError as e:
            pass
            # print(f"Error: {folder_path} - {e.strerror}")
    else:
        # print(f"{folder_path} does not exist.")
        pass

folder_removal(f'{current_dir}/__pycache__')
folder_removal(f'{current_dir}/build')
folder_removal(f'{current_dir}/garbage')
folder_removal(f'{current_dir}/images')
folder_removal(f'{current_dir}/sounds')

# remove unncessesary files
def file_removal(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

file_removal(f'{current_dir}/main.spec')
file_removal(f'{current_dir}/main.py')

# moves the program to the current working directory
source_path = f'{current_dir}/dist/main.exe'
shutil.copy(source_path, current_dir)
folder_removal(f'{current_dir}/dist')
os.rename(os.path.join(current_dir, 'main.exe'), os.path.join(current_dir, program_name)) # renames the program


def become_persistent(self):
    file_location = os.environ["appdata"] + f"\\{program_name}"
    if not os.path.exists(file_location):
        shutil.copyfile(sys.executable, file_location)
        subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v winexplorer /t REG_SZ /d "' + file_location + '"', shell=True)


if persistency == True:
    become_persistent()

file_removal(f'{current_dir}/setup.py')