"""
Welcome to Project:EnAble v3.0
Project:EnAble is under Copyright © 2023 Jeron Osguthorpe

Project: EnAble
Author: Jeron Osguthorpe
Version: v3.1.0 - Beta

BASIC INFORMATION REGARDING PROJECT: ENABLE
Git Hub Organization Link: https://github.com/projectenable
Git Hub Repository Link: https://github.com/projectenable/Project-Enable
Website: https://enable.codingtricksyt.com
Email: enable@codingtricksyt.com
YouTube: https://youtube.com/codingtricks
Twitter: https://twitter.com/proj_enable
License, Code of Conduct, and Contributing: https://github.com/projectenable/Project-Enable
Donate: https://enable.codingtricksyt.com/

ChatGPT Involment: ChatGPT was used to help create this part of the project. Among ChatGPT, 
Copilot was also used to help create this part of the project. ChatGPT is a project by OpenAI. 
Copilot is a project by OpenAI and GitHub. Both projects are under the MIT License.

"""
# IMPORT LIBRARIES
import tkinter as tk
from PIL import Image # ImageTk NOTE: This is not working for some reason
import subprocess
import v3
import serial


# SETTING UP THE GUI
root = tk.Tk()
root.title("Project: EnAble - Raspberry Pi Edition")
# root.iconbitmap("v3.0/v3.0 Rasp Edition/images/icon.ico") NOTE: This is not working for some reason
root.geometry("500x500")

"""
# SETTING UP THE BACKGROUND IMAGE
NOTE: This is not working for some reason
background_image = Image.open("v3.0/v3.0 Rasp Edition/images/background.png")
background_image = background_image.resize((500, 500), Image.LANCZOS)
background_image = ImageTk.PhotoImage(background_image)

background_label = tk.Label(root, image=background_image)
background_label.grid(row=0, column=0, columnspan=2, rowspan=2, sticky="nsew")
""" 

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# SETTING UP THE BUTTONS
cancel = False
def run_script1():
    while cancel == False:
        v3.start(50)

def run_script2():
    while cancel == False:
        v3.start(100)

def run_script3():
    while cancel == False:
        v3.start(150)

def run_script4():
    v3.cancel_all()

def canceltrue():
    print("cancel = True")
    cancel = True

button1 = tk.Button(root, text="Low Sensitivity", command=run_script1, font=("Montserrat", 12), bg="#C0C0C0", padx=20, pady=10, width=15, height=2)
button1.grid(row=0, column=0, padx=25, pady=10)

button2 = tk.Button(root, text="Medium Sensitivity", command=run_script2, font=("Montserrat", 12), bg="#C0C0C0", padx=20, pady=10, width=15, height=2)
button2.grid(row=0, column=1, padx=25, pady=10)

button3 = tk.Button(root, text="High Sensitivity", command=run_script3, font=("Montserrat", 12), bg="#C0C0C0", padx=20, pady=10, width=15, height=2)
button3.grid(row=1, column=0, padx=25, pady=10)

button4 = tk.Button(root, text="CANCEL ALL", command=lambda: [run_script4(), canceltrue()], font=("Montserrat", 12), bg="#C0C0C0", padx=20, pady=10, width=15, height=2)
button4.grid(row=1, column=1, padx=25, pady=10)

# END OF PROGRAM
root.mainloop()

"""
Project: EnAble© is under Copyright 2023 by Jeron Osguthorpe. Though the project is open source, taking all 
credit for works is not. Though you are allowed to use the code for your own projects, you are not allowed to
take credit for the code. If you would like help with the code, please contact Jeron Osguthorpe. Contact 
information can be found on the Project: EnAble© website and GitHub repository/organization.
"""