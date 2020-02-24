## YouTube Watch History

Returns information about your watch history in more readable/manageable CSV file from the JSON provided in Google Takeout. <br>
I've included a simple Python script to generate a pie chart showing which channel you watch the most.

#### Google Takeout:
* Go to [Takeout](https://takeout.google.com/) and login to your Google/YouTube account.
* Deselect all and select YouTube from the list.
* Make sure that ```history``` is selected in YouTube content options are ticked and then click ```Next step``` at the bottom of the page.
  * Before clicking to the next step, click on ```Multiple formats``` and change the history format from ```HTML``` to ```JSON```.
* Select ```Export once``` and then click ```Create export``` then wait for the email to come with the download.

#### Usage:
* Download ```main.py``` and move your ```watch-history.json``` to the same directory as it.
  * If you've run the program again and want to update your ```output.csv``` make sure it's in same directory also and use the optional argument ```-c <filename>```.
* Install the modules from ```requirements.txt```: ```pip3 install -r requirements.txt```.
* Update the ```example_config.py```.
  * Obtain your API key from [Google Developers](https://console.developers.google.com/) for ```YouTube Data API v3```.
  * Update the config file with it and then rename the config file to ```config.py```.
* Run the code with, filename is a required argument ```python3 main.py [-h] -f <filename> [-c <already scraped data filename>]```.
* Once the program is finished there will be an file called ```output.csv``` containing the scraped data.
