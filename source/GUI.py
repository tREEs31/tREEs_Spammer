import sys
import tkinter as tk

from PIL import Image, ImageTk
from time import sleep
from tkinter import messagebox

from source.CLI_Styling import CommandLineUI
from source.Load_Configuration import UserConfig
from source.tREEs_SpamBot import tREEs_SpamBot

""" Create a class for the Tkinter Graphical User Interface."""
class GraphicalUI:

    # Initialise with a tk.Tk() arg. Import Objects.
    def __init__(self, root):
        self.ui = CommandLineUI()
        self.window = root
        self.config = UserConfig()
        self.config.Parse_Configuration()
        self.spambot = tREEs_SpamBot(window=self.window, gui=self)
    
        # Setting Window Icon with PIL PhotoImage as it handles more File Formats.
        self.wicon = Image.open(self.config.window_icon_path)
        self.window_icon = ImageTk.PhotoImage(self.wicon)
        self.window.wm_iconphoto(False, self.window_icon)

        
        # Setting Background Image with PIL PhotoImage.
        self.background_image = Image.open(self.config.window_bg_path)
        self.background_converted = ImageTk.PhotoImage(self.background_image)
        self.background = tk.Label(self.window, image=self.background_converted)
        self.background.pack()

        
        # Set Window Geometry, Title and Lock from Resizing if Specified.
        self.window.geometry("{}x{}".format(self.config.window_height, self.config.window_width))
        self.window.resizable(height=False, width=False)
        self.window_title = self.config.window_title
        self.window.title(self.window_title)

        
        # Label for Text Input Box.
        textbox_bgcolor = self.config.input_label_bgcolor
        textbox_fgcolor = self.config.input_label_fgcolor
        self.input_label = tk.Label(self.window, text="Enter Message To SPAM: ", bg=textbox_bgcolor, fg=textbox_fgcolor)
        self.input_label.place(relx=0.5, rely=0.4, anchor="n")
        # Text Box for Entering Message to Spam.
        self.input_box = tk.Entry(self.window, width=40)
        self.input_box.place(relx=0.5, rely=0.5, anchor="center")

        
        # Button to Start the Spambot.
        button_bgcolor = self.config.startbtn_bgcolor
        button_fgcolor = self.config.startbtn_fgcolor
        button_highlight = self.config.startbtn_highlight_color
        self.start_button = tk.Button(self.window, text="START", command=self.start, bg=button_bgcolor, fg=button_fgcolor)
        self.start_button.config(highlightbackground=button_highlight, highlightcolor=button_highlight)
        self.start_button.place(relx=0.85, rely=0.60, anchor="ne")

        
        # Button to Stop the Spambot.
        button_bgcolor = self.config.stopbtn_bgcolor
        button_fgcolor = self.config.stopbtn_fgcolor
        button_highlight = self.config.stopbtn_highlight_color
        self.stop_button = tk.Button(self.window, text="STOP", command=self.stop, bg=button_bgcolor, fg=button_fgcolor)
        self.stop_button.config(highlightbackground=button_highlight, highlightcolor=button_highlight)
        self.stop_button.place(relx=0.30, rely=0.60, anchor="ne")       


        # Init and add Text Label for Speed Options Slider.
        self.speed_options = self.config.speed_options
        self.speed_selected = tk.StringVar(self.window)
        self.speed_selected.set(self.speed_options[1])
        self.option_label = tk.Label(self.window, text="MSG Interval ", bg=textbox_bgcolor, fg=textbox_fgcolor)
        self.option_label.place(relx=0.60, rely=0.60, anchor="ne")
        
        # Options Slider for Setting SpamBot Interval.
        button_bgcolor = self.config.slider_bgcolor
        button_fgcolor = self.config.slider_fgcolor
        button_highlight = self.config.slider_highlight_color
        self.dropdown = tk.OptionMenu(self.window, self.speed_selected, *self.speed_options)
        self.dropdown.config(bg=button_bgcolor, fg=button_fgcolor, 
        highlightbackground=button_highlight, highlightcolor=button_highlight, highlightthickness=2)
        self.dropdown["menu"].config(bg=button_bgcolor, fg=button_fgcolor)
        self.dropdown.place(relx=0.56, rely=0.67, anchor="ne")


        # Init and set Text Label for Message Count Options Slider.
        self.count_options = self.config.count_options
        self.count_selected = tk.StringVar(self.window)
        self.count_selected.set(self.count_options[0])
        self.count_label = tk.Label(self.window, text="MSG Count:", bg=textbox_bgcolor, fg=textbox_fgcolor)
        self.count_label.place(relx=0.59, rely=0.78, anchor="ne")

        # Count Slider for Specifying Amount of Messages to Send.
        button_bgcolor = self.config.count_bgcolor
        button_fgcolor = self.config.count_fgcolor
        button_highlight = self.config.count_highlight
        self.count_menu = tk.OptionMenu(self.window, self.count_selected, *self.count_options)
        self.count_menu.config(bg=button_bgcolor, fg=button_fgcolor,
        highlightbackground=button_highlight, highlightcolor=button_highlight, highlightthickness=2)
        self.count_menu["menu"].config(fg=button_fgcolor, bg=button_bgcolor)
        self.count_menu.place(relx=0.56, rely=0.86, anchor="ne")

    # Start the SpamBot.
    def start(self):
        # Disable the Text Input Functionality or TKinter Hangs.
        self.input_box.config(state="disabled")
        self.input_label.config(text="ACTIVATED! Click the Target!...", fg="green")
        self.window.update()
        user_text = self.input_box.get()                # Message Input
        speed_selected = self.speed_selected.get()      # Speed Option
        count_selected = self.count_selected.get()      # Msg Amount
        # Set spambot.spamming = True or spambot.Spam_Text won't Start.
        if count_selected !="∞":
            self.spambot.Spam_Text(string=user_text, interval=speed_selected, count_max=int(count_selected))
        else:
            self.spambot.Spam_Text(string=user_text, interval=speed_selected)

    # Stop the SpamBot.
    def stop(self):
        # Set spam flag to False, release Textbox and Inform.
        self.spambot.spamming = False
        self.input_box.config(state="normal")
        self.input_label.config(text="STOPPED! Spamming Complete!", fg="red")
        self.window.update()
        sleep(3) # Pause to allow user to see Message Update.
        self.input_label.config(text="Enter Message To SPAM: ", fg=self.config.input_label_fgcolor)
        self.window.update()


    # Print Runtime Statistics to the CommandLine UI when window closes.
    def on_window_close(self):
        # If the SpamBot is Spamming the tk.mainloop() isn't listening for
        # events and therefor can't close the window, so by default we do
        # not allow the user to close, and Instruct them on Next Steps.
        if self.spambot.spamming == True:
            messagebox.showwarning("SPAMMING", "Cancel SPAM First.", icon=messagebox.WARNING)
        
        elif self.spambot.spamming == False:
            self.ui.Calculate_RunTime()
            sys.exit(0)


