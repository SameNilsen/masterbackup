import json

JSON_file = json.load(open('test.json', 'r'))

with open('test.jsonl', 'w') as outfile:
    for entry in JSON_file:
        json.dump(entry, outfile)
        outfile.write('\n')