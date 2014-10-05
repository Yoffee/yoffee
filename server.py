from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

PORT = 80

coffee_waiting = False


class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.wfile.write(self.version_string())
        self.end_headers()
        if self.command == 'GET':
            if self.headers.get_param("username") is not None:
                print("Yo Recieved")
                coffee_waiting = True
            elif self.path == "index":
                if coffee_waiting:
                    self.wfile.write("1")
                    coffee_waiting = False
                else:
                    self.wfile.write("0")


server = HTTPServer(('', PORT), myHandler)
server.serve_forever()
