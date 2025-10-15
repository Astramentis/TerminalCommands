# Pitch Demo README: '200 Digits of Pi'
This README is for investors to examine my code as a software developer. The explanation of the application itself is in the [Application README](https://github.com/Astramentis/TerminalCommands/blob/demo-branch/src/README.md).

While this is a showcase branch, it is functionally complete and I have used the master branch to learn to memorize numbers. It serves a dual function as a realistic reflection of how I architect my work. 

Relevant code is in the src folder, specifically [application.py](https://github.com/Astramentis/TerminalCommands/blob/demo-branch/src/application.py) and [application_logic.py](https://github.com/Astramentis/TerminalCommands/blob/demo-branch/src/application_logic.py) and the math database file using SQLite. 

![image](https://github.com/user-attachments/assets/ad54bd66-4920-43a7-a888-49e4363dd398)

# How to Run this Application:

If you intend to run the code directly on your machine (with python and pip installed):


download the repository -> pip install -r requirements.txt after navigating to the repository folder -> run `python3 application.py` without issue

If you try to run it in a virtual environment on windows you will run into a tkinter bug that has remained unpatched for the past decade.

# FAQ

**What madness inspired this?**

Due to various personal goals and economic hazards, I prepared to return to college for a math degree (Masters in Stats). I hadn't studied math seriously for years and I decided to dedicate time to relearn the fundamentals, starting with a fundamental of fundamentals - mental arithmetic. 

Human brains process language differently than numbers in memory, and no application exists (as far as I'm aware) that provides the practice required to learn memorization of numbers. While I enjoyed much of the mental math courses, making this application was a way to force me to 'chew my vegetables' and force myself to memorize numbers and test theories of 'gamification' in software.

**Why is this unfinished?**

For my purposes, this was a version with cTkinter for my personal use and a proof of concept for how I intended to architect math education software. Python and the CTK framework are insufficient for further development. I am currently moving forward with C and [raylib](https://www.raylib.com) for additional development. raylib is more suited to my case and comes with features like hot reloading, direct threadsafe tools, debug/analytics, and having native cross compilation - including mobile development. 

**What is remaining?**

There are many intended features that were left unfinished due to rewriting with raylib. They are listed in the [application README](https://github.com/Astramentis/TerminalCommands/blob/demo-branch/src/README.md).