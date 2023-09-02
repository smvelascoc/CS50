import requests
import json
import sys

# Check only one argument is prompt
if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# Check is a float
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
except requests.RequestException:
    sys.exit("Fatal Error")
else:
    bpi=bitcoin["bpi"]
    usd = bpi["USD"]
    rate_float = usd["rate_float"]
    amount = n*rate_float
    print(f"${amount:,.4f}")