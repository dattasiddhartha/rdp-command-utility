import argparse
import os, sys, time, subprocess
import pandas as pd
import itertools
import keyboard
from pywinauto import Application, Desktop
from util import *
"""
Usage:

-Running the CLI-
python cli.py
python <filepath>/cli.py --commands_file commands.txt --credentials_file credentials.txt

-Storing commands-
commands.txt stores the time delays between each command.
default time delay between characters in text is 100ms.
default time delay between commands is 1000ms.
entering ms value in time_delay column specifies time delay after the execution of the command.

-Storing credentials-
credentials.txt contain the list of remote desktop ip & password configurations.
"""

parser = argparse.ArgumentParser(description='rdp command execution utility')
parser.add_argument('--commands_file', type=str, default="commands.txt",
                    help='Filename for commands.txt')
parser.add_argument('--credentials_file', type=str, default="credentials.txt",
                    help='Filename for credentials.txt')
args = parser.parse_args()

commands = pd.read_csv(args.commands_file, index_col=None)
credentials = pd.read_csv(args.credentials_file, index_col=None)
special_commands = ['winr', '<enter>']
default_keystrokes = ['alt', 'alt gr', 'ctrl', 'left alt', 'left ctrl', 'left shift', 'left windows', 'right alt', 'right ctrl', 'right shift', 'right windows', 'shift', 'windows']

for index, row in credentials.iterrows():
    ip, username, password = row['ip'], row['username'], row['password']
    for cdx, command in commands.iterrows():
        processshift_timedelay = 1
        inprocess_timedelay = 0.05
        if command['command'] == 'start_rdp': 
            start_rdp(ip, username, password)
            
            windows = Desktop(backend="win32").windows()
            window_indices = [w.window_text() for w in windows if ip in w.window_text().lower()][0]
            print(window_indices)

            app = Application(backend="win32").connect(title=window_indices)
            window_rdp = app.window(title_re=window_indices)
            
            window_rdp.set_focus()
            time.sleep(processshift_timedelay)
            
        if command['command'] == 'kill_rdp': kill_rdp()
            
        if cdx > 0:
            if command['time_delay'] == command['time_delay']: processshift_timedelay = int(command['time_delay']/1000)
            
            if command['command'] not in special_commands: enter_text(command['command'], inprocess_timedelay)
            if command['command'] == 'winr': open_winr(processshift_timedelay)
            if command['command'] == '<enter>': 
                keyboard.press_and_release('enter')
                time.sleep(processshift_timedelay)
            
