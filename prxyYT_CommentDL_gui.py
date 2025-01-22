#Youtube comment downloader gui
#Purpose: Accept a youtube link, download and display comments
#Usage: python prxyYT_CommentDL_gui.py

import youtube_comment_downloader
import os
import json
from itertools import islice
from tkinter import *

class DownloadSession(object):
    def __init__(self):
        self.entry_for_link = None
        self.label_for_comments = None
        
root = Tk()
root.geometry("1200x600")
mainFrame = Frame(root, bd=20, bg="gray", width=1000)
mainFrame.grid()
myDownloadSession = DownloadSession()


def main():
    print("Start Main")
    
    
    fileMenuSetup()
    dataFrameSetup()
    displayFrameSetup()
###########################################################
def fileMenuSetup():
    print("Start fileMenuSetup")
    #create menu variable and bind to root
    pMenu = Menu(root)
    root.config(menu=pMenu)
    
    #Setup File menu
    filemenu = Menu(pMenu)
    pMenu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='New', command = None)
    filemenu.add_command(label='Open...', command = None)
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=root.quit)
    
    #Setup help menu
    helpmenu = Menu(pMenu)
    pMenu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='About', command = None)
    
    #Setup settings menu
    settingsMenu = Menu(pMenu)
    pMenu.add_cascade(label='Settings', menu=settingsMenu)
    settingsMenu.add_command(label='Prefrences', command = None)
############################################################
def dataFrameSetup():
    dataFrame = Frame(mainFrame, bd=5, bg="yellow", padx=15, pady=5)
    dataFrame.grid()
    
    label = Label(dataFrame, text='Enter a YouTube link in the box to download comments')
    label.grid()
    
    entry = Entry(dataFrame, width=30)
    entry.grid()
    myDownloadSession.entry_for_link = entry
    
    button1 = Button(dataFrame, text='Get Comments')
    button1.grid()
    button1['command'] = lambda: getYTComments()

    
############################################################
def displayFrameSetup():
    displayFrame = Frame(mainFrame, bd=1, bg="red")
    displayFrame.grid()
    
    commentText = Text(displayFrame, height=15, width=120)
    commentText.grid()
    commentText.insert(END, 'GeeksforGeeks\nBEST WEBSITE\n')
    myDownloadSession.label_for_comments = commentText

############################################################
def getYTComments():
    myCommentFilePath = "C:/Users/geneb/Downloads/tempYTComments.json"
    myCommentText = ""
    youtube_url = myDownloadSession.entry_for_link.get()
    
    #youtube-comment-downloader --url myCommentLink --output myCommentFilePath
    myYoutubeCommentDownloader = youtube_comment_downloader.YoutubeCommentDownloader()
    SORT_BY_POPULAR = 0
    SORT_BY_RECENT = 1
    myCommentText = myYoutubeCommentDownloader.get_comments_from_url(youtube_url, sort_by=SORT_BY_RECENT, language=None, sleep=.1)
    
    # with open(myCommentFilePath, 'r') as file:
        # myCommentText = file.read()
    for comment in islice(myCommentText, 10):
        #print(comment)
        myDownloadSession.label_for_comments.insert(END, str(comment)+"\n\n")
    #Cleanup
    #os.remove(myCommentText)



main()
mainloop()
