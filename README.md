# ezproxy-ticket

This script was developed by Belson Heng in Python to show how to authenticate with OCLC's EZProxy via ticket authentication. There's no license to this, so feel free to use it as long as it doesn't break stuff :)

## Getting Started 

Update ```.env``` file with your own settings. The SECRET key should be similar to the one used by your EZproxy server. GROUP is an optional field, but it indicates the user group. SERVER should point to your EZproxy server location. USER is required so that proxy logs can record the user access. URL refers to the subscribed electronic resource databases (e.g. sciencedirect.com).

```
SECRET=...
GROUP=""
SERVER="https://yourproxyserver.com"
USER="youruserid"
URL="https://www.sciencedirect.com"
```

To run, simply execute the following command:
```
python run.py
```
