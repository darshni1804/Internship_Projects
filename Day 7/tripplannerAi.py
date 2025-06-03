import webbrowser
import os

filename = 'trip_planner.html'

# Check if file exists
if os.path.exists(filename):
    # Open in default web browser
    webbrowser.open('file://' + os.path.realpath(filename))
else:
    print(f"Error: {filename} not found.")
