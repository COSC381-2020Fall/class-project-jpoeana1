# class-project-jpoeana1

---cse.py---
Before running the program, you have to go to https://programmablesearchengine.google.com/ 
You create your account (using your personal email).
Obtaining your cse_id :
Then you input the search engine you want to make your search on, i.e. YouTube.
The site will produce a Seach Engine ID for you, that will be your my_cse_id. 
Copy that and paste it into the config file.
Obtaining your api_key :
Go to console.cloud.google.com (using your school email)
Then go to APIs & Services > Credentials 
You can set up your api there. Then you copy and paste the api id in the config.py
How to run cse.py:
In terminal "python3 cse.py"

---download_youtube_data_batch.sh & video_ids.txt & download_youtube_data.py & create_data_for_indexing.py---
To run these programs in terminal first run 
>$ bash download_youtube_data_batch.sh
>$ python3 create_data_for_indexing.py

--- requirements.txt & create_whoosh_index.py & query_on_whoosh.py---
To install whoosh from requirements in terminal
>$ python3 -m pip install -r requirements.txt

QueryParser searches for words. If you write in the quotations of query_on_whoosh.py "home and school" it will omit "and". It also ignores captials.

To run program:
>$ python3 create_whoosh_index.py
This will create a directory called indexdir that will have 3 files inside containing "MAIN" at the start.

>$ python3 query_on_whoosh.py
The result should show you the words searched and the time it took to find.


