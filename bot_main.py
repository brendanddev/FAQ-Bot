"""
Main script that allows for interactions between the user and faq bot.
It contains the logic for cleaning utterance (input), understanding
the users intent, and generating a response based on this intent.

Brendan Dileo

"""

from load_data import read_json_data
from greetings_goodbyes import respond_to_greeting, respond_to_goodbye
import re


def clean_utterance(utterance):
    clean = re.sub(r'[^\w\s]', '', utterance)
    clean = re.sub(r'\s+', ' ', clean).strip()
    return clean.lower()


def understand(utterance):
    cleaned_utterance = clean_utterance(utterance)
    for i, question in enumerate(intents):
        if clean_utterance(question) == cleaned_utterance:
            return i
    return -1


def generate(intent):
    if intent == -1:
        return "Sorry, I don't know the answer to that!"
    return responses[intent]


intents, responses = read_json_data()


def main():
    print("Welcome to Brendan's FAQ Bot!")
    print("The focus of this FAQ bot is on Pokemon Go!!")
    print()
    print("To begin interacting with the bot, greet it.")
    print("For example, you can say 'hi', 'hello', or similar greetings!")
    print("To stop interacting with the bot, say goodbye.")
    print("For example, you can say 'goodbye', 'bye', or similar goodbyes!")

    while True:
        utterance = input(">>>").lower()

        greeting_response = respond_to_greeting(utterance)
        if greeting_response:
            print(greeting_response)
            continue

        goodbye_response = respond_to_goodbye(utterance)
        if goodbye_response:
            print(goodbye_response)
            break

        intent = understand(utterance)
        response = generate(intent)
        print(response)
        print()


# Runs the chat code
if __name__ == "__main__":
    main()