import sys
import requests
import json
import socket
if len(sys.argv) <2:
	print("Usage: " + sys.argv[0] + "<url>")
	sys.exit(1)
req = requests.get("https://"+sys.argv[1])
print("\n"+str(req.headers))
gethostby_ = socket.gethostbyname(sys.argv[1])
print("\nThe IP address of " + sys.argv[1] + " is: " + gethostby_ + "\n")
#ipinfo.io
req_two = requests.get("https://ipinfo.io/"+gethostby_+"/json")
resp_json.loads(req_two.text) # type: ignore
print("Location: "+resp_["loc"])
print("Region: "+resp_["region"])
print("City: "+resp_["city"])
print("Country: "+resp_["country"])
