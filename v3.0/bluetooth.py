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

NOTE: This code is experimental and may not work. 

"""

# IMPORT LIBRARIES
import serial
import v3
 
# SETTING UP THE SERIAL PORT
ser = serial.Serial('/dev/rfcomm0')
print("Bluetooth Ready")
print("Use the Project: EnAble App To Control Sensitivity")
while True:
    x = ser.read(1)
    if x == b'1':
        v3.start(50)
    elif x == b'2':
        v3.start(62)
    elif x == b'3':
        v3.start(76)
    elif x == b'4':
        v3.start(89)
    elif x == b'5':
        v3.start(100)
    elif x == b'6':
        v3.start(115)
    elif x == b'7':
        v3.start(128)
    elif x == b'8':
        v3.start(141)
    elif x == b'9':
        v3.start(150)



"""
Project: EnAble© is under Copyright 2023 by Jeron Osguthorpe. Though the project is open source, taking all 
credit for works is not. Though you are allowed to use the code for your own projects, you are not allowed to
take credit for the code. If you would like help with the code, please contact Jeron Osguthorpe. Contact 
information can be found on the Project: EnAble© website and GitHub repository/organization.
"""