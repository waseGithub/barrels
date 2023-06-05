#!/usr/bin/env python3

import subprocess

script_path = "/home/waselab2/Documents/barrels/barrel_sql/pull_arduino.py"

process_check_cmd = f"pgrep -fl 'python3 {script_path}'"

process_output = subprocess.check_output(process_check_cmd, shell=True)
process_output = process_output.decode().strip()

if any(script_path in line for line in process_output.split("\n")):
    print("Script is already running.")
else:
    print("Script is not running. Starting...")
    subprocess.Popen(["x-terminal-emulator", "-e", "python3", script_path])
