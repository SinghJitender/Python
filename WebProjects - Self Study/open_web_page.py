# Open file in web browser
#import webbrowser
#webbrowser.open('http://nseindia.com')

#read webpage
import urllib.request
page = urllib.request.urlopen('https://www.google.com/')
print(page.read())