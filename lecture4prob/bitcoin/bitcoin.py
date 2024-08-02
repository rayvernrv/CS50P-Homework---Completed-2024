import json
import sys
import requests

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    else:
        unit = sys.argv[1]
        units = float(unit)
except (requests.RequestException, ValueError):
    sys.exit("Command-line argument is not a number")

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
object = response.json()
rate = object["bpi"]["USD"]["rate_float"] #input key of dictionary to locate value
amount = units * float(rate)
print(f"${amount:,.4f}")

# print (json.dumps(response.json(),indent=2))
