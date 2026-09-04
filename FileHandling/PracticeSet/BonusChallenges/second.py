import os
from pathlib import Path
# os.listdir()

file_handling = Path(__file__).parent / "demo.tmp"
# print(file_handling)
try:
    currentDic = os.getcwd()
    print(currentDic)
    # file_path = os.path.join(currentDic,'.tmp')
    os.remove(file_handling)
    print("File deleted successfully!")
except FileNotFoundError:
    print("File not here!")