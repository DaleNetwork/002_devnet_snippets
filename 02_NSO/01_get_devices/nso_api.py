import requests 
import json
import pprint

base_url="https://sandbox-nso-1.cisco.com"
username = 'developer'
password = 'Services4Ever'

# Reference the API Docs
# https://developer.cisco.com/docs/nso/#!cisco-nso-restconf-swagger-api-docs-overview

# Reference the always on NSO sandbox
# https://devnetsandbox.cisco.com/RM/Diagram/Index/aa07cf66-b756-4424-99c1-4a93aa42c913?diagramType=Topology

get_device_url = base_url + '/restconf/data/tailf-ncs:devices/device'

headers = { 'Content-Type': 'application/yang-data+json' }
# this is a YANG model based url, not regular json
# compare with DNA, where we used 'Content-Type: application/json' 

# Use self signed certs
requests.packages.urllib3.disable_warnings()

response = requests.get(get_device_url,
                    auth = (username, password),
                    headers = headers,
                    verify = False)

# print(response.encoding)   # output: none

print(response.text)