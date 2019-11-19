from mypkg.scc import Factory, SiteChecker
import sys, time

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