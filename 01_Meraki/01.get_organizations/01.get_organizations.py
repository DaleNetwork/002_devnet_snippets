import requests
import json
url="https://api.meraki.com/api/v1/organizations"

# dotnet reality ap serial "Q2GD-U5PN-BFUL"
url = 'https://api.meraki.com/api/v1/devices/Q2GD-U5PN-BFUL'

payload = None
Demokey = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
dnrkey = input("What is the dotnet reality's API Key?")
if dnrkey =="":
    APIKey = Demokey
else:
    APIKey = dnrkey

headers = { "Content-Type": "applications/json",
            "Accept": "applications/json",
            "X-Cisco-Meraki-API-key": APIKey
        }

response = requests.request("GET", url, headers = headers, data = payload)

parsed_response = json.loads(response.text.encode("utf8")) # [list][dict]
pretty_response = json.dumps(parsed_response, indent = 4)  # str

print("response:", response)   # <Response [200]>
print("type(response.text.uncode('utf8'):",type(response.text.encode("utf8")))   
    # output <class 'bytes'>
print("type(parsed_response):",type(parsed_response)) # <class 'list>
print("type(pretty_response):",type(pretty_response)) # <class 'str'>
print("type(parsed_response[1]:",type(parsed_response[0])) # <class 'dict'>

print(len(parsed_response))
# print(parsed_response)
# for i in range(len(parsed_response)):
#     print(i+1, parsed_response[i]["name"])
print(pretty_response)