"""
This script will read data from a json file, which contains
the list of intents and responses recognized by the FAQ Bot.

Brendan Dileo
"""

import json

def read_json_data():
    """
    Reads the intents and responses from the data file,
    and returns a parallel key value list.
    """
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            print("Data Loaded Successfully!")
        return data["questions"], data["answers"]
    except FileNotFoundError:
        print("Error: The data file is missing!")
    except json.JSONDecodeError:
        print("Error: There was an issue decoding the JSON data!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return [], []