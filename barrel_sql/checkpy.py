#!/usr/bin/env python3

import psutil
import subprocess

script_path = "/home/waselab2/Documents/barrels/barrel_sql/pull_arduino.py"

is_running = False

for proc in psutil.process_iter(["cmdline"]):
    if proc.info["cmdline"] and proc.info["cmdline"][0] == "python3" and script_path in proc.info["cmdline"]:
        is_running = True
        break

if is_running:
    print("Script is already running.")
else:
    print("Script is not running. Starting...")
    subprocess.Popen(["x-terminal-emulator", "-e", "python3", script_path])
