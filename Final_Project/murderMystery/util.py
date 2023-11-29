import json


def connect_data():
    """Get data from data.json file"""
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print("Unable to load data: ", e)
        exit()
