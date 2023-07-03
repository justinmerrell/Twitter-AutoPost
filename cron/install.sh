#!/bin/bash
set -e

# Navigate to the project directory
cd /opt/Twitter-AutoPost

# Check if Python 3.11 is installed
if ! command -v python3.11 &> /dev/null
then
    echo "Python 3.11 could not be found. Please install Python 3.11 and try again."
    exit
fi

# Remove the existing virtual environment if it exists
rm -rf /opt/Twitter-AutoPost/env

# Create a new virtual environment in the correct location and activate it
python3.11 -m venv /opt/Twitter-AutoPost/env
source /opt/Twitter-AutoPost/env/bin/activate

# Install requirements.txt
pip install -r requirements.txt

# Add or update the cron job
# If "--live" is passed to the script, include it in the run.sh call
if [[ $* == *--live* ]]; then
    (crontab -l 2>/dev/null || true; echo "0 0 * * 0 bash /opt/Twitter-AutoPost/cron/run.sh --live > /opt/Twitter-AutoPost/output.log 2> /opt/Twitter-AutoPost/error.log") | crontab -
else
    (crontab -l 2>/dev/null || true; echo "0 0 * * 0 bash /opt/Twitter-AutoPost/cron/run.sh > /opt/Twitter-AutoPost/output.log 2> /opt/Twitter-AutoPost/error.log") | crontab -
fi

# Deactivate the virtual environment
deactivate
