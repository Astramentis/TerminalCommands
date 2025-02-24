import tkinter
root = tkinter.Tk()   
print('\n')
print(root.tk.exprstring('$tcl_library'))   
print(root.tk.exprstring('$tk_library'))
print('paste the file paths according to the requirements ReadMe')

#follow the instructions outlined here https://stackoverflow.com/a/50628771


# or paste the following to use the relative path to the TCL packaged with the repostiory 

'''
rem set TCL/TK paths relative to the repo already in the repository

set TCL_LIBRARY=%~dp0tcl\tcl8.6
set TK_LIBRARY=%~dp0tcl\tk8.6
set TKPATH=%~dp0tcl\tk8.6
'''