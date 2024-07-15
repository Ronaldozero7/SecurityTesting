import requests
from Config.config import BASE_URL

class Genderize:
    def __init__(self, nme):
        self.url = f"{BASE_URL}?name={nme}"
        self.resp = None

    def fetch(self):
        self.resp = requests.get(self.url)

    def get_gender(self):
        return self.resp.json()['gender']

    def get_count(self):
        return self.resp.json()['count']

    def get_probability(self):
        return self.resp.json()['probability']
