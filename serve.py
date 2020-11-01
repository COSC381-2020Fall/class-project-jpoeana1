from http.server import BaseHTTPRequestHandler, HTTPServer

class HTTPServer_RequestHandler(BaseHTTPRequestHandler):
    # handle the GET request from the browser
    # self: the instance of the class: HTTPServer_RequestHandler
    # self: is the web sever instance
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")

        #dynamically generates a webpage
        self.wfile.write(b"<!DOCTYPE html>");
        self.wfile.write(b"<html lang='en'>");
        self.wfile.write(b"<head>");
        self.wfile.write(b"<title>hello, title</title>");
        self.wfile.write(b"</head>");
        self.wfile.write(b"<body>");
        self.wfile.write(b"hello world");
        self.wfile.write(b"</body>");
        self.wfile.write(b"</html>");

port = 8080
server_address = ("0.0.0.0", port)
httpd = HTTPServer(server_address, HTTPServer_RequestHandler)
httpd.serve_forever()