#importing modules
import os 
import sys 
import time
import glob
  
#the path where the text files can be found
path = 'C:\\Python\\The-Tech-Academy-Basic-Python-Projects\\Directory'

"""
lists the files within the path.
this would allow you to see that there are 2 .txt files
one named Deku.txt and one named Trixie.txt
"""

dirs = os.listdir(path)
for file in dirs:
    print (file)

#this one will single out just the .txt files

os.chdir(path)
textFiles = glob.glob('*.txt')
print(textFiles)

#creating the absolute path to Deku.txt and Trixie.txt

fname1 = "Deku.txt"
fname2 = "Trixie.txt"

abPath1 = os.path.join(path, fname1)
print(abPath1)

abPath2 = os.path.join(path, fname2)
print(abPath2) 

#this will show the last time Deku.txt was changed and print the contents
#uses the absolute path that was created and assigned to abPath1

f=open(abPath1)
file_contents = f.read()
print (file_contents)
f.close()

modification_time = os.path.getmtime(abPath1) 
print("Last modification time:", modification_time) 
  
local_time = time.ctime(modification_time) 
print("Last modification time(Local time):", local_time) 

#this will show the last time Trixie.txt was changed and print the contents
#uses the absolute path that was created and assigned to abPath2

f=open(abPath2)
file_contents = f.read()
print (file_contents)
f.close()

modification_time = os.path.getmtime(abPath2) 
print("Last modification time:", modification_time) 
  
local_time = time.ctime(modification_time) 
print("Last modification time(Local time):", local_time) 
