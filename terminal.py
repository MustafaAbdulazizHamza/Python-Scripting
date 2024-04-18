import subprocess as sb
import os
import sys
from colorama import Fore, init
init(autoreset=True)
while True:
    try:
        loc = os.getcwd() # To get the current working directory 
        cmd = input(Fore.GREEN+f"{loc} >"+Fore.RESET)
        if cmd.lower() in ['exit', 'q']:
            sys.exit(0) # Exit the script
        if cmd.split()[0].lower() == 'cd': # Why?
            directory = cmd.split()[1]
            if os.path.isdir(directory): # Is a directory?
                os.chdir(directory)
            else:
                print(Fore.RED+"The directory {} was not found".format(directory))
        else:
            p1 = sb.run(cmd, shell=True, text=True, capture_output=True)
            if p1.returncode == 0: print(p1.stdout)
            else: print(Fore.RED+f"{p1.stderr}")
    except KeyboardInterrupt:
        print(Fore.RED+"You must enter `exit` or `q` to exit the terminal.")
    except IndexError: pass
    except Exception as e: print(Fore.RED+f"{e}")
