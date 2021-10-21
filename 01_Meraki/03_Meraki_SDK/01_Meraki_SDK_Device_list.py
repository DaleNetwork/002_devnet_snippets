import meraki

api_key = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
url = "https://dashboard.meraki.com"
org_name = "DevNet Sandbox"

# this is old format from eric chou
# dashboard = meraki.DashboardAPI(
#     api_key = api_key,
#     base_url = url +"api/v1",
#     output_log = False, 
#     print_console = False
# )

# new format from: 
# https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-devices
dashboard = meraki.DashboardAPI(api_key)

organization_id = '549236'      # this id is for "DevNet Sandbox"


response = dashboard.organizations.getOrganizationInventoryDevices(
    organization_id, total_pages='all'
)
# the call will display some return info on the stdio

print("="*50)

for item in response:   print(item)

print("="*50)
print(response)