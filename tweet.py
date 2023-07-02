import os
import sys
import json

from src.tweet_builder import get_tweet
from requests_oauthlib import OAuth1Session
import os
import json
import logging
import argparse
from dotenv import load_dotenv

# ---------------------------------------------------------------------------- #
#                                    Logging                                   #
# ---------------------------------------------------------------------------- #
logger = logging.getLogger("tweet")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))

# ---------------------------------------------------------------------------- #
#                                Required Files                                #
# ---------------------------------------------------------------------------- #
# Check if the tweet history file exists. If not, create it.
if os.path.exists("tweet_history.json"):
    try:
        with open("tweet_history.json", "r", encoding="utf-8") as tweet_history_file:
            json.load(tweet_history_file)
    except json.decoder.JSONDecodeError:
        with open("tweet_history.json", "w", encoding="utf-8") as tweet_history_file:
            tweet_history_file.write("[]")
else:
    with open("tweet_history.json", "w+", encoding="utf-8") as tweet_history_file:
        tweet_history_file.write("[]")


def setup_oauth():
    '''
    Setup OAuth1 authentication with Twitter.
    '''
    load_dotenv()

    consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
    consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
    access_token = os.getenv("CASHED_ACCESS_TOKEN")
    access_token_secret = os.getenv("CASHED_ACCESS_SECRET")

    return OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )


def post_tweet(oauth, payload):
    '''
    Post a tweet to Twitter.
    '''
    response = oauth.post(
        "https://api.twitter.com/2/tweets",
        json=payload,
    )

    if response.status_code not in [200, 201]:
        raise Exception(
            f"Request returned an error: {response.status_code} {response.text}"
        )

    print(f"Response code: {response.status_code}")
    print(json.dumps(response.json(), indent=4, sort_keys=True))


def main(live=False):
    '''
    Generate a tweet and post it to Twitter.
    '''
    logger.info("Generating tweet...")

    tweet = get_tweet()
    logger.info(f"Tweet: {tweet}")

    if live:
        oauth = setup_oauth()
        logger.info("Live mode. The tweet will be posted to Twitter.")
        payload = {"text": tweet}
        post_tweet(oauth, payload)
    else:
        logger.info("Dry run mode. The tweet will not be posted.")
        logger.info(f"Tweet: {tweet}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Post tweets to Twitter.')
    parser.add_argument('--live', action='store_true',
                        help='If set, the tweet will be posted to Twitter. Otherwise, the tweet will be printed to the console.')
    args = parser.parse_args()

    main(args.live)
