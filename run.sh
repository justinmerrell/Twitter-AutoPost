#!/bin/bash

# Activate the virtual environment
source /root/automation/Twitter-AutoPost/env/bin/activate

# Call the main.py script
python /root/automation/Twitter-AutoPost/tweet.py

# Deactivate the virtual environment
deactivate
