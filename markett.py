import requests
from bs4 import BeautifulSoup

def convert_price(price_str):
    price_str = price_str.replace(',', '')  # حذف
    if 'B' in price_str:
        price = float(price_str.replace('B', '')) * 1_000_000_000 
    elif 'M' in price_str:
        price = float(price_str.replace('M', '')) * 1_000_000
    elif 'K' in price_str:
        price = float(price_str.replace('K', '')) * 1_000  
    else:
        price = float(price_str)
    return price

def get_top_coins_price(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        prices = []
        for i, row in enumerate(soup.find_all('tr', {'class': 'cmc-table-row'})):
            if i < 10:
                price_str = row.find('td', {'class': 'cmc-table__cell--sort-by__price'}).text.strip()
                price = convert_price(price_str)
                prices.append(price)
        return prices
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

coin_market_url = 'https://coinmarketcap.com/'
coin_ranking_url = 'https://coinranking.com/'

print("Coin Market Prices:")
cmc_prices = get_top_coins_price(coin_market_url)
if cmc_prices:
    print(cmc_prices)

print("\nCoin Ranking Prices:")
cr_prices = get_top_coins_price(coin_ranking_url)
if cr_prices:
    print(cr_prices)