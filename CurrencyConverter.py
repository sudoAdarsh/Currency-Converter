import requests

def getinput():
    while True:
        try:
            amount = float(input("Enter the amount to convert: "))
            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                return amount
        except ValueError:
            print("Enter a valid number.")

from_currency = input("Enter source currency: ").strip().lower()
to_currency = input("Enter target currency: ").strip().lower()

def convert_currency(amount, from_currency, to_currency):
    api_data = requests.get(f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{from_currency}.json")
    if api_data.status_code == 200:
        data = api_data.json()
        try:
            rate = data[from_currency][to_currency]
            converted_amount = amount * rate
            return converted_amount
        except KeyError:
            print(f"Currency code '{to_currency}' not found for '{from_currency}'. Please check your input.")
            return None
    else:
        print("API request failed, please try again later!")

def main():
    amount = getinput()
    converted = convert_currency(amount, from_currency, to_currency)
    if converted is not None:
        print(f"\n{amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}")
    else:
        print("Conversion Failed!")

main()