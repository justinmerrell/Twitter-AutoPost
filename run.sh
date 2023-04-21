#!/bin/bash

# Activate the virtual environment
source /opt/Twitter-AutoPost/env/bin/activate

# Call the main.py script
cd /opt/Twitter-AutoPost && /opt/Twitter-AutoPost/env/bin/python tweet.py

# Deactivate the virtual environment
deactivate
