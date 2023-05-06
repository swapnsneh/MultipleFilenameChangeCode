import os

def renameFiles():
    folder = r"C:\Users\mahaj\Desktop\test"

    for count, filename in enumerate(os.listdir(folder)):
        dst = f"{count+1}.pdf"
        src= f"{folder}/{filename}"
        name= f"{folder}/{dst}"

        os.rename(src, name)

renameFiles()
