# https://latisresearch.umn.edu/python-virtual-environments-in-windows#:~:text=To%20see%20a%20list%20of,location%20of%20your%20virtual%20environments.


# from os import system

# names = ["Robert", "Svaboda", "John", "Krishna"]

# for name in names:
#     system(f"say the name {name}")


#**** OR


import win32com.client


names = ["Robert", "Svaboda", "John", "Krishna"]

speaker = win32com.client.Dispatch("SAPI.SpVoice")
for name in names:
    speaker.Speak(f"say the name {name}")


# py -m pip install pywin32








# PS H:\> myenv/Scripts/Activate.ps1
# (myenv) PS H:\> py -m pip install pywin32
# Collecting pywin32
#   Downloading pywin32-305-cp311-cp311-win_amd64.whl (12.1 MB)
#      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.1/12.1 MB 4.8 MB/s eta 0:00:00
# Installing collected packages: pywin32
# Successfully installed pywin32-305
# [notice] A new release of pip available: 22.3 -> 23.0.1
# [notice] To update, run: python.exe -m pip install --upgrade pip
# (myenv) PS H:\> pip install --upgrade pip
# Requirement already satisfied: pip in h:\myenv\lib\site-packages (22.3)
# Collecting pip
#   Using cached pip-23.0.1-py3-none-any.whl (2.1 MB)
# ERROR: To modify pip, please run the following command:
# H:\myenv\Scripts\python.exe -m pip install --upgrade pip

# [notice] A new release of pip available: 22.3 -> 23.0.1
# [notice] To update, run: python.exe -m pip install --upgrade pip
# (myenv) PS H:\> H:\myenv\Scripts\python.exe -m pip install --upgrade pip
# Requirement already satisfied: pip in h:\myenv\lib\site-packages (22.3)
# Collecting pip
#   Using cached pip-23.0.1-py3-none-any.whl (2.1 MB)
# Installing collected packages: pip
#   Attempting uninstall: pip
#     Found existing installation: pip 22.3
#     Uninstalling pip-22.3:
#       Successfully uninstalled pip-22.3
# Successfully installed pip-23.0.1





# (myenv) PS H:\> cd "H:\100 Days of Python\Day 81-90"   
# (myenv) PS H:\100 Days of Python\Day 81-90> python Day88.py