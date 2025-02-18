import os
import json

with open("./temp/start.cfg", "r") as f:
    data = json.loads(f.read())

print(data["Name"])