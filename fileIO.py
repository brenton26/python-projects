

import os

fName='afile.txt'

fPath='/Users/Zumbi/Desktop/TestFolder/'

abpath=os.path.join(fPath,fName)
print(abpath)

this=os.listdir(path='/Users/Zumbi/Desktop/TestFolder')

print("\nAll files in this folder: \n")

for i in this:
    print(i)


print("\nFull file path of all files in this folder that end with .txt: \n")

for i in this:
    if i.endswith('.txt'):
        file_path=os.path.join(fPath,i)
        print(file_path)

print("\nThese files were last edited:\n")

for i in this:
    if i.endswith('.txt'):
        file_path=os.path.join(fPath,i)
        file_time=os.path.getmtime(file_path)
        print("{} was last edited {}.".format(i,file_time))
