import tkinter as tk

from source.GUI import GraphicalUI
from source.CLI_Styling import CommandLineUI

# Create a Root Object, pass to GUI Window and Loop.
if __name__ == '__main__':
    root = tk.Tk()
    CLI_Output = CommandLineUI()
    CLI_Output.Print_Banner()
    tREEs_SpamBot = GraphicalUI(root)
    # Edit the Window Deletion Protocol to trigger Program Closure.
    root.protocol("WM_DELETE_WINDOW", tREEs_SpamBot.on_window_close)
    root.mainloop()