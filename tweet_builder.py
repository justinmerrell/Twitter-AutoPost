import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")


def generate_concept():
    '''
    Generate a concept using the GPT-3 Concept Prompt
    '''
    with open("prompts/concept.txt", "r", encoding="UTF-8") as concept_prompt_file:
        prompt = concept_prompt_file.read()

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content.strip(), prompt


def format_concept(concept):
    '''
    Format the concept into a tweet using the GPT-3 Structure Prompt
    '''
    with open("prompts/structure.txt", "r", encoding="UTF-8") as structure_prompt_file:
        prompt = structure_prompt_file.read()

    # Inject the concept into the prompt
    prompt.replace("{{CONCEPT}}", concept)

    # Inject the tweet length into the prompt
    disclaimer = get_disclaimer()
    tweet_length = str(280 - len(disclaimer) - 10)
    prompt.replace("{{TWEET_LENGTH}}", tweet_length)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content.strip(), prompt


def get_disclaimer():
    '''
    Get the disclaimer text
    '''
    with open("prompts/disclaimer.txt", "r", encoding="UTF-8") as disclaimer_prompt_file:
        disclaimer = disclaimer_prompt_file.read()

    # Inject GitHub link into the disclaimer
    disclaimer.replace("{{GITHUB_USERNAME}}", os.environ.get("GITHUB_USERNAME"))

    disclaimer = "\n\n" + disclaimer

    return disclaimer


def add_disclaimer(tweet_text):
    '''
    Add the disclaimer to the end of the tweet
    '''
    disclaimer = get_disclaimer()
    return tweet_text + "\n\n" + disclaimer


def get_tweet():
    '''
    Generate a tweet
    '''
    max_attempts = 10
    attempts = 0

    while attempts < max_attempts:
        concept, _ = generate_concept()
        tweet, _ = format_concept(concept)
        tweet = add_disclaimer(tweet)

        if len(tweet) <= 279:
            return tweet
        else:
            attempts += 1

    # If the function reaches this point, all attempts failed to generate a tweet shorter than 280 characters.
    raise ValueError("Unable to create a tweet within the character limit after 10 attempts.")


if __name__ == "__main__":
    print(get_tweet())
