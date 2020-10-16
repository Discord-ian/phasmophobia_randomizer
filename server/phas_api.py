from flask import Flask, request
import json
import random


app = Flask(__name__)

data = json.loads(open("topics.json", "r").read())


@app.route("/new-topic", methods=["GET"])
def new_topic():
    picked = random.choice(data["topics"])
    picked = check_regex(picked)
    return picked


def check_regex(item):
    if "{0." in item:
        to_c = item.split("{0.")[1].split("}")[0]
        if to_c == "random":
            return item.replace("{0.random}", random.choice(data["itemList"]))
        if to_c == "identifiableItems":
            return item.replace("{0.identifiableItems}", random.choice(data["identifiableItems"]))
    return item

if __name__ == "__main__":
    app.run(debug=False)