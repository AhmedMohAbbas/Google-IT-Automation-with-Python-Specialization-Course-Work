import os
import datetime

# All these functions take paths as arguments, if you are going to use relative paths "Like down below", you have to open the terminal in the same directory

print(os.remove("RandomFiles1.TXT")) # To remove an existing file

print(os.rename("RandomFiles2.TXT", "gebrish.TXT")) # To change the name of a file

print(os.path.exists("RandomFiles1.TXT")) # To check if a file/folder (a Path) exists  

print(os.path.isfile("fafsda")) # checks if a path exists and that it is indeed a file and only a file, not a folder, directory or anything else

print(os.path.getsize("RandomFiles3.TXT")) # returns the size in Bytes

print(os.path.getmtime("RandomFiles3.TXT")) # returns the last modification time stamp (Unix time-stamp, the one from the 1970)
# to get it in a readable form:
tmstmp = os.path.getmtime("RandomFiles3.TXT") 
print(datetime.datetime.fromtimestamp(tmstmp))

print(os.path.abspath('PowerShellAliases.txt')) # get the full path of any file, anywhere on the machine

# You can use python's os module to manipulate directories using the same stile as Linux:-
print(os.getcwd()) # Same as pwd in linux
os.mkdir("some directory or path")
os.chdir("some path") # same as cd
os.rmdir("some directory or path") # same as remove, to remove an EMPTY directory
os.listdir("some directory or path") # returns a list of all the child items and sub-directories of the provided path

os.path.join("directory", "folder") # creates the path string between the 2 independent of the operating system. Basically, it automatically handels putting a / or  \
 