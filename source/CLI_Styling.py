import subprocess, sys

from colorama import Fore
from datetime import datetime

from time import gmtime, strftime

""" Create a class for Commandline UI Elements. """
class CommandLineUI:

    def __init__(self):
        self.start = strftime("%H:%M:%S", gmtime())
        # Colors.
        self.red = Fore.RED
        self.green = Fore.GREEN
        self.white = Fore.WHITE
        self.clear = Fore.RESET
        # Colored Symbols
        self.error_symbol = self.red + "[!]" + self.clear
        self.ack_symbol = self.green + "[-]" + self.clear
    

    # Print Statement for General Output / Debugging Messages.
    def Print_Debug(self, debug_message):
        current_time = strftime("%H:%M:%S", gmtime())
        print(f"{self.green}[{self.clear}{current_time}{self.green}]{self.clear} - {self.ack_symbol}: {debug_message}")


    # Print Statement for when an Error Occurs.
    def Print_Error(self, error_message):
        current_time = strftime("%H:%M:%S", gmtime())
        print(f"{self.red}[{self.clear}{current_time}{self.red}]{self.clear} - {self.error_symbol}: {error_message} ")

    # Print the Banner, Iterate chars to color with Colorama.
    def Print_Banner(self):
        self.Clear_Terminal()
        Banner = []
        with open('images/banner.ascii', 'r') as f:
            for line in f.readlines():
                for char in line:
                    Banner.append(char)
        
        colored_banner = []
        for character in Banner:
            if character == "█":
            
                if character.endswith("\n") == True:
                    character = self.white + character + self.clear + "\n"
                    colored_banner.append(character)
                
                else:
                    character = self.white + character + self.clear
                    colored_banner.append(character)
            
            else:
                character = self.red + character + self.clear
                colored_banner.append(character)
        
        print("".join(colored_banner))
        print(f"{self.red}" + "_"*17 + f"{self.white}" + f" by tREEs {self.red}" + "_"*23 + f"{self.white}v 1.0 {self.red}" + "_"*6 + f"{self.clear}\n")


    # Print Statements for when SpamBot is Active.
    def Print_Spamming(self, count, count_max=None):
        current_time = strftime("%H:%M:%S", gmtime())
        if count_max:
            print(f"{self.green}[{self.clear}{current_time}{self.green}]{self.clear} - {self.green} [ MSG {count} / {count_max} ]{self.clear} -: Input Transmitted Successfully.")
        
        else:
            print(f"{self.green}[{self.clear}{current_time}{self.green}]{self.clear} - {self.ack_symbol}: Message {count} Transmitted Successfully.")


    # Function for Calculating the Spambots total Runtime.
    def Calculate_RunTime(self):
        self.end = strftime("%H:%M:%S", gmtime())
        self.start_time = datetime.strptime(self.start, "%H:%M:%S")
        self.end_time = datetime.strptime(self.end, "%H:%M:%S")
        time_elapsed = self.end_time - self.start_time
        self.Print_Debug(debug_message="Total Runtime: {}".format(time_elapsed))

    
    # Function for Clearing the Terminal Screen.
    def Clear_Terminal(self):
        # Set Clear Command for Windows OS.
        if sys.platform.lower().startswith("win") == True:
            subprocess.run('cls', shell=True)
        
        # Else Assume UNIX / IOS 
        else:
            subprocess.run('clear', shell=True)