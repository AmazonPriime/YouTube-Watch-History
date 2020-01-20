## YouTube Watch History

Returns information about your watch history in more readable/manageable CSV file from the HTML provided in Google Takeout.

#### Google Takeout:
* Go to [Takeout](https://takeout.google.com/) and login to your Google/YouTube account.
* Deselect all and select YouTube from the list.
* Make sure that ```history``` is selected in YouTube content options are ticked and then click ```Next step``` at the bottom of the page.
* Select ```Export once``` and then click ```Create export``` then wait for the email to come with the download.

#### Usage:
* Download ```main.py``` and move your ```watch-history.html``` to the same directory as it.
* Install the modules from ```requirements.txt```: ```pip3 install -r requirements.txt```.
  * Will install the [selectolax](https://github.com/rushter/selectolax) module used for parsing HTML.
* Run the code with, filename is a required argument ```python3 main.py [-h] <filename>```.
* Once the program is finished there will be an file called ```output.csv``` containing the scraped data.
