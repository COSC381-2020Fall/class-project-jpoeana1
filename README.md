# class-project-jpoeana1

---cse.py--- <br>
Before running the program, you have to go to https://programmablesearchengine.google.com/  <br>
You create your account (using your personal email). <br>
Obtaining your cse_id : <br>
Then you input the search engine you want to make your search on, i.e. YouTube. <br>
The site will produce a Seach Engine ID for you, that will be your my_cse_id. <br>
Copy that and paste it into the config file. <br>
Obtaining your api_key : <br>
Go to console.cloud.google.com (using your school email) <br>
Then go to APIs & Services > Credentials <br>
You can set up your api there. Then you copy and paste the api id in the config.py <br><br>
How to run cse.py: <br>
In terminal "python3 cse.py" <br>
<br>

---download_youtube_data_batch.sh & video_ids.txt & download_youtube_data.py & create_data_for_indexing.py--- <br>
To run these programs in terminal first run <br>
>$ bash download_youtube_data_batch.sh <br>
>$ python3 create_data_for_indexing.py <br>

--- requirements.txt & create_whoosh_index.py & query_on_whoosh.py--- <br>
To install whoosh from requirements in terminal <br>
>$ python3 -m pip install -r requirements.txt <br>

QueryParser searches for words. If you write in the quotations of query_on_whoosh.py "home and school" it will omit "and". It also ignores captials. <br>

To run program:
>$ python3 create_whoosh_index.py <br>
This will create a directory called indexdir that will have 3 files inside containing "MAIN" at the start. <br>

>$ python3 query_on_whoosh.py <br>
The result should show you the words searched and the time it took to find.


