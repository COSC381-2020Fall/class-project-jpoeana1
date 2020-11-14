from flask import Flask, render_template, request, jsonify, redirect
import query_on_whoosh
import smtplib
import config
import math
import sqlite3



# turn this file (app.py) into a web app
app = Flask(__name__)
app.config.update(dict(JSONIFY_PRETTYPRINT_REGULAR=True))

# I want to build an app that has a route that listens to /
@app.route("/")
def handle_slash():
    requested_name = request.args.get("name")
    return render_template("index.html", user_name=requested_name)

@app.route("/test/", strict_slashes=False)
def handle_test():
    input = "abc"    # request.args.get("i")
    return test_module.test(input)

@app.route("/query", strict_slashes=False)
def handle_query():
    query_term = request.args.get("q")
    query_page = int(request.args.get("p"))
    return jsonify({"query_term": query_term, "search_results": query_on_whoosh.query(query_term, current_page=query_page)})

@app.route("/query_view", strict_slashes=False)
def handle_query_view():
    query_term = request.args.get("q")
    if not query_term:
        query_term = ""

    query_page_arg = request.args.get("p")
    if not query_page_arg:
        query_page_arg = "1"

    conn = sqlite3.connect('history.db')
    c = conn.cursor()
    
    # INSERT INTO search_terms (id, term, search_time) VALUES (1, 
    #'baby', strftime('%s', 'now')); delete from search_terms (id, term, search_time) values (1, 'garbage
    #', strftime('%s', 'now'));
    #c.executescript(f"INSERT INTO search_terms (id, term, search_time) VALUES (1, '{query_term}', strftime('%s', 'now'));");
    c.execute("INSERT INTO search_terms (term, search_time) VALUES (?, strftime('%s', 'now'));",  (query_term,))
    c.execute("SELECT * FROM search_terms;")
    rows = c.fetchall()
    conn.commit()
    conn.close()

    query_page = int(query_page_arg)
    search_results = query_on_whoosh.query(query_term, current_page=query_page)
    return  render_template("query.html", 
                            results=search_results[0], 
                            query_term=query_term, 
                            page_cnt=math.ceil(search_results[1]/10), 
                            current_page=query_page, 
                            history_list=rows)


@app.route("/about", strict_slashes=False)
def handle_about():
    return render_template("about.html")


@app.route("/success", strict_slashes=False)
def handle_request():
    new_data = request.args.get("new_data")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("jpoeana1@emich.edu", config.gmail_password)
    message = "Subject: {}\n\n{}".format("Request to add new data", "request to add: " + new_data)
    server.sendmail("jpoeana1@emich.edu", "jpoeana1@emich.edu", "request " + new_data)
    return render_template("success.html", new_data=new_data)