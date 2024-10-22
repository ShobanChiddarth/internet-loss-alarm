# internet-loss-alarm

Python script that beeps a few times if your internet goes down. Delay between each check is customisable.

### Steps to get it running
1. Install the required modules
   `pip install -r requirements.txt`
2. Simply run the python file: `python main.py`

### To make it run at startup (Windows only)
1. Open file explorer (Win+E)
2. Type `shell:startup` at the address bar
3. Copy the file [internet-loss-alarm.bat](./internet-loss-alarm.bat)
4. Paste it in the `shell:startup` folder you opened
5. Now copy the full path to the file [main.py](./main.py)
6. Open the file `internet-loss-alarm.bat` which is inside the `shell:startup` folder using a text editor
7. Replace `.\path\to\internet-loss-alarm\main.py` with the path you copied.
8. Make sure you use quotation marks if the path has spaces.

Now whenever you restart your computer, the script runs (just not in the background). You can stop it with CTRL+C.

### Credits
[beep.mp3](./beep.mp3) was downloaded from [pixabay](https://pixabay.com/sound-effects/search/beeps/). You can replace it with whatever sound you like.