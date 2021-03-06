# class-project-jpoeana1

## Set up Python verion: 3.7.9
1. run: `python3 -m pip install -r requirements.txt`

## Retrieves Google Search results
1. modify config.py to add your api key and cse key
2. run: `python3 cse.py`

## Retrieves Video Ids from search results
1. run: `python3 parse_search_results.py google_search.json videoids.txt`

## Retrives YouTube Data
1. run: `python3 download_youtube_data.py videoids.txt`

## Prepares for Whoosh Index
1. run: `python3 create_data_for_indexing.py`

## Create Whoosh Indexing
1. run: `python3 create_whoosh_index.py`

## Query on Whoosh
1. run: `python3 query_on_whoosh.py home 2 1` will output a json-format result

## Flask App for Query on Whoosh
To run locally
1. run: `flask run`

To run forever remotely using public IP
1. run: `screen -S flask-server`
2. run: `flask run --host 0.0.0.0`
3. run: `ctrl + A D` this will detach from screen
4. Copy your AWS public IP address and paste it into web browser ending with `:5000/query?q=<search_term>&p=<query_page>`

To end run forever
1. run: `screen -ls` this will list the screens in use
2. Copy paste the screen name - should end in '_flask-server_'
3. run: `screen -r <screen_name>` this will retach screen
4. run: `exit` this will kill terminal script