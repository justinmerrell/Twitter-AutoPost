# Twitter AutoPost

Twitter AutoPost is a Python script that automatically posts tweets to your Twitter account. It fetches tweets from a custom function and adds a well-formatted disclaimer before posting the tweet.

## Features

- Automatically fetch tweets from a custom function
- Add a disclaimer to each tweet
- Post tweets to your Twitter account
- No manual authentication required for each tweet

## Requirements

- Python 3.6 or higher
- `requests`
- `requests_oauthlib`
- `python-dotenv`

## Installation

1. Clone the repository:

git clone https://github.com/justinmerrell/Twitter-AutoPost.git


2. Change the directory:

cd Twitter-AutoPost


3. Install the required packages:

pip install -r requirements.txt


4. Create a `.env` file in the project root directory and add your Twitter API credentials:

TWITTER_CONSUMER_KEY=<your_consumer_key>
TWITTER_CONSUMER_SECRET=<your_consumer_secret>
TWITTER_ACCESS_TOKEN=<your_access_token>
TWITTER_ACCESS_TOKEN_SECRET=<your_access_token_secret>


5. Customize the `get_tweet()` function in `tweet_former.py` to generate your desired tweet content.

## Usage

Run the script with the following command:

python tweet.py


The script will fetch a tweet from the `get_tweet()` function, add the disclaimer, and post the tweet to your Twitter account.

## Contributing

If you'd like to contribute to this project, please feel free to submit a pull request, open an issue, or fork the repository and make changes as you'd like.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgements

- Twitter API
- `requests` library
- `requests_oauthlib` library
- `python-dotenv` library
