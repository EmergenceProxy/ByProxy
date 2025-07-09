#Hold all the classes that draw different pages with dominate module
import os
from dominate.tags import *
from dominate import document
from dominate.util import text

import sys

# adding Folder_2 to the system path
sys.path.insert(0, '/home/proxyApps/pyCode')
print(f"-----------------os path: {os.getcwd()}")
from prxyYT_CommentDL_Web import DownloadSession

class drawHTML:
    
##############################-Class Objects-##########################################
    myDownloadSession = DownloadSession()
    videoData = {
                "1": {
                    "cid": "UgxvmVYzQ_0gYQGBhcZ4AaABAg",
                    "text": "The white have done nothing but steal and Kill whoever did not believe in their will it is a fact in history. Take Puerto Rico as a perfect example the difference is we are not being killed outright now days.  But we are being starved and striped of our riches by the wait it has been happening forever. Eventhoe we fight and die and have died for this country in every war.",
                    "time": "46 seconds ago",
                    "author": "@pereztattoo",
                    "channel": "UCv5s3fPwp_hwJ4tBkFl5g-g",
                    "votes": "0",
                    "replies": "",
                    "photo": "https://yt3.ggpht.com/ytc/AIdro_k_J4FHEowgLxQwzHA-o1ZKRBeAY3dLK7SBuFQhgOk=s88-c-k-c0x00ffffff-no-rj",
                    "heart": "false",
                    "reply": "false",
                    "time_parsed": "2025-05-21 08:12:57"
                },
                "2": {
                    "cid": "Ugwe6LjCcIWEMPjaz5N4AaABAg",
                    "text": "White boy said white people smarter look like to me black guy took his ass to history class\ud83e\udd23\ud83e\udd23\ud83e\udd23",
                    "time": "1 minute ago",
                    "author": "@ImHim5252",
                    "channel": "UCSmVZWYkm5kxrxqWhqFEpUg",
                    "votes": "0",
                    "replies": "",
                    "photo": "https://yt3.ggpht.com/uup4avLjkeKoPr9XnIpYoT1Y2AAm4L1QYzpN9u2Ob6kFVW4KMqGUP3Id4Hd15RYcupTvz9pTuas=s88-c-k-c0x00ffffff-no-rj",
                    "heart": "false",
                    "reply": "false",
                    "time_parsed": "2025-05-21 08:12:43"
                },
                "3": {
                    "cid": "UgwQEFmzqenOrPvdfKZ4AaABAg",
                    "text": "1:08:23 I can\u2019t watch this anymore. This white guy doesn\u2019t know shit",
                    "time": "1 minute ago",
                    "author": "@marcusjohnson9243",
                    "channel": "UC5mtcn1JD5IYH9FH6XW__tg",
                    "votes": "0",
                    "replies": "",
                    "photo": "https://yt3.ggpht.com/ytc/AIdro_kHm0gcr_suppS7eDR0dIZIObkz4lymEZWKSZYdAr8doQ=s88-c-k-c0x00ffffff-no-rj",
                    "heart": "false",
                    "reply": "false",
                    "time_parsed": "2025-05-21 08:12:43"
                }
    }
    videoData2 = {
                "1": {
                    "cid": "UgxvmVYzQ_0gYQGBhcZ4AaABAg",
                    "text": "The white have done nothing but steal a.",
                    "time": "46 seconds ago",
                    "author": "@pereztattoo"
                }
    }
    
##############################-Helper Functions-##########################################
    # @staticmethod
    def remove_surrogates(self, text):
        encoded_bytes = text.encode('utf-16', errors='replace')
                             # text.encode('utf-16', 'surrogateescape', errors='replace')
        # print(f"remove_surrogates: {encoded_bytes}\n")
        encoded_bytes = encoded_bytes.decode('utf-8', 'replace')
        # print(f"remove_surrogates: {encoded_bytes}\n")
        return encoded_bytes
    
