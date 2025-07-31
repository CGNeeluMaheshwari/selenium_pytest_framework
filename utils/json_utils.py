import json


def load_test_data(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
    return [(item["username"], item["password"], item["expected"]) for item in data]
