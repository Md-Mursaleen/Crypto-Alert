from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def getEthPrice(symbol,outputCurrency):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
    'symbol':symbol,
    'convert':outputCurrency
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '04279dfc-5eda-4e6d-8426-0eaabf51ce0d',
    }
    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        return data['data']['ETH']['quote']['USD']['price']
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        return False