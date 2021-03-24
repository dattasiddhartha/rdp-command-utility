import os, sys, time, subprocess
import pandas as pd
import itertools
import keyboard
from pywinauto import Application, Desktop

# Managing remote desktop session
def start_rdp(ip, username, password):
    try:
        os.system(
                    """
                    cmdkey /generic:"{}" /user:"{}" /pass:"{}"
                    """.format(ip, username, password)
                ) 
        subprocess.run("mstsc /v:{} /f".format(ip), shell=True, timeout=5)
    except:
        return 0
    
def kill_rdp():
    subprocess.run("taskkill /F /IM:mstsc.exe /T", shell=True, timeout=5)
    
# key commands
def open_winr(processshift_timedelay):
    # execute win+r
    keyboard.press('left windows')
    keyboard.press_and_release('r')
    keyboard.release('left windows')
    time.sleep(processshift_timedelay)

def enter_text(text, inprocess_timedelay):
    for i in text:
        keyboard.press_and_release(i)
        time.sleep(inprocess_timedelay)
    
def run_winr_command(text, processshift_timedelay, inprocess_timedelay):
    open_winr(processshift_timedelay)
    enter_text(text, inprocess_timedelay)
    keyboard.press_and_release('enter')
    time.sleep(processshift_timedelay)
    
def run_cmd_command(cmd_command, processshift_timedelay, inprocess_timedelay):
    # launch cmd    
    open_winr(processshift_timedelay)
    enter_text('cmd', inprocess_timedelay)
    keyboard.press_and_release('enter')
    time.sleep(processshift_timedelay)
    # run cmd command    
    enter_text(cmd_command, inprocess_timedelay)
    keyboard.press_and_release('enter')
    time.sleep(processshift_timedelay)