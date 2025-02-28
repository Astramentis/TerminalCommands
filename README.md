# Interviewer ReadMe: '200 Digits of Pi'

This ReadMe is to provide prospective interviewers context relevant to the project & author, pre-empt questions, and setup instructions for running my application '200 Digits of Pi'.

As a showcase branch this program is intentionally incomplete, and is meant to function as a replacement for 'take home projects' that I will no longer entertain due to AI code reviews and 'asynchronous' interviews.

While this is a small program, it is a good springboard for discussion of programming and a reflection of how I aim architect my work, in addition to teaching a party trick you can learn in approximately 2 hours.  

If you intend to run the code directly on your machine or a virtual machine and are not using the venv module you can download the repository as usual, pip install requirements after navigating to the repository folder, and run application.py without issue, but I recommend skimming the actual [application ReadMe](https://github.com/Astramentis/TerminalCommands/blob/Interview-Publish/src/README.md) for an overview of why this application exists and who it's for.

![image](https://github.com/user-attachments/assets/ad54bd66-4920-43a7-a888-49e4363dd398)

However, if you would like to use a virtual environment or see how I handle an esoteric bug, read on.

# Tkinter and the Virtual Environment

Context for those unfamiliar with Tkinter:

Tkinter is a python wrapper on top of a string-based command wrapper to draw pixels on a screen using the TK/TCL C libraries (both by John Ousterhout et al. - you might know for his [popular presentation on software architecture](https://www.youtube.com/watch?v=bmSAYlu0NcY&t=288s ) ) as a 'cross platform' solution to developing basic applications. It is multiple layers of abstractions that make a mess of both responsibility for resolving issues, produces applications that are just shy of black boxes to the people that make them, and does not provide useful features for fast iteration or guarantees of reliability.

For reasons beyond my understanding, it is highly recommended and entire books are written on developing applications with it.


----


*The key words 'MUST', 'REQUIRED', 'SHOULD', 'SHOULD NOT', 'RECOMMEND', 'MAY', and 'OPTIONAL' in this section are to be interpreted as described in [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119)*

There is a bug where virtual environments are unable to render python's Tkinter application because the virtual environment does not correctly path to the TK/TCL C libraries that are included with python, pip-freeze does not include these libraries, and the Tkinter library does not include the TK/TCL packages (a grand total of 5.75 MB). This makes me wonder how testing Tkinter is automated, if at all. 

From 9 years, 11 months ago: [Trying to use Tkinter throws Tcl error "Can't find a usable init.tcl"](https://stackoverflow.com/questions/29320039/trying-to-use-tkinter-throws-tcl-error-cant-find-a-usable-init-tcl) as a sequel to the [issue raised  14 years ago](https://github.com/pypa/virtualenv/issues/56). 

The issue persists into the modern day...

Below I provide two solutions that must be implemented by the end user if they are intending to use a virtual environment. You must first generate the virtual env since the venv folder and it's contents are required to modify activate.bat:

![image](https://github.com/user-attachments/assets/b5fc0504-c407-4480-af82-e1567905d499)

#### Relevant terminal venv commands:

Generate virtual env
```
python -m venv venv
```
Install required packages (if you decide to install requirements manually at the latest version you will need to roll back playsound to version 1.2.2 [due to a bug]([url](https://github.com/TaylorSMarks/playsound/issues/160))
```
pip install -r requirements.txt
```
Activate venv
```
venv\Scripts\activate
```
Launch application (you should get an error here if you have not edited the activate.bat on windows), but will otherwise launch after implementing a solution 1 or 2
```
python -B src\application.py
```

### Solution 1 (simple) - update the path to the libraries included in the fixvenv folder: 

After your initial venv setup copy and paste the code below into venv's activate.bat file:

```
rem Set TCL and TK paths relative to the repo

set TCL_LIBRARY=%~dp0tcl\tcl8.6
set TK_LIBRARY=%~dp0tcl\tk8.6
set TKPATH=%~dp0tcl\tk8.6
```

![image](https://github.com/user-attachments/assets/13f3fdac-4baa-4854-b08f-95159f0c22a2)

This solution updates the TCL/TK library paths to the packages I included in the fixvenv folder before the activate.bat ends.

With the requirements installed AND paths updated you should be able to run application.py within a virtual environment without issue, but your mileage may vary. 

### Solution 2 (less simple) - run a python script outside the venv (readandrun.py) to find the library paths on your machine and paste those paths into the generated activate.bat: 

Navigate in the src folder > fixvenv > open readandrun.py to copy and paste your local TCL/TK path into your venv activate.bat file as [explained in this thread](https://stackoverflow.com/a/50628771). 

_Note: do not put paths in quotes, you will get an error_

---

# FAQ

**Why is this unfinished?**

I have no intention of continuing with Tkinter and now that I've done a rough draft intend to rewrite this in raylib as it's more suited to my needs and comes with features I actually need. If someone insist on a take-home project I can implement a feature of their request into this program and see the size of a problem they expect me to solve.

**Unit tests?**

Unit tests were not appropriate for solving issues that extended beyond basic logic, and would have been a poor use of time. Considering this was an exploratory project, full regression and compatibility testing was the priority. 

**How long did this take?**

This was started in Nov 2024 up to Feb 02 2025, as an after-work project. Approximately 40 working hours, most of it resolving bugs with imported code or working around constraints native to Tkinter. The application logic itself is simple by it's very nature, hence my desire to rewrite it in a more apporpriate framework. SQLite as an alternative to I/O, and the WAL enabled is more than enought to store and access state/session data.

