import os

def arrange_file(files,ext):
    files_ext = [file for file in files if file.endswith(ext)]
    print(files_ext)

    if not(os.path.exists("images")):
        os.mkdir("images")
        
    for i,file in enumerate(files_ext):
        os.rename(file,f"images/photo-{i+1}{ext}")
        


if __name__ == "__main__":
    files = os.listdir()
    arrange_file(files,".jpg")
         
                 
