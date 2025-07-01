import json

with open("block_times_log.json") as f:
    data = json.load(f)

print(data[0].keys())
