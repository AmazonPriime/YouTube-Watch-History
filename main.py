import os, argparse, re, csv, json
from datetime import datetime
from functions import get_duration, check_videos, get_time
from config import url

# setup argument parser
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", help = "Name of the html file containing YT history. (including .html extension)", type = str, required = True)
parser.add_argument("-c", "--current", help = "Name of the the file already generated by the program (avoids scraping data already obtaiend)", type = str)
args = parser.parse_args()


# check if the file is in the correct format
if not args.filename.endswith(".json"):
    print("Incorrect filename, must be a html file.")
    exit(1)


# check if the file exists in the current working directory (cwd)
cwd = os.getcwd()
filepath = os.path.join(cwd, args.filename)
if not os.path.exists(filepath):
    print("Your 'YT-history' file does not exist, make sure the file is in same directory as the Python 'main.py' and that you provide the correct filename.")
    exit(1)


# check the current arg and create a filepath for it
c_filepath = os.path.join(cwd, args.current) if args.current else None
if not os.path.exists(c_filepath):
    print("Your 'current' file does not exist, make sure the file is in same directory as the Python 'main.py' and that you provide the correct filename.")
    exit(1)


# read the file and store in a string called 'data'
try:
    with open(filepath) as file:
        data = file.read()
except:
    print("Error reading the file, make sure the file is in the same directory as the Python 'main.py' and that you provied the correct filename.")
    exit(1)


# read in the data from the already existing file
videos = [["Title", "Author", "Author URL", "Timestamp", "Duration", "ID"]]
if c_filepath:
    with open(c_filepath) as file:
        reader = csv.DictReader(file)
        for row in reader:
            videos.append([row['Title'], row['Author'], row['Author URL'], row['Timestamp'], row['Duration'], row['ID']])


# grabbing the title, author, url and timestamp from the JSON about the videos available on YouTube storing them in a 2D array
data = json.loads(data)
for video in data:
    if check_videos(video['time'], videos):
        if "titleUrl" in video and "subtitles" in video:
            author = video['subtitles'][0]['name']
            author_url = video['subtitles'][0]['url']
            title = video['title'].replace("Watched ", "", 1)
            id = re.findall("watch\?v=(.*)", video['titleUrl'])[0]
            time = get_time(video['time'])
            duration = get_duration(url, id)
            if duration == -1:
                print("Daily API call limit has been reached, this will reset at midnight of your local time.")
                print("Saving the data that has been scraped already.")
                break
            videos.append([title, author, author_url, time, duration, id])
            print("+ " + title)



# store the 2D array containing videos into a CSV file called 'output.csv'
c_filepath = c_filepath if c_filepath else "output.csv"
with open(c_filepath, "w") as file:
    writer = csv.writer(file)
    writer.writerows(videos)
print("Data has been saved to the file: " + c_filepath)