##############################-HTML pages to draw-##########################################
    def getStyle(self):
        return """
                * {
                  box-sizing: border-box;
                }
                body {
                  //background-color: #8f9492;
                  background-color: #679436;
                  background-color:#ccc;
                  font-family: sans-serif;
                  font-size: 24px;
                }
                input {
                    font-size: 20px;
                }
                table, th, td {
                  border: 1px solid black;
                }
                .text_input{
                    width: 50%;
                }
                .text_input_url{
                    width: 75%;
                }
                /* Create three unequal columns that floats next to each other */
                .column {
                  float: left;
                  padding: 10px;
                  //height: 100%;
                  //height: 550px;/* Should be removed. Only for demonstration */
                }

                .left, .right {
                  width: 25%;
                }

                .left{
                    //height: 100%;
                }
                .middle {
                    width: 50%;
                    //height: 100%;
                }

                /* Clear floats after the columns */
                .row:after {
                  content: "";
                  display: table;
                  clear: both;
                }

                /* Responsive layout - makes the three columns stack on top of each other instead of next to each other */
                /*
                @media screen and (max-width: 800px) {
                  .column {
                    width: 100%;
                  }
                }
                */
            """
        pass

    def drawDataEntryColumn(self, username, formDict=None):
        url_input_value = ""
        if formDict is not None:
            print("drawDataEntryColumn: pull form values") #Add user input data to page b4 transmit
            url_input_value = formDict["url_input"]
            un_search_value = formDict["un_search_input"]
            comment_search_value = formDict["comment_search_input"]
            cid_search_value = formDict["cid_search_input"]
            print(f"drawDataEntryColumn: url_input_value: {url_input_value}")
        else:
            print("drawDataEntryColumn: print basic form")
            print(f"drawDataEntryColumn: username: {username}")
            url_input_value = ""
            un_search_value = ""
            comment_search_value = ""
            cid_search_value = ""
            pass

        with div(cls="column", id="dataEntryColumn", style="background-color:#C0D6DF;") as dataEntryDiv:
            # Link entry fields
            with form(action=f"http://18.225.8.106:5000/{username}/youtube/view_comments", method="get",
                      name="url_input_form"):
                p('Enter a YouTube link in the box to download comments:')
                input_(type='text', name='url_input', cls="text_input_url", value=url_input_value, required=True)
                p('Number of comments to download:')
                input_(type='range', name='commentCount_range', min="100", max="5000", value="100", step="100",
                       oninput="this.form.commentCount_input.value=this.value")
                input_(type='number', name='commentCount_input', min="100", max="5000", value="100",
                       oninput="this.form.commentCount_range.value=this.value")
                input_(type='submit', value="Send", name="url_input_form")
                hr()
            # Search author field
            # with form(action=f"http://18.225.8.106:5000/{username}/youtube/search_comments_author", method="get",name="search_author_form"):
                p('Search YouTube comment author:')
                input_(type='text', name='un_search_input', value=un_search_value, cls="text_input")
                input_(type='submit', value="Send", formaction=f"http://18.225.8.106:5000/{username}/youtube/search_comments_author", method="get", name="search_author_form")
                hr()
            # Search comment field
            # with form(action=f"http://18.225.8.106:5000/{username}/youtube/search_comments_text", method="get", name="search_comment_form"):
                p('Search YouTube comment text:')
                input_(type='text', name='comment_search_input', value=comment_search_value, cls="text_input")
                input_(type='submit', value="Send", formaction=f"http://18.225.8.106:5000/{username}/youtube/search_comments_text", method="get", name="search_comment_form")
                hr()
            # Search cid field
            # with form(action=f"http://18.225.8.106:5000/{username}/youtube/search_comments_cid", method="get",name="search_cid_form"):
                p('Search base CID for threads:')
                input_(type='text', name='cid_search_input', value=cid_search_value, cls="text_input")
                input_(type='submit', value="Send", formaction=f"http://18.225.8.106:5000/{username}/youtube/search_comments_cid", method="get",name="search_cid_form")
                hr()
            # Data Analysis buttons
            # with form(action=f"http://18.225.8.106:5000/{username}/youtube/sort_comments", method="get", name="count_analysis_form"):
                p('Data Analysis buttons:')
                # button('Count and sort by # of comments', type="submit", onclick="alert(document.getElementById('unEntry').value)")
                input_(type="submit", value='Count and sort by # of comments',
                       formaction=f"http://18.225.8.106:5000/{username}/youtube/sort_most_comments", method="get",
                       name='comment_count_input')
                input_(type="submit", value='Count # of author comments',
                       formaction=f"http://18.225.8.106:5000/{username}/youtube/sort_author_alpha", method="get",
                       name='author_count_input')
                input_(type="submit", value='Count # of word occurences',
                       formaction=f"http://18.225.8.106:5000/{username}/youtube/sort_most_common_words", method="get",
                       name='word_count_input')

            if formDict is None:
                with p(id="page-BOT"):
                    a('Goto Page Top', href='#page-TOP')
                with p():
                    a('Goto Page Bottom', href='#page-BOT')
        return dataEntryDiv


    def drawDataDisplayColumn(self, showAllFields = False):
        # showAllFields = False
        setDivWidth = "width: 100%;"

        if showAllFields:
            setDivWidth = "width: 50%;"
        # dataDisplayColumnStyle = f"background-color:#DBE9EE; height: 100%; {setDivWidth}; overflow-x:auto;"
        dataDisplayColumnStyle = f"background-color:#DBE9EE; height: 100%; width: 100%; overflow-x:auto;"

        with div(cls="column", id="dataDisplayColumn", style=dataDisplayColumnStyle):  # cls="column middle"
            #
            p('Data Display:')
            with table(style="width: 20%;"):  # style="width: 50%;"
                with thead():
                    tableHeaderRow = tr()
                    if showAllFields:
                        # print(f"-----drawDataDisplayColumn: self.videoData {self.videoData}.")
                        # print(f"-----drawDataDisplayColumn: self.videoData[\"1\"] {self.videoData['1']}.")
                        for headerValue in self.videoData['1'].keys():  # add all fields
                            tableHeaderRow.add(td(headerValue))
                    else:
                        tableHeaderRow.add(td("Entry #"))
                        tableHeaderRow.add(td("Authors"))
                        tableHeaderRow.add(td("Entry Time"))
                        tableHeaderRow.add(td("Comment"))
                        tableHeaderRow.add(td("Comment ID"))
                    pass
                with tbody():
                    for entry in self.videoData:
                        tableDataRow = tr()
                        comment = self.videoData[entry]
                        # print(f"drawYoutubeDownloader_CommentData: entry: {entry}\n")
                        if showAllFields:
                            for headerValue in comment.keys():
                                # self.videoData["1"]
                                tempData = comment[headerValue]
                                if "text" in headerValue:
                                    tempData = comment[headerValue]
                                    # print("drawYoutubeDownloader_CommentData: text surrogate removal, pre: ",tempData)
                                    tempData = self.remove_surrogates(tempData)
                                    # print(f"drawYoutubeDownloader_CommentData: text surrogate removal, post: {tempData}\n")
                                tableDataRow.add(td(str(tempData)))
                        else:
                            tableDataRow.add(td(entry))
                            tableDataRow.add(td(comment["author"]))
                            tableDataRow.add(td(comment["time"]))

                            tempData = comment["text"]
                            # print("drawYoutubeDownloader_CommentData: text surrogate removal, pre: ",tempData)
                            tempData = self.remove_surrogates(tempData)
                            # print(f"drawYoutubeDownloader_CommentData: text surrogate removal, post: {tempData}\n")
                            tableDataRow.add(td(tempData))

                            tableDataRow.add(td(comment["cid"]))
                    pass
                with tfoot():
                    tableFooterRow = tr()
                    if showAllFields:
                        for headerValue in self.videoData["1"].keys():  # add all fields
                            tableFooterRow.add(td(headerValue))
                    else:
                        tableFooterRow.add(td("Entry #"))
                        tableFooterRow.add(td("Authors"))
                        tableFooterRow.add(td("Entry Time"))
                        tableFooterRow.add(td("Comment"))
                        tableFooterRow.add(td("Comment ID"))
                    pass

            with p(id="page-BOT"):
                a('Goto Page Top', href='#page-TOP')
            with p():
                a('Goto Page Bottom', href='#page-BOT')
        pass


    # @staticmethod
    def drawYoutubeDownloader(self, name):
            print("Start: drawYoutubeDownloader")
            doc = document(title='YT Comment DownLoader')
            # false = "False"

            with doc.head:
                link(rel='stylesheet', href='login2_style.css')
                script(type='text/javascript', src='script.js')
                style(self.getStyle())

            with doc:
                h1('Hello from Dominate!')
                p(text('This is a page generated using the Dominate library by Kino. '), a('>Kino Link<', href='https://github.com/Knio/dominate'))
                p('This page is created to interface as the YoutubeCommentDownloader web GUI.')

                with div(cls="row") as dataentryDiv:
                    with p(id="page-TOP"):
                        a('Goto Page Top', href='#page-TOP')
                    with p():
                        a('Goto Page Bottom', href='#page-BOT')

                    # data entry Column
                    # dataentryDiv +=
                    self.drawDataEntryColumn(username=name)

                    # data display Column
                    showAllFields = False
                    setDivWidth = "width: 100%;"

                    if showAllFields:
                        setDivWidth = "width: 50%;"
                    # dataDisplayColumnStyle = f"background-color:#DBE9EE; height: 100%; {setDivWidth}; overflow-x:auto;"
                    dataDisplayColumnStyle = f"background-color:#DBE9EE; height: 100%; width: 50%; overflow-x:auto;"

                    # with p(id="page-BOT"):
                    #     a('Goto Page Top', href='#page-TOP')
                    # with p():
                    #     a('Goto Page Bottom', href='#page-BOT')

            # print(doc)
            # print(doc.render(pretty=True))
            return doc.render(pretty=True)

    # @staticmethod
    def drawYoutubeDownloader_CommentData(self, username, formDict, showAllFields = False):
        print("Start: drawYoutubeDownloader_CommentData")
        doc = document(title='YT Comment DownLoader')

        with doc.head:
            link(rel='stylesheet', href='login2_style.css')
            script(type='text/javascript', src='script.js')
            style(self.getStyle())

        with doc:
            h1('Hello from Dominate!')
            p(text('This is a page generated using the Dominate library by Kino. '), a('>Kino Link<', href='https://github.com/Knio/dominate'))
            p('This page is created to interface as the YoutubeCommentDownloader web GUI.')

            with p(id="page-TOP"):
                a('Goto Page Top', href='#page-TOP')
            with p():
                a('Goto Page Bottom', href='#page-BOT')

            with div(cls="row"):
                #data entry Column
                self.drawDataEntryColumn(username, formDict)

                #data display Column
                self.drawDataDisplayColumn(showAllFields)

        # print(doc)
        # print(doc.render(pretty=True))
        return doc.render(pretty=True)



    # @staticmethod
    def drawPWTool(self):
        doc = document(title='My Dominate Example')

        with doc.head:
            link(rel='stylesheet', href='login2_style.css')
            script(type='text/javascript', src='script.js')
            style("""
                body {
                  background-color: #f0f0f0;
                  font-family: sans-serif;
                }
                """)

        with doc:
            h1('Hello from Dominate!')
            p(text('This is a page generated using the Dominate library by Kino. '), a('>Kino Link<', href='https://github.com/Knio/dominate'))
            ul(li('Item 1'), li('Item 2'), li('Item 3'))

        print(doc.render(pretty=True))
        return doc.render(pretty=True)#Hold all the classes that draw different pages with dominate module
    
