import requests

base_url = 'https://sandbox-nso-1.cisco.com'
username = 'developer'
password = 'Services4Ever'

# Use self signed certs
requests.packages.urllib3.disable_warnings()

# Reference the always on NSO sandbox
# https://devnetsandbox.cisco.com/RM/Diagram/Index/aa07cf66-b756-4424-99c1-4a93aa42c913?diagramType=Topology

# Reference the API Docs
# https://developer.cisco.com/docs/nso/#!single-device-config

nso_url = '/restconf/data/tailf-ncs:devices/device='

# Reference the project '01_get_devices, to get device's name
# the 5 devices' name are  "core-rtr01", "dist-sw01", "dist-rtr02", "dist-rtr01", "core-rtr02"

device_name = 'dist-sw01'
get_config_url = base_url + nso_url + device_name

payload = None
headers = { "Accept": "application/yang-data+json" }

response = requests.request('GET', get_config_url, 
                            headers = headers, 
                            auth = (username, password),
                            verify = False)

# print(response.encoding)
print(response.text)