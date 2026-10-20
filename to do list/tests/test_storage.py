import json

with open("tasks.json", "w") as f:
    a = json.dumps("t", indent=3)
