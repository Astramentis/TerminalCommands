import customtkinter as ctk
import application_logic as app_l
import os
from playsound import playsound
from threading import Thread
###################### GLOBALS ########################### DO NOT TOUCH THESE #####################
chunk_id = 1 # should start at 3.1415 and increment up using the index# to find the next value
hint_active = False
###################### GLOBALS ########################### DO NOT TOUCH THESE #####################

ctk.FontManager.load_font("src/pix.ttf")
ctk.set_appearance_mode("dark")
ctk.set_widget_scaling(1.45)  #scales widget buttons and text size
root = ctk.CTk() 
root.title("TWO HUNDRED DIGITS OF PI")
pi_text = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303820'
root.geometry("840x555")
root.iconbitmap("src/images/untitled_design2.ico")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
#root.geometry('-1000-10') 
# ^^^^^^ move app position when started -- https://stackoverflow.com/questions/65256092/how-to-open-tkinter-gui-on-second-monitor-display-windows

#==============================================Grid Config======================================
new_font = ("m5x7",35) #To change font in tabs: https://github.com/TomSchimansky/CustomTkinter/discussions/709#discussioncomment-11354741
main_frame = ctk.CTkCanvas(root, width=400, height=400, bg="#2B2B2B", highlightthickness = 2)
main_frame.grid(row=0, column=0, padx=1, pady=1, sticky="nsew")
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_rowconfigure(2, weight=0)

view_area = ctk.CTkTextbox(main_frame, wrap="word", font = new_font, activate_scrollbars=False)
view_area.configure(bg_color= 'transparent',fg_color = 'transparent', text_color = "snow",pady = 0)
view_area.grid(row=0, column=0, padx=10, pady=(3, 3), sticky="nsew")
view_area.insert(1.0, pi_text, tags = None) 

bottom_frame = ctk.CTkFrame(main_frame, fg_color= 'transparent')
bottom_frame.grid(row=0, column=0, padx=2, pady=(5,2), sticky="sew", bg = None, border_color = None, fg_color = None)

bottom_frame.grid_columnconfigure(0, weight=1) #input field
bottom_frame.grid_columnconfigure(1, weight=0)
bottom_frame.grid_columnconfigure(2, weight=0)
#==============================================Option Menu======================================
def optionmenu_callback(choice):
    #TODO add conditionals here for a short one-shot mode 
    #TODO make one-shot mode  
    print("optionmenu dropdown clicked:", choice)

optionmenu_var = ctk.StringVar(value="⚙️")
optionmenu = ctk.CTkOptionMenu(bottom_frame, values=['1', '2'], 
                               width=15, height=35,
                               command=optionmenu_callback,
                               variable=optionmenu_var)
optionmenu.grid(row=0, column=4, padx=2, pady=2, sticky="e")
#==============================================Buttons/Inputs/Functions=========================

def submit(event=None): #TODO swap this button for a pop-up now that an input tracker works or use it for hint overrides
    input_text = input_field.get()
    view_area.insert('end', f"{input_text}\n")
    input_field.delete(0, 'end')

def reset(): 
    #TODO just reset state instead of destroy entire window, set-up new session
    root.destroy()
    os.startfile("src/application.py")
    #Keybinds as events: https://github.com/python/cpython/blob/3.8/Lib/tkinter/__init__.py CTRL + F 'event types', it's super scuffed
    #root.bind(("<Return>") ,lambda event:submit()) #don't need this yet but will come in handy later

def init():
    view_area.delete('1.0', 'end')
    global chunk_id 
    global hint_active 
    chunk_id = 1 
    hint_active = False
    #TODO - create new session for tracking

def audio_threaded(num):
    #this is trivial to expand for user designated audio later
    # - has to be threadsafe because ctinkter/tkinter already breaks execution order - refer to sleep late execution bug
    # - playsound might break on windows 11/ARM, I refuse to install windows 11 to find out
    def bad_sound():
        thread = Thread(playsound('src/sounds/bad_sound.wav'))
        thread.start()
    def good_sound():
        thread = Thread(target=playsound, args=('src/sounds/good_sound.wav',))
        thread.start()
    '''
    def user_sound():
        user_audio_filepath = None 
        thread = Thread(playsound(f"{user_audio_filepath}")) #fix parsing here if user audio is implemented
        thread.start()
    #if num == 2:
        #user_sound()
    '''
    if num == 0:
        bad_sound()
    if num == 1:
        good_sound()

def clear_hints():
        text = view_area.get("1.0", "end")
        index = text.find(" ")
        if index != -1:
            view_area.delete(f"1.0 + {index} chars", "end")

def input_tracker(*args):
    current_value = input_var.get()
    global chunk_id
    global hint_active
    print(current_value)
    if len(current_value) == 6:
        db_chunk = app_l.check_6(chunk_id) 
        if chunk_id == 1:
            view_area.delete('1.0', 'end') 
        if current_value != db_chunk:
            print('incorrect')
            audio_threaded(0)
            input_var.set(current_value[6:])
            input_field.icursor('end')
        elif current_value == db_chunk:
            #TODO - 
            clear_hints()
            view_area.insert('end', f"{current_value[:6]}")
            input_var.set(current_value[6:])
            input_field.icursor('end')
            chunk_id = chunk_id + 1
            hint_active = False #reset hint on successful input
            print('correct')
            audio_threaded(1)

def hint():
    #if you click a hint, the hint chunk should be set to the current chunk_id # so that all hints follow the same pattern as the chunk. 
    #TODO - add ability to override hint
    #TODO - add profiles with hint overrides
    global chunk_id 
    global hint_active
    mhint_minor, mhint_major = app_l.hint(chunk_id)
    print(mhint_minor, mhint_major)
    if hint_active == False:
        if chunk_id == 1:
            view_area.delete('1.0', 'end')
        view_area.insert('end', f" {mhint_minor}")
        hint_active = True
    elif hint_active == True:
        view_area.insert('end', f"\n{mhint_major}") 

input_var = ctk.StringVar() 
input_var.trace_add("write", input_tracker) #https://stackoverflow.com/questions/4140437/interactively-validating-entry-widget-content-in-tkinter scroll to Steven Rumbalski's trace answer
print(input_var)

input_field = ctk.CTkEntry(bottom_frame, font = new_font, validate = "key", validatecommand = None, textvariable=input_var,placeholder_text = "3.141", text_color= "white")
input_field.grid(row=0, column=0, padx=(2,0), pady=0, sticky="ew")

submit_button = ctk.CTkButton(bottom_frame, text="Retry", command=init, font = new_font,width=65)
submit_button.grid(row=0, column=1, padx=2, pady=2)

hint_button_text = "Hint?"
hint_button = ctk.CTkButton(bottom_frame, text=hint_button_text, command=hint, font = new_font,width=65)
hint_button.grid(row=0, column=2, padx=2, pady=2)

reset_button = ctk.CTkButton(bottom_frame, text="Restart", command=reset, font = new_font, text_color="#e32818",width=65)
reset_button.grid(row=0, column=3, padx=2, pady=2)

root.mainloop()
