from pathlib import Path
import json

paths = [str(x) for x in Path('./youtube_data').glob('**/*.json')]
results = []
for path in paths:
    with open(path, 'r') as f:
        data = json.load(f)
        print('Video ID: ' + f['video_id'])
        print('Title: ' + f['title'])
        print('Description: ' + f['desc'])
        print('')
        # insert your code here

with open('data_for_indexing.json', 'w') as dump_file:
    json.dump(results, dump_file)
