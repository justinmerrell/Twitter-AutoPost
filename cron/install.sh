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

# Create a virtual environment and activate it
python3.11 -m venv env
source env/bin/activate

# Install requirements.txt
pip install -r requirements.txt

# Make run.sh executable
chmod +x run.sh

# Add or update the cron job
# If "--live" is passed to the script, include it in the run.sh call
if [[ $* == *--live* ]]; then
    (crontab -l 2>/dev/null || true; echo "0 0 * * * /opt/Twitter-AutoPost/cron/run.sh --live > /opt/Twitter-AutoPost/output.log 2> /opt/Twitter-AutoPost/error.log") | crontab -
else
    (crontab -l 2>/dev/null || true; echo "0 0 * * * /opt/Twitter-AutoPost/cron/run.sh > /opt/Twitter-AutoPost/output.log 2> /opt/Twitter-AutoPost/error.log") | crontab -
fi

# Deactivate the virtual environment
deactivate
