import requests
import json
from config import Backyard as by

class API:

    @staticmethod
    def get_price(base, quote, amount):
        res = requests.get(
            f'{by.URL}fsym={by.KEYS[quote][0]}&tsyms={by.KEYS[base][0]}')
        rate = json.loads(res.content)
        rate = rate[by.KEYS[base][0]]
        result = float(rate) * float(amount)
        return rate, result


class APIException(Exception):
    pass