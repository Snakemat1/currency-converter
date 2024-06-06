import requests

def get_exchange_rates(api_key):
    url = f"http://api.exchangeratesapi.io/v1/latest?access_key={api_key}"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200:
        raise Exception(f"Error fetching data from API: {data.get('error', 'Unknown error')}")
    return data['rates']

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        raise ValueError("Invalid currency code")
    if from_currency != 'EUR':
        amount = amount / rates[from_currency]
    return amount * rates[to_currency]

def main():
    api_key = 'b46a582992a8da7ac186d897c26bc2a3'  # Вставьте свой API ключ
    rates = get_exchange_rates(api_key)

    try:
        amount = float(input("Введите сумму для конвертации: "))
        from_currency = input("Из какой валюты: ").upper()
        to_currency = input("В какую валюту: ").upper()

        converted_amount = convert_currency(amount, from_currency, to_currency, rates)
        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    except ValueError as ve:
        print(f"Ошибка ввода данных: {ve}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
