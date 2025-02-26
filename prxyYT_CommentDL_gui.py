#Youtube comment downloader gui
#Purpose: Accept a youtube link, download and display comments
#Usage: python prxyYT_CommentDL_gui.py

import os   #used to handle files
import json #used for data storage/handling
import operator #Used for sorts
import youtube_comment_downloader #used to get youtube comment data
from itertools import islice #used to extract youtube comment data
from tkinter import *
from tkinter.scrolledtext import ScrolledText


class DownloadSession(object):
    def __init__(self):
        self.entry_for_link = None
        self.loadNumComments = None
        self.label_for_comments = None
        self.comment_dict = {}
        
root = Tk()
root.geometry("1200x680")
root.title('Youtube comment downloader gui')
mainFrame = Frame(root, bd=20, bg='#8c92ac', width=1000)
mainFrame.pack(anchor=N, fill=BOTH, expand=True, side=LEFT )#fill=BOTH,
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
    settingsMenu.add_command(label='Prefrences', command=showPrefMenu )#showPrefMenu()
    
def showPrefMenu():
    print("Start showPrefMenu")
    prefWindow = Toplevel(mainFrame)
    prefWindow.geometry("200x300")
    prefWindow.title('Youtube comment downloader gui: Preferences')
    
    currXLabel = Label(prefWindow, text='current X value: '+str(root.winfo_width()))
    currXLabel.pack()
    
    currYLabel = Label(prefWindow, text='current Y value: '+str(root.winfo_height()))
    currYLabel.pack()
    
    s1 = Scale( prefWindow,  
           from_ = 1200, to = 1700,
           resolution=100,
           orient = HORIZONTAL)    
    
    s2 = Scale( prefWindow,
           from_ = 600, to = 900,
           resolution=100,
           orient = VERTICAL)  
           
    prefSaveButton = Button(prefWindow, text='Save & Apply')
    prefSaveButton['command'] = lambda: applyPrefs(s1.get(), s2.get())
    s1.pack(side=TOP)
    s2.pack(side=TOP)
    prefSaveButton.pack(side=BOTTOM, anchor=S)
    
def applyPrefs(s1, s2):
    root.geometry( str(s1) + "x" + str(s2))
    
  
    
############################################################
def dataFrameSetup():
    dataFrame = Frame(mainFrame,  relief="raised", bd=20, bg='#000453', padx=15, pady=15)
    dataFrame.pack(anchor=W, fill=Y, side=LEFT)
    
    #Link entry fields
    dataFrame1 = Frame(dataFrame, bd=5, bg='#8c92ac', padx=15, pady=5)
    dataFrame1.pack(anchor=CENTER, fill=X, side=TOP, pady=20)
    
    linkLabel = Label(dataFrame1, text='Enter a YouTube link in the box to download comments')
    linkLabel.pack()
    
    linkEntry = Entry(dataFrame1, width=50, justify=CENTER)
    linkEntry.pack()
    myDownloadSession.entry_for_link = linkEntry
    
    comments2Load = Scale( dataFrame1,
           from_ = 10, to = 1000,
           resolution=100,
           length=250,
           label= "# of comments 2 load", 
           orient = HORIZONTAL)
    myDownloadSession.loadNumComments = comments2Load
    comments2Load.pack()
    
    linkButton = Button(dataFrame1, text='Get Comments')
    linkButton.pack()
    linkButton['command'] = lambda: getYTComments()
    
    #Search author field
    dataFrame2 = Frame(dataFrame, bd=5, bg='#8c92ac', padx=15, pady=5)
    dataFrame2.pack(anchor=CENTER, fill=X, side=TOP, pady=20)
    
    unLabel = Label(dataFrame2, text='Search YouTube comment author')
    unLabel.pack()
    
    unEntry = Entry(dataFrame2, width=50, justify=CENTER)
    unEntry.pack()
    myDownloadSession.entry_for_un_search = unEntry
    
    unButton1 = Button(dataFrame2, text='Search username')
    unButton1.pack()
    unButton1['command'] = lambda: searchYTComments("author")
    
    #Search comment field
    dataFrame3 = Frame(dataFrame, bd=5, bg='#8c92ac', padx=15, pady=5)
    dataFrame3.pack(anchor=CENTER, fill=X, side=TOP, pady=20) #, side=BOTTOM, anchor=N, 
    
    commentLabel = Label(dataFrame3, text='Search YouTube comment text')
    commentLabel.pack()
    
    commentEntry = Entry(dataFrame3, width=50, justify=CENTER)
    commentEntry.pack()
    myDownloadSession.entry_for_comment_search = commentEntry
    
    commentButton1 = Button(dataFrame3, text='Search comment')
    commentButton1.pack()
    commentButton1['command'] = lambda: searchYTComments("text")
    
    #Data Analysis buttons
    dataFrame4 = Frame(dataFrame, bd=5, bg='#8c92ac', padx=15, pady=5)
    dataFrame4.pack(anchor=CENTER, fill=X, side=TOP, pady=20)
    
    calcNumAuthorButton = Button(dataFrame4, text='Count # of author comments')
    calcNumAuthorButton.pack()
    calcNumAuthorButton['command'] = lambda: countAuthors()
    
    calcNumCommentButton = Button(dataFrame4, text='Count and sort by # of comments')
    calcNumCommentButton.pack()
    calcNumCommentButton['command'] = lambda: countAuthors("count")
    
    
    
    calcWordCountButton = Button(dataFrame4, text='Count # of word occurences')
    calcWordCountButton.pack()
    calcWordCountButton['command'] = lambda: countWords()
    

    
