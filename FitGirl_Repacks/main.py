import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

def pwd():
    print(f"Current directory is: {os.getcwd()}")
    print()

pwd()

destination = Path(os.getenv("TARGET_FOLDER")) / os.getenv("GAME_NAME") / "installer/"
print(f"Desired installation folder location: {destination}")
#print(f"Files in directory '{directory} are: {os.listdir(directory)}'")
if destination.exists():
    print(f"Desired folder already exists. \n Changing to: '{destination}'")
    os.chdir(destination)
    pwd()
else:
    print(f"Creating the new folder")
    os.makedirs(destination)
    os.chdir(destination)
    pwd()


