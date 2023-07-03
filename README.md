# Twitter AutoPost

Twitter AutoPost is a Python script that automatically posts tweets to your Twitter account. It fetches tweets from a custom function and adds a well-formatted disclaimer before posting the tweet.

## Features

- Automatically fetch tweets from a custom function
- Add a disclaimer to each tweet
- Post tweets to your Twitter account
- No manual authentication required for each tweet

## Requirements

- Python 3.6 or higher
- packages listed in `requirements.txt`

## Quick Installation (Cron)

1. Clone the repository:

    `git clone https://github.com/justinmerrell/Twitter-AutoPost.git /opt/Twitter-AutoPost`

2. Change the directory:

    `cd /opt/Twitter-AutoPost`

3. Run the installer script in the cron directory:

    `./cron/install.sh`

## Development Setup

1. Clone the repository:

    `git clone https://github.com/justinmerrell/Twitter-AutoPost.git`

2. Change the directory:

    `cd Twitter-AutoPost`

3. Install the required packages:

    `pip install -r requirements.txt`

    ```bash
    OPENAI_API_KEY=<your_api_key>

    TWITTER_CONSUMER_KEY=<your_consumer_key>
    TWITTER_CONSUMER_SECRET=<your_consumer_secret>

    TWITTER_ACCESS_TOKEN=<your_access_token>
    TWITTER_ACCESS_TOKEN_SECRET=<your_access_token_secret>

    CASHED_ACCESS_TOKEN=<your_cashed_access_token>
    CASHED_ACCESS_SECRET=<your_cashed_access_secret>

    GITHUB_USERNAME=<your_github_username>

    HEALTHCHECKS_URL=<your_healthchecks_url>
    HEALTHCHECKS_ID=<your_healthchecks_id>
    ```

## Usage

Run the script with the following command:

`python tweet.py`

## Customizing

You can customize the prompts that are used to generate the Tweets, as well as the disclaimer that is added to each Tweet. Under the `prompts` folder you will find the following files:

- `concept.txt` - This file contains the prompt that is used to generate the concept for the Tweet.
- `structure.txt` - This file contains the prompt that is used to generate the structure for the Tweet.

## Contributing

If you'd like to contribute to this project, please feel free to submit a pull request, open an issue, or fork the repository and make changes as you'd like.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
