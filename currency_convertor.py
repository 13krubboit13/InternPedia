import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

def get_exchange_rates():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()["rates"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rates: {e}")
        return None

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        print("Invalid currency code.")
        return None
    converted_amount = amount * (rates[to_currency] / rates[from_currency])
    return converted_amount

def main():
    rates = get_exchange_rates()
    if rates is None:
        print("Failed to retrieve exchange rates. Exiting the program.")
        return
    
    currencies = list(rates.keys())
    
    while True:
        print("\nAvailable currencies:", ", ".join(currencies))
        from_currency = input("Enter the source currency code: ").upper()
        to_currency = input("Enter the target currency code: ").upper()
        
        try:
            amount = float(input(f"Enter the amount to convert from {from_currency} to {to_currency}: "))
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            continue
        
        converted_amount = convert_currency(amount, from_currency, to_currency, rates)
        
        if converted_amount is not None:
            print(f"{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")
        
        if input("Do you want to perform another conversion? (y/n): ").lower() != 'y':
            print("Thank you for using the Currency Converter. Goodbye!")
            break

if __name__ == "__main__":
    main()
