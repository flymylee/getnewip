import json
import requests
import os
import sys
import platform

"""
Get New Public IP
"""

# Function for Getting the abstact path of input file name input.
def getabspath(input):
	if platform.system() == "Windows":
		separtor = '\\'
	else:
		separtor = '/'

	if input.find(separtor) == -1:
		return os.path.abspath(os.path.curdir) + separtor + input
	else:
		return input

# Showing the usage of this application.
def usage():
	print('\x1b[1;31;47m' + "Getting Public IP" + " \x1b[0m" + '\n')
	print("getnewip " + '\x1b[1;32m' + "--json [PATH]FILENAME" + '\x1b[0m')
	print("getnewip " + '\x1b[1;33m' + "--skeleton" + '\x1b[0m')

# Getting Public IP
public_ip = requests.get("https://api.ipify.org/").text

# Update Public IP in the batch file for AWS Route53 DDNS
if len(sys.argv) == 1:
	usage()

elif sys.argv[1] == "--json":
	filename = sys.argv[2]
	path = getabspath(filename)

	if os.path.exists(path) == False:
		print("File not exists!")

	else:
		try:
			with open(path, 'r') as f:
				data = json.load(f)
				data["Changes"][0]["ResourceRecordSet"]["ResourceRecords"][0]["Value"] = public_ip

		except OSError as err:
			print("File not exists!\n")

		# Delete the original file and then write down the updated
		os.remove(path)
		with open(path, 'w') as f:
			json.dump(data, f, indent=2)

	print("Done!")

# Generate a snippet has the basic structure of a JSON template
elif sys.argv[1] == "--skeleton":
	with open("skeleton.json", 'w') as f:

		skeleton = {
			"Comment": "",
			"Changes": [
				{
					"Action": "[CREATE|DELETE|UPSERT]",
					"ResourceRecordSet": {
						"Name": "",
						"Type": "[A|TXT|MX]",
						"TTL": 0,
						"ResourceRecords": [
							{
							"Value": ""
							}
						]
					}
				}
			]
		}

		json.dump(skeleton, f, indent=2)

	print("Done!")

else:
	print("Invalid Command!\n")
	usage()