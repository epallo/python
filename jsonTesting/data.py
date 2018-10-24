#!/usr/bin/python
import json

file = open('test.json')
json_data = json.load(file)
file.close()

print(json_data["test"])
