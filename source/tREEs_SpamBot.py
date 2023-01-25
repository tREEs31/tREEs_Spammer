import sys

from time import sleep
from pynput.keyboard import Key, Controller

from source.CLI_Styling import CommandLineUI


""" Create a class for the Main SpamBot Functions. """
class tREEs_SpamBot:


    # Initialise with Objects and create Spamming Boolean False.    
    def __init__(self, window, gui):
        self.window = window
        self.keyboard = Controller()
        self.spamming = False
        self.ui = CommandLineUI()
        self.gui = gui
    
    
    # Function for typing a string. self.window.after() causes a pause.
    def Type_String(self, string, interval):
        self.keyboard.type(string)
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)
        self.window.after(interval)
    
    
    # Function to call for Spamming Text.
    def Spam_Text(self, string, interval, count_max=None):
        # Interval needed in ms, simple conversion.
        interval = interval + "000"
        # Keeping inside a try / except block.
        try:
            count = 1
            # If theres a maximum no. of messages limit accordingly
            if count_max:
                self.spamming = True
                while count <= count_max and self.spamming == True:
                    self.Type_String(string=string, interval=interval)
                    self.ui.Print_Spamming(count=count, count_max=count_max)
                    count +=1
                    # When max is reached pass to GUI stop() function.
                    if count == count_max:
                        self.Type_String(string=string, interval=interval)
                        self.ui.Print_Spamming(count=count, count_max=count_max)
                        self.ui.Print_Debug(debug_message="Spamming Run Complete.")
                        self.gui.stop()

            
            # If theres no maximum set, let her rip
            elif not count_max:
                while self.spamming == True:
                    self.Type_String(string=string, interval=interval)
                    self.ui.Print_Spamming(count=count)
                    count +=1


        # Allow the user to cancel the Spam process from CLI.
        except KeyboardInterrupt:
            self.ui.Print_Error(error_message="Keyboard Interrupt. Spamming Stopped.")
            self.gui.stop() # Pass to GUI Stop Function.