############################################################
def displayFrameSetup():
    displayFrame = Frame(mainFrame, relief="raised", bd=20, bg='#740000', padx=25, pady=10)
    displayFrame.pack(anchor=W, fill=BOTH, side=LEFT, expand=True) # anchor=W, side=LEFT)
    
    # commentText = Text(displayFrame, height=15, width=120, bg='#dcffb3', font =("Courier", 14))
    # commentText.pack(fill=BOTH, side=LEFT, expand=True)
    # commentText.insert(END, 'GeeksforGeeks\nBEST WEBSITE\n')
    # myDownloadSession.label_for_comments = commentText
    
    
    scrollCommentText = ScrolledText(displayFrame, height=15, bg='#dcffb3', font =("Courier", 14)) #, width=120, 
    scrollCommentText.pack(fill=BOTH, side=LEFT, expand=True) #
    
    scrollCommentText.insert(END, 'GeeksforGeeks\nBEST WEBSITE\n')
    myDownloadSession.label_for_comments = scrollCommentText

############################################################
def getYTComments():
    myCommentFilePath = "C:/Users/geneb/Downloads/tempYTComments.json"
    myCommentText = ""
    youtube_url = "https://www.youtube.com/watch?v=c52IzePdOag" #
    youtube_url = myDownloadSession.entry_for_link.get()
    
    #youtube-comment-downloader --url myCommentLink --output myCommentFilePath
    myYoutubeCommentDownloader = youtube_comment_downloader.YoutubeCommentDownloader()
    SORT_BY_POPULAR = 0
    SORT_BY_RECENT = 1
    myCommentText = myYoutubeCommentDownloader.get_comments_from_url(youtube_url, sort_by=SORT_BY_RECENT, language=None, sleep=.1)
    
    # with open(myCommentFilePath, 'r') as file:
        # myCommentText = file.read()
    myDownloadSession.label_for_comments.delete("1.0", 'end')#"1.0", "end"
    
    #print("getYTComments: len(myCommentText): ", len(json.dumps(myCommentText) ))
    count=1
    print("getYTComments: ", myDownloadSession.loadNumComments.get())
    for comment in islice(myCommentText, myDownloadSession.loadNumComments.get()):
        #print(comment)
        #print("Entry: ", count)
        myDownloadSession.label_for_comments.insert(END, "Entry: "+str(count)+"\n" )
        #myDownloadSession.label_for_comments.insert(END, str(comment)+"\n")
        
        myDownloadSession.comment_dict.update({count:comment})
        #print("getYTComments: myDownloadSession.comment_dict[count]: ", myDownloadSession.comment_dict[count])
        for item in comment:
            myDownloadSession.label_for_comments.insert(END, str(item)+": ")
            myDownloadSession.label_for_comments.insert(END, str(comment[item])+"\n")
        #y = json.loads(comment)

        # the result is a Python dictionary:
        #print(comment["cid"])
        myDownloadSession.label_for_comments.insert(END,"\n\n")
        count += 1
    #Cleanup
    #os.remove(myCommentText)

