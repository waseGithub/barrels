#!/usr/bin/env python3

import subprocess

script_path = "/home/waselab2/Documents/barrels/barrel_sql/pull_arduino.py"

try:
    subprocess.check_output(["pgrep", "-f", "python3", script_path])
    print("Script is already running.")
except subprocess.CalledProcessError:
    print("Script is not running. Starting...")
    subprocess.Popen(["x-terminal-emulator", "-e", "python3", script_path])
