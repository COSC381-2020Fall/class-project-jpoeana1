import json
from tqdm import tqdm
import sys

if __name__ == '__main__':
    search_result_file = sys.argv[1]
    output_file = sys.argv[2]

    video_ids = []
    with open(search_result_file) as f:
        results = json.load(f)
        for item in tqdm(results):
            if "videoobject" in item["pagemap"]:
                video_ids.append(item["pagemap"]["videoobject"][0]["videoid"])

    with open(output_file, 'w') as f:
        for video_id in video_ids:
            f.write(f'{video_id}\n')