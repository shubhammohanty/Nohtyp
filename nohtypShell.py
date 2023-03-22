import datetime
import os
import platform

helpmessage = """
------------------------------------------------------INTRODUCTION------------------------------------------------------
HI everyone.
I am Shubham Mohanty and this is nohtyp, an esoteric langauge made by me which is inspired by python but not at all similar
to it.
Since it is an esoteric langauage, it is not intended for any productive or deployment purpose rather made for fun or for 
an artistic presentation.
Enjoy

------------------------------------------------------SYNTAX-------------------------------------------------------------
You must have noticed the name of this langauge which is 'nohtyp' , its the opposite of python right ? The logo is also 
the mirror image of original python's logo. 
The syntax also follows the same pattern which means it is just the opposite synatx of python. Let me show you an example-
For printing hello world in python, you write print("hello world") right ? But for my langauge you need to write it in the 
reversed alphabetical order which is  )"dlrow olleh"(tnirp infact the parenthesis are reversed as well.


------------------------------------------------------FILE FORMAT---------------------------------------------------------
When it comes to the file extension for nohtyp, it is also the opposite of python which is .yp
After writing the code in an editor like vscode, notepad etc., you need to save it with .yp extension so that the nohtyp
interpreter can recongnize it and run the program for you.

THANK YOU
            """





shellversion = '0.0.1'
website = 'www.nohtyp'
fileLocation = os.getcwd()
now = datetime.datetime.now()
date = datetime.datetime.date(now)
time = datetime.datetime.time(now)

cpuarch = platform.machine()
osver = platform.platform()

def InteractiveMode():
    print(f"""nohtyp Interative Shell {shellversion} (tags/v{shellversion} {date}, {time}) [{cpuarch} on {osver}]
Type "help", "version", "website", "locatefile" for more information. """)
    
    
    while True:
        inputCommand = input(">>> ")
        if inputCommand[::-1] == 'exit()':
            print("Exiting Shell.....")
            break
        elif inputCommand == 'help':
            print(helpmessage)
        elif inputCommand == 'version':
            print('>>>',shellversion)
        elif inputCommand == 'website':
            print('>>>',website)
        elif inputCommand == 'locatefile':
            print('>>>',fileLocation)
        else:
            exec(inputCommand[::-1])



InteractiveMode()
