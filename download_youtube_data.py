import pprint
import sys
import json
from googleapiclient.discovery import build


my_api_key = "AIzaSyDHVW1JvQ1icKL_YQul2z30YwQUPmcr53k"

def youtube_data(video_id):
    service = build("youtube", "v3", developerKey=my_api_key)
    result = service.videos().list(part='snippet', id=video_id).execute()
    return result

if __name__ == '__main__':
    result = youtube_data(sys.argv[1])
    pprint.pprint(result)
    with open(sys.argv[1]+'.json','w') as dump_file:
            json.dump(result,dump_file)

