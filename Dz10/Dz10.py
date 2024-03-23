import requests


def currency_converter(amount, from_currency, to_currency):

    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            exchange_rate = data['rates'][to_currency]
            converted_amount = amount * exchange_rate
            return converted_amount
        else:
            print("Failed to fetch exchange rates. Please try again later.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


amount1 = float(input("Введіть суму яку хочете конвертувати в долари: "))
from_currency1 = "UAH"
to_currency1 = "USD"

converted_amount = currency_converter(amount1, from_currency1, to_currency1)
if converted_amount is not None:
    print(f"{amount1} {from_currency1} дорівнює {converted_amount} {to_currency1}")
