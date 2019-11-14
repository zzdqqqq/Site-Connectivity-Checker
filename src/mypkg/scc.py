import socket
import argparse
import re
import time

class Factory():
    def create_parser(args):
        parser = argparse.ArgumentParser(prog= "python3 scc.py 'www.example.com'", description="Site-Connectivity-Checker")
        parser.add_argument("-hn", dest="host_name", action="store", help="python3 scc.py ['host name']")
        parser.add_argument("-debug", dest="debug", action="store_true", help="debug mode")
        parser.add_argument("-save", dest="save_file", action="store_true", help="save HTTP header file")
        parser.add_argument("-buffer", dest="buffer_size", action="store", help="set buffer size to store http header and body")

        return parser

class SiteChecker():
    def __init__(self, args):
        # Get data
        # self.args = parser.parse_args()
        self.args = args
    
        print("Connecting to: ", self.args.host_name)
        self.port = 80

        if not self.args.buffer_size:
            self.args.buffer_size = 20

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.args.host_name, 80))
            s.sendall(b"GET / HTTP/1.0\r\n\r\n")
            data = s.recv(int(self.args.buffer_size))

        self.data = data.decode('utf-8')

    def scc(self):
        match_obj = re.match(r"^(HTTP/1...)([0-9][0-9][0-9]{1})", self.data)
        if match_obj:
            if match_obj.group(2) == '200':
                # print("200 OK")
                return "200 OK"
            elif match_obj.group(2) == '500':
                return "500 Internal Server Error"
            else:
                return "NOT OK"

    def scc_debug(self):
            if self.args.save_file:
                with open("http_data.txt", "w+") as f:
                    f.write(self.data)

            if self.args.debug:
                return self.data

if __name__ == "__main__":
    # Do some test

    parser = Factory().create_parser()
    args = parser.parse_args()
    checker = SiteChecker(args)
    print(checker.scc())
    debug = checker.scc_debug()
    if debug:
        print(debug)