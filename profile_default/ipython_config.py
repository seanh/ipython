import sys

c = get_config()
c.TerminalInteractiveShell.banner1 = f"Python {sys.version}\n"
c.TerminalInteractiveShell.confirm_exit = False
c.TerminalInteractiveShell.prompts_class = "IPython.terminal.prompts.ClassicPrompts"
c.TerminalInteractiveShell.separate_in = ""
