#!/bin/bash
set -e

# Activate the virtual environment
source /opt/Twitter-AutoPost/env/bin/activate

# Call the main.py script with or without the --live flag
if [[ $* == *--live* ]]; then
    cd /opt/Twitter-AutoPost && /opt/Twitter-AutoPost/env/bin/python /opt/Twitter-AutoPost/tweet.py --live
else
    cd /opt/Twitter-AutoPost && /opt/Twitter-AutoPost/env/bin/python /opt/Twitter-AutoPost/tweet.py
fi

# Deactivate the virtual environment
deactivate
