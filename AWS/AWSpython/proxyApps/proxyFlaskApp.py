from flask import Flask, redirect, url_for, request, render_template
from pyCode.pageSketchBook import drawHTML
# from dominate.tags import *
# from dominate import document


app = Flask(__name__)

myArtist =  drawHTML()
htmlDir = "/home/proxyApps/appData/ytcData"
workingDir = "/home/proxyApps/appData/ytcData"
    
#################################################Dominate Examples#################################

def drawDominateExample():
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
        p('This is a paragraph generated using the Dominate library.')
        ul(li('Item 1'), li('Item 2'), li('Item 3'))

    # print(doc.render(pretty=True))
    return doc.render(pretty=True)

@app.route('/')
def hello():
        return 'Hello from Flask on EC2!'


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

#################################################Youtube Methods###################################

@app.route('/<username>/youtube/')
def alt_load_youtube(username):
    print("Start: alt_load_youtube")
    return load_youtube(username)
    # return redirect(url_for('load_youtube', name=username))

@app.route('/<name>/youtube')
def load_youtube(name):
    print("Start: load_youtube")
    youtubeCommentPageHtml = myArtist.drawYoutubeDownloader(name)
    return youtubeCommentPageHtml
    #return 'welcome %s' % name
    
@app.route('/<name>/youtube/view_comments', methods=['GET'])
def load_youtube_comments(name):
    print("Start: load_youtube_comments")
    # user = request.form['nm']
    # userPW = request.form['pw']
    #this file should only: pass the request down to python, or send HTML with data back to user.
    youtubeCommentPageHtml = myArtist.selectPainting(name, request)
    
    return youtubeCommentPageHtml
    #return 'welcome %s' % name

@app.route('/<name>/youtube/search_comments_author', methods=['GET'])
def search_comments_author(name):
    print("Start: search_comments_author")
    youtubeCommentPageHtml = myArtist.selectPainting(name, request)
    return youtubeCommentPageHtml
    pass

@app.route('/<name>/youtube/search_comments_text', methods=['GET'])
def search_comments_text(name):
    print("Start: search_comments_text")
    youtubeCommentPageHtml = myArtist.selectPainting(name, request)
    return youtubeCommentPageHtml
    pass

@app.route('/<name>/youtube/search_comments_cid', methods=['GET'])
def search_comments_cid(name):
    print("Start: search_comments_cid")
    youtubeCommentPageHtml = myArtist.selectPainting(name, request)
    return youtubeCommentPageHtml
    pass

@app.route('/<name>/youtube/sort_most_comments', methods=['GET'])
def sort_most_comments(name):
    print("Start: sort_most_comments")
    youtubeCommentPageHtml = myArtist.selectPainting(name, request)
    return youtubeCommentPageHtml
    pass

@app.route('/<name>/youtube/sort_author_alpha', methods=['GET'])
def sort_author_alpha(name):
    print("Start: sort_author_alpha")
    youtubeCommentPageHtml = myArtist.selectPainting(name, request)
    return youtubeCommentPageHtml
    pass

@app.route('/<name>/youtube/sort_most_common_words', methods=['GET'])
def sort_most_common_words(name):
    print("Start: sort_most_common_words")
    youtubeCommentPageHtml = myArtist.selectPainting(name, request)
    return youtubeCommentPageHtml
    pass

###########################################Login Methods##########################################

@app.route('/<name>/pwtool')
def load_pwtool(name):
    pwToolPageHtml = myArtist.drawPWTool()
    return pwToolPageHtml
    #return 'welcome %s' % name


@app.route('/login_Test', methods=['POST', 'GET'])
def login_Test():
    userList = ["proxy", "irf", "gio", "njefferson"]
    print(f"login: request: {request}")
    print(f"login: request.method: {request.method}")
    print(f"login: request.form: {request.form}")
    user = ""
    if request.method == 'POST':
        user = request.form['usrnm']
        userPW = request.form['usrpw']

        print(f"login: user: {user}")
        print(f"login: userPW: {userPW}")
        return redirect(url_for('load_youtube', name=user))
    elif request.method == 'GET':
        return render_template('login2_template.html')

    return '404 error username not authorized %s' % user

@app.route('/login', methods=['POST', 'GET'])
def login():
    userList = ["proxy", "irf", "gio"]
    if request.method == 'POST':
        user = request.form['nm']
        userPW = request.form['pw']
        
        print(f"login: user: {user}")
        print(f"login: userPW: {userPW}")
        
        # if(user in userList):
        if (user):
            MATCH = {
                'youtube': 'load_youtube',
                'pwtool': 'load_pwtool'
            }
            
            try:
                MATCH[userPW]
                return redirect(url_for(MATCH[userPW], name=user))
            except KeyError:
                raise NotImplementedError(f"Running {userPW} page not implemented.")
        else:
            return redirect(url_for('success', name=user))
    else:#GET request
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))

###################################################################################################

if __name__ == '__main__':
    app.run(debug=True)