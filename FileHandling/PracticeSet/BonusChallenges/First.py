from pathlib import Path
import shutil

file_path = Path(__file__).parent / "task2.txt"

print(file_path)
try:
    with open(file_path,"r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File not here")
    
# uppercase = shutil.copy("task2.txt","uppercase.txt")
with open(file_path,"w") as f:
    uppercase1 = f.write(content.upper())
