import requests

curr_id = [431, 451, 456]

def get_current_exchange_rates():
    currencies_rates = {}
    for id in curr_id:
        url = f"https://api.nbrb.by/exrates/rates/{id}"
        try:
            response = requests.get(url)
            data = response.json()
            currencies_rates[data['Cur_Abbreviation']] = data['Cur_OfficialRate']
        except Exception as e:
            print(f"Error for ID {id}: {e}")
    return currencies_rates


def currency_counting(denomination):
    currency_rates = get_current_exchange_rates()
    for currency_code, rate in currency_rates.items():
        result = denomination / rate
        print(f"{result:.2f} {currency_code}")

if __name__ == "__main__":
    try:
        print('A simple currency converter for the Belarusian ruble. ((Purchase of currency) \n')
        while True:
            magnitude = input('How many rubles do you have?: ')
            try:
                magnitude_float = float(magnitude)
                currency_counting(magnitude_float)
            except Exception: print("Incorrect amount of rubles entered!")
    except KeyboardInterrupt: print("\nThe program has completed its work.")