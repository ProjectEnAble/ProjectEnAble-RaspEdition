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

NOTE: Purpose of this file: This file is used to test the bluetooth connection with the official Android app. This file is not part of the main program.

"""
# IN ORDER TO TEST BLUETOOTH, DOWNLOAD THE OFFICIAL PROJECT: ENABLE ANDROID APP

import serial
ser = ser.Serial('/dev/rfcomm0')
while True:
    x = ser.read(1)
    print(x)


"""
Project: EnAble© is under Copyright 2023 by Jeron Osguthorpe. Though the project is open source, taking all 
credit for works is not. Though you are allowed to use the code for your own projects, you are not allowed to
take credit for the code. If you would like help with the code, please contact Jeron Osguthorpe. Contact 
information can be found on the Project: EnAble© website and GitHub repository/organization.
"""