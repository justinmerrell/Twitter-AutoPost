import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")


def generate_concept():
    prompt = """Create a unique and engaging Twitter post concept related to one of the following themes: artificial intelligence, technology trends, entrepreneurship, or personal development.
    The tweet should be concise, informative, and spark interest among the target audience. Ensure the content is original and relevant to Justin Merrell's personal brand and experiences.
    Do not mention Justin Merrell by name, if needed use the first person pronoun "I" or "me". Limit the length to 185 characters, do not wrap the concept in quotes.

    Justin Merrell context:
    Justin Merrell is a software developer and entrepreneur with diverse experiences, including dropping out of college, founding a successful makerspace, and embracing a minimalistic lifestyle.
    He has a strong background in various projects and has learned the importance of considering alternative perspectives and giving others the benefit of the doubt.
    His core values center around not following the masses, seeking happiness outside of the traditional path, and continuously learning and growing.
    Justin is working on building a consistent online presence and generating content to share his insights and experiences with a broader audience.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content.strip(), prompt


def format_concept(concept):
    prompt = f"""
    Using the concept "{concept}", create a unique and engaging Twitter post related to one of the following themes: artificial intelligence, technology trends, entrepreneurship, or personal development.
    Only return the text of the tweet, do not wrap it in quotes, limit the length to 185 characters.

    Select one of the following formats:
    1. Question-based format:
        - Start with a thought-provoking question related to the theme
        - Provide a brief insight or fact
        - End with a call-to-action (e.g., inviting readers to share their thoughts, read your blog post, etc.)
    Example: What's the next big breakthrough in AI? 🤖 Recent advancements in machine learning are revolutionizing industries! 💡 Share your thoughts below! #AI #TechTrends

    2. Statistic or fact-based format:
        - Begin with an interesting statistic or fact related to the theme
        - Offer a short commentary or perspective on the fact
        - Include relevant hashtags
    Example: Did you know? 90% of startups fail within the first 5 years. 😯 Perseverance and adaptability are key! 💪 #Entrepreneurship #StartupLife

    3. Insight or tip-based format:
        - Share a valuable insight or tip related to the theme
        - Include a brief explanation or example
        - Add relevant emojis and hashtags for engagement
    Example: Boost your productivity with the Pomodoro Technique! ⏲️ Work in focused 25-minute intervals followed by a short break. 🌟 Try it today! #PersonalDevelopment #ProductivityTips
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content.strip(), prompt


def add_disclaimer(tweet_text):
    # disclaimer = "\n[Automated tweet. Source code: https://github.com/justinmerrell. Please consider following or sponsoring!]"
    disclaimer = "\n\n[Automated tweet | Source code: github.com/justinmerrell | Consider following or sponsoring!]"
    return tweet_text + disclaimer


def get_tweet():
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        concept, concept_prompt = generate_concept()
        tweet, tweet_prompt = format_concept(concept)
        tweet = add_disclaimer(tweet)

        if len(tweet) <= 280:
            return tweet
        else:
            attempts += 1

    # If the function reaches this point, all 3 attempts failed to generate a tweet shorter than 280 characters.
    raise ValueError("Unable to create a tweet within the character limit after 3 attempts.")
