# parsing the running config retrieved by netconf, from xml to a dictionary
# and retrieve the specific info, such as interface information

import xmltodict

xml_running_config = "01_get_iosxe_run_conf_output.xml"
with open(xml_running_config) as data:
    for i in range(3) : data.readline() # bypass top 3 non_xml lines 
    xml_example = data.read()

# print("type(xml_example):",type(xml_example))   # class str
# print(xml_example)
xml_dict = xmltodict.parse(xml_example) 
real_dict = xml_dict["rpc-reply"]["data"]["native"]
# print(type(dict(xml_dict)))   # dict
# print(type(dict(real_dict)))   # dict
# print(xml_dict) 

with open(xml_running_config + ".parsed.txt","w") as data1:
    data1.write(str(xml_dict))      # must convert to str, then write.  

def max_key_len(d):
   keylen = []
   for item in d:
      keylen.append(len(item))
   return max(keylen)

# print(intf0)
def pretty(d, indent=0):   # print dict in a nested way
   keyMaxLen = max_key_len(d)
   for key, value in d.items():
      print("  "*indent + "{:{}}".format(key,keyMaxLen), end="")
      if isinstance(value, dict):
         print()
         pretty(value, indent + 1)
      elif isinstance(value, list):
         print()
         for vlist in value : 
            pretty(vlist, indent+1) 
      else:
         print(" "*(indent+1) + str(value))

pretty(real_dict)