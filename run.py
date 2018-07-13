##################################################################################################################
# Author: Belson
# This is a sample code to establish ticket authentication with EZproxy server
# More information here: 
# https://help.oclc.org/Library_Management/EZproxy/Authenticate_users/Authentication_methods/Ticket_authentication
##################################################################################################################

import os, hashlib, time, requests
from dotenv import load_dotenv, find_dotenv
from urllib.parse import urlparse, parse_qs

load_dotenv(find_dotenv())
timestamp = time.strftime("%Y%m%d%H%M%S")
packet = f"$c{timestamp}$g{os.getenv('GROUP')}$e"
ticket = hashlib.md5(f"{os.getenv('SECRET')}{os.getenv('USER')}{packet}".encode('utf-8')).hexdigest() + packet
request_url = f"{os.getenv('SERVER')}/login?user={os.getenv('USER')}&ticket={ticket}&qurl={os.getenv('URL')}"

print(f"visiting:\n{request_url}")
session = requests.session()
response = session.get(request_url)
print(f"Response URL: {response.url}")
print(f"Status Code:\n{response.status_code}")
print(f"Headers:\n{response.headers}")

# Retrieve session id
session_id = parse_qs(urlparse(response.history[-1].url).query)['session'][0]
print(f"Session id: {session_id}")

