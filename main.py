import os, argparse
from bs4 import BeautifulSoup


# setup argument parser
parser = argparse.ArgumentParser()
parser.add_argument("name", help = "Name of the html file containing YT history.", type = str)
args = parser.parse_args()


# check if the file is in the correct format
if not args.name.endswith(".html"):
    print("Incorrect filename, must be a html file.")
    exit(1)


# check if the file exists in the current working directory (cwd)
cwd = os.getcwd()
filepath = os.join(cwd, args.name)
if not os.path.exists(filepath):
    print("File does not exist, make sure the file is in same directory as the Python 'main.py' and that you provide the correct filename.")
    exit(1)


#
