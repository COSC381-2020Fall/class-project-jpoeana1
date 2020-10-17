#!/usr/bin/python3
import pprint
from googleapiclient.discovery import build
import config

my_api_key = config.my_api_key # The API KEY you aquired
my_cse_id = config.my_cse_id # The search-engine-ID you created
# ces: custom search engine
my_search_topic = 'BTS' #The phrase that you want to search

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

thislist = []

for n in range(10):
    if __name__ == '__main__':
        results = google_search(my_search_topic, my_api_key, my_cse_id, num=10)
        thislist.insert(n, results)

pprint.pprint(thislist)



    
