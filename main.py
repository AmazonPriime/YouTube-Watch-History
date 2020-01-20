import os, argparse, time, sys, re
from selectolax.parser import HTMLParser

start = time.time()

# setup argument parser
parser = argparse.ArgumentParser()
parser.add_argument("filename", help = "Name of the html file containing YT history. (including .html extension)", type = str)
args = parser.parse_args()


# check if the file is in the correct format
if not args.filename.endswith(".html"):
    print("Incorrect filename, must be a html file.")
    exit(1)


# check if the file exists in the current working directory (cwd)
cwd = os.getcwd()
filepath = os.path.join(cwd, args.filename)
if not os.path.exists(filepath):
    print("File does not exist, make sure the file is in same directory as the Python 'main.py' and that you provide the correct filename.")
    exit(1)


# read the file and store in a string called 'data'
try:
    with open(filepath) as file:
        data = file.read()
except:
    print("Error reading the file, make sure the file is in the same directory as the Python 'main.py' and that you provied the correct filename.")
    exit(1)


#
selector = "div.content-cell.mdl-typography--body-1"
for node in HTMLParser(data).css(selector):
    if node.text(strip = True) != "":
        re_result = re.findall("<a.*?>(.*?)<\/a>", node.html)
        re_url = re.findall("href=\"(https:\/\/www\.youtube\.com\/watch.*?)\">", node.html)
        if len(re_result) == 2 and len(re_url) == 1:
            print("Title: %s" % re_result[0])
            print("Author: %s" % re_result[1])
            print("URL: %s" % re_url[0])
            if node.last_child:
                print("Date: %s\n" % node.last_child.html)

print("Time taken: {}s".format(time.time() - start))
