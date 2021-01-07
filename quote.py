import requests
import json
from random import randint


class Quote:
    def give(self):
        random_key = randint(1, 10**6)
        params = {
            'method': 'getQuote',
            'format': 'json',
            'lang': 'ru',
            'key': str(random_key)
        }
        url = 'http://api.forismatic.com/api/1.0/'
        json_answer = requests.get(url, params)
        dictionary = json.loads(json_answer.text)
        return dictionary


if __name__ == '__main__':
    result = Quote().give()
    print(result)
