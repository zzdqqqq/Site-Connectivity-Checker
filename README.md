# Site Connectivity Checker (command line tool)
## Motivation
When you visit a URL, you expect to get the requested pages on your browser. But this is not always the case. Sometimes, sites can be down, so you won’t get the desired results. You can keep trying until it comes up.

This project build a command line tool to automatically do this work.

## TODO
- [ ] Conenct to a website by TCP protocol (Compared to ICMP TCP can get more information)
- [ ] According to the status codes, return true or false (or some other status)
- [ ] Run this command in background using "systemd". When the site response, send a alert.

