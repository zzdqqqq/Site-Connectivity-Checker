import socket
import argparse
import re
import time

parser = argparse.ArgumentParser(prog= "python3 main.py 'www.example.com'", description="Site-Connectivity-Checker")
parser.add_argument("host_name", help="python3 main.py ['host name']")

args = parser.parse_args()
print("Connecting to: ", args.host_name)
port = 80

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((args.host_name, 80))
        s.sendall(b"GET / HTTP/1.1\r\n\r\n")
        data = s.recv(512)

    data = data.decode('ASCII')
    print(data)

    # with open("http_data.txt", "w+") as f:
    #     f.write(data)
    # with open("http_data.txt", "r") as f:
    #     first_line = f.readline()

    match_obj = re.match(r"^(HTTP/1.1.)([0-9][0-9][0-9]{1})", data)
    if match_obj:
        if match_obj.group(2) == '200':
            print("200 OK")
            break
        elif match_obj.group(2) == '500':
            print("500 Internal Server Error")
        else:
            print("NOT OK")
    time.sleep(2)