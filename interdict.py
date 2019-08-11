import json
from difflib import get_close_matches
import time

json_file = "data.json"
json_data = json.load(open(json_file, "r"))


def define_word(word_to_define):
    return "- {}".format("\n- ".join(json_data[word_to_define]))


title = "InterDiction: CLI Interactive Dictionary"
author = "Timothy Collins"
contact = "twwc.tech@protonmail.ch"
version = "0.0.1"


while True:
    word = input("Enter a word: ")
    if word == "-ex":
        print("Exiting...")
        time.sleep(1)
        print("Thank you for using {} v{}\nBy: {}\nContact: {}".format(title, version, author, contact))
        break
    elif word in json_data:
        print(define_word(word), "\n")
    elif len(get_close_matches(word, json_data.keys())) > 0:
        word_check = input(
            "Did you mean '{}' instead? Y for yes, N for no: ".format(get_close_matches(word, json_data.keys())[0]))
        if word_check.upper() == "Y":
            print(define_word(get_close_matches(word, json_data.keys())[0]), "\n")
        else:
            print("Not a known word, please check spelling.\n")
            continue
    else:
        print("Must enter a word or check spelling!\n")