##############################-HTML Selector-#####################################
    def draw_url_input_form(self, name, formDict):
        print("Start: draw_url_input_form")
        print(f"selectPainting: form: {formDict}")
        return self.drawYoutubeDownloader_CommentData(name, formDict)
        pass
    
    # def draw_search_author_form(self,  name, formDict):
    #     print("Start: draw_search_author_form")
    #     print(f"selectPainting: form: {form}")
    #     pass
    #
    # def draw_search_comment_form(self,  name, formDict):
    #     print("Start: draw_search_comment_form")
    #     print(f"selectPainting: form: {formDict}")
    #     pass
    #
    # def draw_search_cid_form(self,  name, formDict):
    #     print("Start: draw_search_cid_form")
    #     print(f"selectPainting: form: {formDict}")
    #     pass

    def draw_search_form(self,  name, formDict):
        print("Start: draw_search_form")
        print(f"selectPainting: form: {formDict}")
        return self.drawYoutubeDownloader_CommentData(name, formDict, showAllFields=False)
        pass
    
    def draw_count_analysis_form(self, name, formDict):
        print("Start: draw_count_analysis_form")
        print(f"selectPainting: form: {form}")
        return self.drawYoutubeDownloader_CommentData(name, formDict, showAllFields = True)
        pass
    
    def selectPainting(self, name, request):
        print(f"selectPainting: Start")
        # print(f"selectPainting: request.name: {request.name}")
        print(f"selectPainting: request.args: {request.args}")
        # request.args.get('operator')
        # print(f"selectPainting: request.form: {request.form}")
        print(f"selectPainting: request.args.get('url_input'): {request.args.get('url_input')}")
        formDict = {}

        # for headerValue in request.keys():#add all fields
        # tableHeaderRow.add(td(headerValue))
        for key, value in request.args.items():
            # params.append(f'{key}: {value}')
            print(f"selectPainting: {key}: {value}")
            formDict[key] = value

        global myDownloadSession
        myDownloadSession = DownloadSession(formDict)
        print(f"selectPainting: myDownloadSession: after")
        print(f"selectPainting: myDownloadSession: {myDownloadSession.loadNumComments}")
        if 'url_input_form' in request.args:
            print(f"selectPainting: found url_input_form:")
            # self.videoData = myDownloadSession.getYTComments()
            self.videoData = myDownloadSession.loadVideoComments(name) #Implement comment loading logic
            return self.draw_url_input_form(name, formDict)
        elif "search_author_form" in request.args:
            print(f"selectPainting: found search_author_form:")
            self.videoData = myDownloadSession.getYTComments()
            self.videoData = myDownloadSession.searchYTComments("author")
            # self.videoData = myDownloadSession.loadVideoComments() #Implement comment loading logic
            return self.draw_search_form(name, formDict)
            # return self.draw_search_author_form(formDict)
        elif "search_comment_form" in request.args:
            print(f"selectPainting: found search_comment_form:")
            self.videoData = myDownloadSession.getYTComments()
            self.videoData = myDownloadSession.searchYTComments("text")
            # self.videoData = myDownloadSession.loadVideoComments() #Implement comment loading logic
            return self.draw_search_form(name, formDict)
            # return self.draw_search_comment_form(formDict)
        elif "search_cid_form" in request.args:
            print(f"selectPainting: found search_cid_form:")
            self.videoData = myDownloadSession.getYTComments()
            self.videoData = myDownloadSession.searchYTComments("cid")
            # self.videoData = myDownloadSession.loadVideoComments() #Implement comment loading logic
            return self.draw_search_form(name, formDict)
            # return self.draw_search_cid_form(formDict)
        elif "comment_count_input" in request.args:
            print(f"selectPainting: found comment_count_input:")
            self.videoData = myDownloadSession.getYTComments()
            self.videoData = myDownloadSession.countAuthors("count")
            # self.videoData = myDownloadSession.loadVideoComments() #Implement comment loading logic
            # return self.draw_url_input_form(name, formDict)
            return self.draw_count_analysis_form(name, formDict)
        elif "author_count_input" in request.args:
            print(f"selectPainting: found author_count_input:")
            self.videoData = myDownloadSession.getYTComments()
            self.videoData = myDownloadSession.countAuthors("author")
            # self.videoData = myDownloadSession.loadVideoComments() #Implement comment loading logic
            # return self.draw_url_input_form(name, formDict)
            return self.draw_count_analysis_form(name, formDict)
        elif "word_count_input" in request.args:
            print(f"selectPainting: found author_count_input:")
            self.videoData = myDownloadSession.getYTComments()
            self.videoData = myDownloadSession.countWords("count")
            return self.draw_count_analysis_form(name, formDict)
        else:
            return self.drawYoutubeDownloader(name)


        # drawYoutubeDownloader(self, name)

        doc = h1("404")
        return doc
        pass