import json, os, sys
from source.CLI_Styling import CommandLineUI

""" Create an Object for Loading in User Configuration. """
class UserConfig:


    # Initialise with CommandLine User Interface.
    def __init__(self):
        self.ui = CommandLineUI()


    # Function for checking whether or not a value is a Hex Color Code.
    # Returns True / False.
    def HexCode_Check(self, hex):
        if hex.startswith("#") == True and len(hex) == 7:
            return True
        else:
            return False


    # Function for Taking values from 'config.json'
    def Parse_Configuration(self):
        # Try to Open 'config.json' for Reading.
        try:
            with open('config.json') as cfgobj:
                config_file = json.load(cfgobj)

        # If 'config.json' can't be found, Handle OSError.
        except OSError:
            self.ui.Print_Error(error_message="Error loading 'config.json' forced SpamBot to Quit!")
            self.ui.Print_Error(error_message="Config file not found in Scripts Parent Directory.")
            self.ui.Print_Error(error_message="There is no way to Proceed. Exiting!")
            sys.exit(1)  


        # Load in Window Title.
        self.window_title = config_file.get("window_title")
        

        # Load in Window Icon Path and Verify .ico file
        self.window_icon_path = config_file.get("window_icon_path")
        if self.window_icon_path.endswith(".ico") == False:
            self.ui.Print_Error(error_message="Error with Loading 'config.json' forced SpamBot to Exit.")
            self.ui.Print_Error(error_message="The File supplied for the window icon isn't a .ico icon file.")
            self.ui.Print_Error(error_message="There is no way to Proceed. Exiting!")
            sys.exit(1)
        
        if os.path.exists(self.window_icon_path) == True:
            pass
        else:
            self.ui.Print_Error(error_message="Error with Loading 'config.json' forced SpamBot to Exit.")
            self.ui.Print_Error(error_message="The File Path supplied for the window icon does not exist.")
            self.ui.Print_Error(error_message="There is no way to Proceed. Exiting!")
            sys.exit(1)
        

        # Parse and Load Window Size Values.
        size_values = config_file.get("window_size")
        if size_values[1].endswith("px") and size_values[3].endswith("px"):
            pass

        else:
            # If the value doesn't look like it refers to Pixels, Error, Exit and Inform.
            self.ui.Print_Error(error_message="Error with Loading 'config.json' forced SpamBot to Exit.")
            self.ui.Print_Error(error_message="Values for 'window_size' not appended with px or otherwise Invalid.")
            self.ui.Print_Error(error_message="There is no way to Proceed. Exiting!")
            sys.exit(1)
        

        # Now verify Value supplied can be converted to Integer.
        try:
            self.window_height = int(size_values[1].strip("px"))
            self.window_width = int(size_values[3].strip("px"))

        # If the value doesn't look like it is an Integer, Error, Exit and Inform.
        except ValueError:
            self.ui.Print_Error(error_message="Error with Loading 'config.json' forced SpamBot to Exit.")
            self.ui.Print_Error(error_message="Value for 'window_size' was not Integer. Did you supply a String?")
            self.ui.Print_Error(error_message="There is no way to Proceed. Exiting!")
            sys.exit(1)


        # Check to Ensure window background filepath Exists. 
        self.window_bg_path = config_file.get("window_bg_image_path")
        if os.path.exists(self.window_bg_path) == True:
            pass
        
        # If the Filepath does not Exist, Error, Exit and Inform.
        else:
            self.ui.Print_Error(error_message="Error with Loading 'config.json' forced SpamBot to Exit.")
            self.ui.Print_Error(error_message="The filepath supplied for the window background does not exist.")
            self.ui.Print_Error(error_message="There is no way to Proceed. Exiting!")
            sys.exit(1)  
        

        # Load remaining Window Color Attributes.
        checklist = list([]) # Will append and use to Verify each string is Hex.
        self.input_label_bgcolor = config_file.get("textbox_bgcolor_hex")
        checklist.append(self.input_label_bgcolor)
        self.input_label_fgcolor = config_file.get("textbox_fgcolor_hex")
        checklist.append(self.input_label_fgcolor)
        self.stopbtn_bgcolor = config_file.get("stop_button_bgcolor")
        checklist.append(self.stopbtn_bgcolor)
        self.stopbtn_fgcolor = config_file.get("stop_button_fgcolor")
        checklist.append(self.stopbtn_fgcolor)
        self.stopbtn_highlight_color = config_file.get("stopbtn_highlight_hex")
        checklist.append(self.stopbtn_highlight_color)
        self.startbtn_bgcolor = config_file.get("start_button_bgcolor")
        checklist.append(self.startbtn_bgcolor)
        self.startbtn_fgcolor = config_file.get("start_button_fgcolor")
        checklist.append(self.startbtn_fgcolor)
        self.startbtn_highlight_color = config_file.get("startbtn_highlight_hex")
        checklist.append(self.startbtn_highlight_color)
        self.slider_bgcolor = config_file.get("speed_slider_bgcolor")
        checklist.append(self.slider_bgcolor)
        self.slider_fgcolor = config_file.get("speed_slider_fgcolor")
        checklist.append(self.slider_fgcolor)
        self.slider_highlight_color = config_file.get("slider_highlight_hex")
        checklist.append(self.slider_highlight_color)
        self.count_bgcolor = config_file.get("count_slider_bgcolor")
        checklist.append(self.count_bgcolor)
        self.count_fgcolor = config_file.get("count_slider_fgcolor")
        checklist.append(self.count_fgcolor)
        self.count_highlight = config_file.get("count_highlight_hex")
        checklist.append(self.count_highlight)


        # Ensure all values are Valid Hex Strings.
        for hex in checklist:
            if self.HexCode_Check(hex) == True:
                pass

            else:
                self.ui.Print_Error(error_message="Error in 'config.json' caused SpamBot to Quit.")
                self.ui.Print_Error(error_message="Entry: {} in WINDOW_COLORS is not a valid Hex Color Code.".format(hex))
                self.ui.Print_Error(error_message="There is no way to Proceed. Exiting!")
                sys.exit(1)
        

        # Load user Supplied Spambot Speed Options from 'config.json'
        self.speed_options = [] # Create Variable for list transfer.
        speed_options = config_file.get("speed_options")
        
        # Sanitize and verify each option is a valid Integer.
        for option in speed_options:
            option = option.strip("sec")
            
            try:
                option = int(option)
                self.speed_options.append(option)

            # If the Value does not look like a Integer, Error, Exit and Inform.
            except ValueError:
                self.ui.Print_Error(error_message="Error loading 'config.json' forced SpamBot to Quit!")
                self.ui.Print_Error(error_message="One or more of the Values in 'speed_options' is not a valid Integer.")
                self.ui.Print_Error(error_message="There is no way to Proceed. Exiting!")
                sys.exit(1)
        

        # Load User supplied Message Count Options from 'config.json'
        self.count_options = [] # Create list for variable transfer.
        count_options = config_file.get("count_options")

        # Sanitize and Verify each option is a Valid Integer.
        for option in count_options:
            
            # Append the Infinity Symbol if it Exists as its the only valid non-Int.
            if option == "∞":
                self.count_options.append(option)
            
            else:
                # Ensure all variables can be handled as type Integer.
                try:
                    option = int(option)
                    self.count_options.append(option)
                # If any of the Variables are not an Integer, Error, Exit and Inform.
                except ValueError:
                    self.ui.Print_Error(error_message="Error loading 'config.json' forced SpamBot to Quit!")
                    self.ui.Print_Error(error_message="The option {} in 'count_options' is not a valid Integer.".format(option))
                    self.ui.Print_Error(error_message="There is no way to Proceed. Exiting!")
                    sys.exit(1)

        
        # If all Operations were successful, Inform the user via CLI.
        self.ui.Print_Debug(debug_message="User Profile loaded from config.json.")