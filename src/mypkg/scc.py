import sys
import socket
import argparse
import re
import time

class Factory():
    def create_parser(args):
        parser = argparse.ArgumentParser(prog= "python3 scc.py 'www.example.com'",
                                         description="Site-Connectivity-Checker")
        parser.add_argument("-hn", dest="host_name",
                                   action="store", 
                                   help="python3 scc.py ['host name']")
        parser.add_argument("-debug", dest="debug", 
                                      action="store_true", 
                                      help="debug mode")
        parser.add_argument("-save", dest="save_file", 
                                     action="store_true", 
                                     help="save HTTP header file")
        parser.add_argument("-buffer", dest="buffer_size", 
                                       action="store", 
                                       help="set buffer size to store http header and body")

        return parser

class SiteChecker():
    def __init__(self, args):
        # Get data
        # self.args = parser.parse_args()
        self.args = args
        self.any_error = False
    
        print("Connecting to: ", self.args.host_name)
        self.port = 80

        if not self.args.buffer_size:
            self.args.buffer_size = 20

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                # s.connect(("www.www", self.port))
                s.connect((self.args.host_name, 80))
            except socket.gaierror:
                print("[ERROR]socket.gaierror: Please enter a correct URL! \n \
                    if you confirm the URL is correct, just ignore the error log.\n \
                    Wait until the site response.")
                self.any_error = True
                s.connect(('', self.port))
            except:
                print("Unexpected error:", sys.exc_info()[0])
                self.any_error = True
                s.connect(('', self.port))
                raise
            s.sendall(b"GET / HTTP/1.0\r\n\r\n")
            data = s.recv(int(self.args.buffer_size))

        self.data = data.decode('utf-8')

    def scc(self):
        if self.any_error:
            return "Check error log."
        match_obj = re.match(r"^(HTTP\/1...)([0-9][0-9][0-9]{1})", self.data)
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
    print(sys.argv)
    while True:
        parser = Factory().create_parser()
        args = parser.parse_args()
        checker = SiteChecker(args)
        res = checker.scc()
        print(res)
        debug = checker.scc_debug()
        if debug:
            print(debug)
        if res == "200 OK":
            break
        time.sleep(2)
