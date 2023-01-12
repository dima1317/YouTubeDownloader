
# importing the module 
import sys
from pathlib import Path
from pytube import YouTube

if len(sys.argv) == 1:
  # ask for the link from user
  link = input('Input YouTube address: ')
  pathfile = input('Save to: ')

elif len(sys.argv) == 3:
  # link from argv
  link = sys.argv[1]
  pathfile = sys.argv[2]
else:
  print('Wrong parameters: should be command only or command <URL> <SaveTo>')
  exit()
try: 
    # which was imported in the beginning 
    yt = YouTube(link) 
except: 
    print("Connection Error") #to handle exception 

#Showing details
print("Title: ", yt.title)
print("Length of video: ", yt.length)

#Starting download
print("Downloading...")
yt.streams.get_highest_resolution().download(pathfile)
print("Download completed!!")
 