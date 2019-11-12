import socket
import argparse
import re
import time

parser = argparse.ArgumentParser(prog= "python3 main.py 'www.example.com'", description="Site-Connectivity-Checker")
parser.add_argument("-hn", dest="host_name", action="store", help="python3 scc.py ['host name']")
parser.add_argument("-debug", dest="debug", action="store_true", help="debug mode")
parser.add_argument("-save", dest="save_file", action="store_true", help="save HTTP header file")
parser.add_argument("-buffer", dest="buffer_size", action="store", help="set buffer size to store http header and body")

args = parser.parse_args()
print("Connecting to: ", args.host_name)
port = 80

if not args.buffer_size:
    args.buffer_size = 20
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((args.host_name, 80))
        s.sendall(b"GET / HTTP/1.0\r\n\r\n")
        data = s.recv(int(args.buffer_size))

    data = data.decode('utf-8')
    if args.debug:
        print(data, "\n")

    if args.save_file:
        with open("http_data.txt", "w+") as f:
            f.write(data)

    match_obj = re.match(r"^(HTTP/1...)([0-9][0-9][0-9]{1})", data)
    if match_obj:
        if match_obj.group(2) == '200':
            print("200 OK")
            break
        elif match_obj.group(2) == '500':
            print("500 Internal Server Error")
        else:
            print("NOT OK")
    time.sleep(2)

# TODO
if __name__ == "__main__":
    # Do some test
    pass