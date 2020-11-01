import os
import sys
import json
from tqdm import tqdm

from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID

def createSearchableData(data_file):
    '''
    Schema definition: video id, video title, description
    '''
    schema = Schema(id=ID(stored=True), title=TEXT(stored=True), description=TEXT(stored=True))
    if not os.path.exists("indexdir"):
        os.mkdir("indexdir")

    # Creating an index writer to add document as per schema
    ix = create_in("indexdir", schema)
    writer = ix.writer()

    with open(data_file) as f:
        youtube_array = json.load(f)
        for youtube_item in tqdm(youtube_array):
            youtube_id = youtube_item['id']
            youtube_title = youtube_item['title']
            youtube_description = youtube_item['description']
            writer.add_document(id=youtube_id, title=youtube_title, description=youtube_description)

    writer.commit()

if __name__ == "__main__":
    data_file = 'data_for_indexing.json' 
    createSearchableData(data_file)