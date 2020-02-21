import requests, json, datetime, re
from datetime import datetime
from pprint import pprint

time_to_seconds = {"H": 60*60, "M": 60, "S": 1}

def get_duration(url, id):
    try:
        url = url.replace("{id}", id)
        response = requests.get(url)
        data = json.loads(response.text)
        if len(data['items']) == 0: return -2
        duration = data['items'][0]['contentDetails']['duration']
        time_values = re.findall("\d*[H|M|S]", duration)
        return sum([time_to_seconds[time[-1]] * int(time[:len(time) - 1]) for time in time_values])
    except:
        return -1


def check_videos(time, videos):
    time = get_time(time)
    for video in videos[1:]:
        if str(time) in video:
            return False
    return True

def get_time(time):
    time = re.sub("\..*", "", time).replace("Z", "")
    return datetime.strptime(time, "%Y-%m-%dT%H:%M:%S").timestamp()
