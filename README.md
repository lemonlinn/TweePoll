# TweePoll
A flask based localhost website that visualizes real-time twitter sentiment filtered by a user inputted hashtag.

# How to use

I am assuming that your computer already has python 3 and pip. If you don't, the latest python can be found [HERE.](https://www.python.org/downloads/)

This website also is most compatible with the Google Chrome browser, so having Chrome is recommended.

### Step 0: Download

Fork this repository or download it onto your computer.

### Step 1: Dependencies

To make sure your computer has the correct libraries downloaded, run the following code in your terminal/command prompt while in the TweePoll directory:

```
$ pip install -r requirements.txt
```

Feel free to use a virtualenv if you'd like.

You also will need to create a file called config.py using any simple text editor. This will contain your twitter API tokens and secret keys. Use the following template:

```
ckey="your ckey"
csecret="your csecret"
atoken="your atoken"
asecret="your asecret"
```

If you do not already have access to the twitter API, you can apply for it [HERE.](https://developer.twitter.com/en/products/twitter-api)

### Step 2: Run on localhost

To run the website locally, run the following code in your terminal/command prompt while in the TweePoll directory:

```
$ py TweePoll_Server_V2.py
```

Without closing the terminal, go to your Chrome browser. Go to [THIS LINK](http://127.0.0.1:5000/) or type 'http://127.0.0.1:5000/' into your address bar. 

### Step 3: Use website

Now you can have fun typing in a keyword, hashtag, or topic and watching the live data visualizations update real time as people tweet about it to presidential nominees Donald Trump and Joe Biden! When you're done, exit the terminal and tab in the browser. 

# Work In Progress
I'm using this project to build my web development skills, as well as my understanding of server/client communication. This is my first time coding in node.js and javascript. How exciting! At any time, I might add in a new feature. Watch, star, or check in later to see what else I might end up throwing in. If I get around to it, I may also add this project as a page on my portfolio website.

## Possible Next Steps:
1. Pause/Play button on the twitter stream
2. Allow user to reset the page, so they can try multiple inputs in one setting
3. Word cloud of common words or hashtags in tweets (word clouds aren't great in the way of data visualization, but they are fun!)
4. Scrolling feed of tweets as they occur
5. Option to download .csv of tweets (text, username, time posted, NRC classification, etc.)
6. Leaflet of USA with lat/lon twitter data mapped on
7. A heatmap of some kind
8. Add a methodology/explanation section at the bottom
9. Add a way to 'jump' the viewer down the webpage so all data visualizations are perfectly framed in the browser
