"""
This script handles specific interactions between the user and
the bot, by processing greetings and goodbyes. It makes use of
regular expressions and the fuzzy matching from the regex module
allowing for slight flexibility in interactions.

Brendan Dileo
"""

import random
import regex as re

greetings_pattern = r"(\bhello\b|\bhi\b|\bhey\b|\bwhats up\b|\bgreetings\b){e<=1}"
greetings = [
    "Hi!",
    "Hey there!",
    "Hello there!",
    "Hello! Ask away!",
    "Greetings!",
    "Hi, good to see you!",
    "Hey! Feels good to be up and running!"
]

goodbyes_pattern = r"(\bgoodbye\b|\bbye\b|\bsee you later\b|\btake care\b|\bfarewell\b|\bhave a good day\b){e<=1}"
goodbyes = ["Have a good day!", "Is it time to leave already?!", "Goodbye!", "Bye Bye!"]


def respond_to_greeting(utterance):
    if re.search(greetings_pattern, utterance, re.IGNORECASE):
        return random.choice(greetings)
    return None

def respond_to_goodbye(utterance):
    if re.search(goodbyes_pattern, utterance, re.IGNORECASE):
        return random.choice(goodbyes)
    return None