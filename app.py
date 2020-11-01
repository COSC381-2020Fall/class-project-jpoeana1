from flask import Flask, render_template, request, jsonify
import query_on_whoosh

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
    return jsonify({"query_term": query_term, "search_results": query_on_whoosh.query(query_term)})

# @app.route("/query", strict_slashes=False)
# def handle_query1():
   # query_term = request.args.get("q")
   # query_n = int(request.args.get("p"))
   # return jsonify(query_on_whoosh.query_v2(query_term, query_n))
   