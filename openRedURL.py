import praw
import os
import re
import webbrowser

username = input("Enter username: ")
pw = input("Enter password: ")
try:
    reddit = praw.Reddit(client_id = 'hKqx7wfOpWihcg',
                         client_secret = 'Gwy82Ak2PJbEiyRBFB27J63WzNI',
                         username = username,
                         password = pw,
                         user_agent = 'garlic'  )
except:
    print("Password Incorrect")

sub = input("Name the subreddit: ")

subreddit = reddit.subreddit(sub)
top_python = subreddit.top('year', limit=20)

allComments = []
for submissions in top_python:
     comForest = submissions.comments
     for com in comForest:
         allComments.append(com.body)
         replyforest = com.replies
         for gettingRep in replyforest:
             allComments.append(gettingRep.body)

"""
for s in allComments:
    print(s)"""
#function to find url in string

def Find(string):
    url = re.findall(r'(https?://[^\s]+)', string) 
    return url 


urlList = []

    
for x in allComments:
    if x.find('reddit.com') == -1:
        urlList.append(Find(x))
    
    
urlList = list(filter(None,urlList))

for x in urlList:
    print(x)



incog = input("Incognito? y/n: ")

if incog == 'y':
    Path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito"
else:
    Path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

controller = webbrowser.get(Path)

controller.open('https://www.google.com')
for x in range(len(urlList)):
    controller.open_new_tab(urlList[x][0])
    