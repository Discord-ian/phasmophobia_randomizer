import json
import random

data = json.loads(open("server/topics.json", "r").read())


def get_topic():
    picked = random.choice(data["topics"])
    picked = check_regex(picked)
    return picked


def check_regex(item):
    if "{0." in item:
        to_c = item.split("{0.")[1].split("}")[0]
        if to_c == "random":
            return item.replace("{0.random}", random.choice(data["itemList"]))
        if to_c == "identifiableItems":
            return item.replace("{0.identifiableItems"), random.choice(data["identifiableList"])
    return item


print(get_topic())
