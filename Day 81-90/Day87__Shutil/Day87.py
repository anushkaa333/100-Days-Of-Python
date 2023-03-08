import shutil



#*********** I] Copy - works with files

shutil.copy("file.docx", "file2.txt")
shutil.copy("file2.txt", "file1.txt")



#********* II] copytree - works with folders/directories

shutil.copytree("folder", "folder1")
shutil.copytree("folder1", "folder2")



#********* III] removetree == rmtree => works with folders/directories

shutil.rmtree("folder2")



#********* IV] remove using os as shutil cant delete file, it will delete folders only

import os

os.remove("file1.txt")





#******* V] Move 

shutil.move("file2.txt", "folder1/mannual_folder")
shutil.move("folder1/Assignment1C.pdf", "Assignment1C.pdf")




