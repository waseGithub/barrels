#!/bin/bash

if ! pgrep -f "python3 /home/waselab2/Documents/barrels/barrel_sql/pull_arduino.py" >/dev/null; then
  echo "Script is not running. Starting..."
  gnome-terminal --command "python3 /home/waselab2/Documents/barrels/barrel_sql/pull_arduino.py"
else
  echo "Script is already running."
fi
