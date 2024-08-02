#API = Application Programming Interface
#3rd party service, write Python code to talk to and get information on a server to use in your own program
#pip install requests
#JSON = JavaScript Object Notation, language agnostic format, for exchanging data.
#JSON = In text format, that can be read and write in any language for your own program. convert to your own langugae

import json #python library, allow you to manipulate JSON data
import requests #pip
import sys

if len (sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1])
# print (json.dumps(response.json(),indent=2)) #print everything in API

o = response.json()
for result in o["results"]:
    print (result["trackName"]) #forloop to retrieve specifically under key: results + trackName
