import json

def fetch_jobs(path):
    with open(path) as f:
        return json.load(f)
