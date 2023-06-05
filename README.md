# Lost Ark Auto Fishing Tool
Automation tool to automate the fishing lifeskill. 

This tool does **not** interfere with any game code or network packets. 

Instead, the tool takes region-bounded screenshots and perform image recognition on them to determine what actions to take.

Your mileage may vary.

# User Setup
**This tool has only been tested on Lost Ark with the following setup: 1080p + Fullscreen + 80% HUD size.**

Before starting the exectuable, make sure to configure the keybinding on your fishing tool in the `config.ini`. Default key is `f`.

If you wish for the program to end once your life energy is out, fill in the energy field in the configuration file. Otherwise, leave it as `0`. This will require the user to keep an
an active eye on the program. This parameter is here if the user wants to utilize the casting minigame and/or to use the throw bait skill.

## Usage
To run the program, simply use the `fishing.exe`. To quit the tool, press the `=` key or `CTRL + C` in the terminal. 

# Development Setup
Pre-requisite is to have Python 3.11.0+ installed using the installation [here](https://www.python.org/downloads/).

Once completed, run the following commands in the terminal below:
1. Setup a python virtual environment by running : ```python -m venv venv```
2. Activate the virtual environment: ```./venv/Scripts/activate```
3. Install python dependencies: ```pip3 install -r requirements.txt```

You can now run the tool by running: ```python fishing.py```

If you choose to run based on the executable, use the `fishing.exe` file, which will immediately start up the program.

However, any changes made outside of the configuration file will require the user to regenerate the `.exe` by running:
```pyinstaller --onefile fishing.py```. Once generated, move the one file from the `dist` directory to the root.

To quit the tool, press the `=` key or `CTRL + C` in the terminal.

# WARNING
This is not endorsed by Smilegate or AGS. Usage of this tool isn't defined by Smilegate or AGS. No personal identifiable data is saved.
