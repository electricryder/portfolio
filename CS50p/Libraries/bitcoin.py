import sys
import requests
import json


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        usd_quant = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    try:
        resp = requests.get(
            "http://rest.coincap.io/v3/assets/bitcoin?apiKey=978a88857a6c36984049529f10a6dc27804174aa470b365b9604ed8b7ce276e6"
        )
    except requests.RequestException:
        sys.exit("API request error")

    cont = resp.json()

    # Not used for the final result, but helpful in the process for better visualization
    # cont_indented = json.dumps(cont, indent= 2)
 
    try:
        bitcoin_usd_rate = float(cont["data"]["priceUsd"])
    except ValueError:
        sys.exit("Invalid value")

    price_usd = bitcoin_usd_rate * usd_quant

    print(f"${price_usd:,.4f}")


if __name__ == "__main__":
    main()
