# Pitch Demo ReadMe: '200 Digits of Pi'
This ReadMe is for investors to understand me (Wesley) as a software developer. The explanation of the application itself is in the [Application ReadMe](https://github.com/Astramentis/TerminalCommands/blob/Interview-Publish/src/README.md), where you can read more about how number memorization works, and the features I intended to add to this before moving to Raylib and C/C++.

While this is a showcase program, it is functionally complete and I have used it to learn to memorize numbers. It serves a dual function as a springboard for discussion of programming, debugging, a realistic reflection of how I architect my work. 

Code is in the src folder; the relevant code files are [application.py](https://github.com/Astramentis/TerminalCommands/blob/Interview-Publish/src/application.py) and [application_logic.py](https://github.com/Astramentis/TerminalCommands/blob/Interview-Publish/src/application_logic.py) and the math database file using SQLite. 

Note: The setup file is for remaking the database, reference for the schema. It is not needed but is included for discussion purposes.

---

# FAQ's

**What madness inspired this?**

Due to various personal goals and looming economic hazards I prepared to return to college for a math degree (Masters in Stats - it's always useful and I already enjoy it). I hadn't studied math seriously for years and I decided to dedicate time to relearn the fundamentals, starting with a fundamental of fundamentals - mental arithmetic. Human brains find language less fungible than numbers as they exist in our human memory, and no application exists (as far as I'm aware) that provides the practice required to learn memorization of numbers. While I enjoyed much of the mental math courses, making this application was a way to force me to 'chew my vegetables' and force myself to memorize numbers and test theories of 'gamification' in software.

**Unit tests?**

Unit tests were used for one function (not present in this branch) - determining sound/number matching - due to having specific corner cases that needed to be robustly tested with every iteration of the function. Considering this was an exploratory project, full regression and compatibility testing was the priority, but I can pull the full project to showcase what my unit tests look like (of course I use an LLM to write my unit tests, it's a waste of time not to). 

**How long did this take?**

This was started in Nov 2024 up to Feb 02 2025, as an after-work project. Approximately 35 working hours, most of it resolving bugs with imported code or working around constraints native to Tkinter like having to set up manual centering of text. The application logic itself is (mostly) simple by it's very nature, hence my desire to rewrite it in a more appropriate framework. SQLite is my alternative to I/O, and the WAL enabled with the engine and database loaded into memory is more than enough to store and access state/session data. The primary bottleneck is the layers of abstraction slowing the application to unacceptable levels.

**You planned on multiplayer? What does multiplayer look like?**

Battle royale; you and <n> number of players drop into a lobby and are given numbers to memorize and purely visual puzzles (think tic tac toe or tiles) to solve or audio to read aloud, numbers grow progressively larger until 1 player remains. 

**Why is this unfinished?**

I have a mostly complete (for my purposes) version with cTkinter for my personal use, but intend to rewrite the project in C and [Raylib](https://www.raylib.com). Raylib is more suited to my needs and comes with features I actually need like hot-reloads and being threadsafe (if I program it that way) and being fast. This branch works as a stand in for the  interviewer "take-home project", or would prefer a project to discuss as a 'drill down' to see why I worked on this and what the limitations are, or what caused me to change course from using python and this library (it doesn't respect operator precedence). 


**Questions for us?**

I'm someone that needs to be learning something, what am I expected to learn working at your company or with your team? What skills should I expect to gain? 
What is the size of problem I'm expected to solve, what am I expected to escalate?

---

If you intend to run the code directly on your machine (with python and pip installed) you can download the repository -> pip install requirements after navigating to the repository folder -> run `python3 application.py` without issue. 

Prior to this, I recommend skimming the actual [application ReadMe](https://github.com/Astramentis/TerminalCommands/blob/Interview-Publish/src/README.md)

![image](https://github.com/user-attachments/assets/ad54bd66-4920-43a7-a888-49e4363dd398)


# Python, Tkinter and Virtual Environment. 

Context for those unfamiliar with Tkinter:

Tkinter is a python wrapper on top of a string-based command wrapper to draw pixels on a screen using the TK/TCL C libraries (both by John Ousterhout et al. - you might know for his [popular presentation on software architecture](https://www.youtube.com/watch?v=bmSAYlu0NcY&t=288s ) ) as a 'cross platform' solution to developing basic applications. It is multiple layers of abstractions that make a mess of both responsibility for resolving issues, produces applications that are just shy of black boxes to the people that make them, and does not provide useful features for fast iteration or guarantees of reliability. It breaks operator precidence, ignores native features of the python language, is filled with hard-coded pauses, is quite ugly, and is breaking other software. 

For reasons beyond my understanding, it is highly recommended and entire books are written on developing applications with it. If you, for whatever reason, feel compelled to use this application library [this playlist of videos with source code](https://www.youtube.com/playlist?list=PLpMixYKO4EXflJFPhTvZOVAbs7lBdEBSa) is one of the only good resources for learning the library.

---


