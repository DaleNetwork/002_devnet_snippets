import requests

#reference Docs: https://developer.cisco.com/meraki/api-v1/#!get-device

# Step1. Retrieves an organization's ID from Meraki dashboard API based on orgznization name
def get_org_id(url, headers, name):
    org_list = requests.get(url + '/api/v0/organizations', headers = headers).json() 
    for org in org_list:
        if org['name'] == name:
            return org['id']

# Step 2. retrieves organization inventory based on ID
def get_inventory(url, headers, org_id):
    inventory_list = requests.get(url + '/api/v0/organizations/' + org_id + '/inventory', 
                              headers = headers).json()
    return inventory_list

myheaders = { 'X-Cisco-Meraki-API-Key': "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"}
base_url = 'https://api.meraki.com'
org_name = 'DevNet Sandbox'

org_id = get_org_id(base_url, myheaders , org_name)

inventory_list = get_inventory(base_url, myheaders, org_id)

# Step 3. print out the inventory list and write it to a file named inventory_list.txt with
# one item per line

with open('inventory_list.txt', 'w') as f:
    for item in inventory_list:
        print(str(item))
        f.write(str(item))
        f.write('\n')