def searchYTComments(option):
    print("Start searchYTComments")
    print("searchYTComments: option: ", option)
    
    myDownloadSession.label_for_comments.delete("1.0", 'end')#"1.0", "end"
    
    #print("getYTComments: len(myCommentText): ", len(json.dumps(myCommentText) ))
    count=1
    for comment in myDownloadSession.comment_dict:
        #myDownloadSession.label_for_comments.insert(END, "Entry: "+str(count)+"\n" )
        #print("searchYTComments: DownloadSession.comment_dict[comment]: ", myDownloadSession.comment_dict[comment])
        #print("searchYTComments: DownloadSession.comment_dict[comment][\"author\"]: ", myDownloadSession.comment_dict[comment]["author"])
        #print("Entry: ", count)
        #myDownloadSession.label_for_comments.insert(END, str(comment)+"\n")
        
        if "author" in option:
            userSearch = myDownloadSession.entry_for_un_search.get()
        elif "text" in option:
            userSearch = myDownloadSession.entry_for_comment_search.get()
        
        if userSearch in myDownloadSession.comment_dict[comment][option]:
            myDownloadSession.label_for_comments.insert(END, "Entry: "+str(count)+"\n" )
            count += 1
            #myDownloadSession.label_for_comments.insert(END, str(item)+": ")
            #myDownloadSession.label_for_comments.insert(END, str(myDownloadSession.comment_dict[comment])+"\n")
            for item in myDownloadSession.comment_dict[comment]:
                myDownloadSession.label_for_comments.insert(END, str(item)+": ")
                myDownloadSession.label_for_comments.insert(END, str(myDownloadSession.comment_dict[comment][item])+"\n")
            myDownloadSession.label_for_comments.insert(END,"\n\n")
        
        #y = json.loads(comment)

        # the result is a Python dictionary:
        #print(myDownloadSession.comment_dict[comment]["cid"])
        #myDownloadSession.label_for_comments.insert(END,"\n\n")
        #count += 1
def countAuthors(option="author"):
    print("Start countAuthors")
    authorList={}
    myDownloadSession.label_for_comments.delete("1.0", 'end')#"1.0", "end"
    
    #print("countAuthors: len(myCommentText): ", len(json.dumps(myCommentText) ))
    count=1
    for comment in myDownloadSession.comment_dict:
        #myDownloadSession.label_for_comments.insert(END, "Entry: "+str(count)+"\n" )
        #print("countAuthors: comment: ", comment)
        #print("countAuthors: comment[\"author\"]: ", myDownloadSession.comment_dict[comment]["author"])
        thisAuthor = myDownloadSession.comment_dict[comment]["author"]
        #print("countAuthors: thisAuthor: ",thisAuthor)
        
        if thisAuthor in authorList:
            #print("countAuthors: authorList[]: ",authorList[thisAuthor])
            authorList.update({thisAuthor:authorList[thisAuthor]+1})
        else:
            authorList.update({thisAuthor:1})
            #print("countAuthors: authorList[]: ",authorList[thisAuthor])
    
    #display list
    #for author in authorList:
    #    myDownloadSession.label_for_comments.insert(END, str(author)+" appears: ")
    #    myDownloadSession.label_for_comments.insert(END, str(authorList[author])+"\n")
    
    #sort list then display
    #sort on value
    if "count" in option:
        #print("countAuthors: Sort list by author comment count: ")
        myDownloadSession.label_for_comments.insert(END, "Sort list by author comment count:: \n")
        #x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
        sorted_x = sorted(authorList.items(), key=operator.itemgetter(1), reverse=True)
    
        for x in sorted_x:
            #print( x[0], x[1])
            myDownloadSession.label_for_comments.insert(END, str(x[0])+" appears: ")
            myDownloadSession.label_for_comments.insert(END, str(x[1])+"\n")
    
    #sort on key
    if "author" in option:
        #print("countAuthors: Sort list by author: ")
        myDownloadSession.label_for_comments.insert(END, "Sort list by author:: \n")
        #x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
        sorted_x = sorted(authorList.items(), key=operator.itemgetter(0))

        for x in sorted_x:
            #print( x[0], x[1])
            myDownloadSession.label_for_comments.insert(END, str(x[0])+" appears: ")
            myDownloadSession.label_for_comments.insert(END, str(x[1])+"\n")
    

def countWords():
    print("Start coundWords")


main()
mainloop()
