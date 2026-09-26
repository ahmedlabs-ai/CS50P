import sys
import requests
try:

    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    amount = float(sys.argv[1])
    response = requests.get(
    "https://rest.coincap.io/v3/assets/bitcoin",
    headers={"Authorization": "Bearer 6469d707e39172f17a845416a72bed4868e25102a0c52fc6b758a710f22ecdba"}
)
    print(f"${float(response.json()['data']['priceUsd']) * amount:,.4f}")

except ValueError:
      sys.exit("Command-line argument is not a number")
