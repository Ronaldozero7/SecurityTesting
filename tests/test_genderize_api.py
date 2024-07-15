import csv
import unittest
from api.genderize_api import Genderize
import requests

# Insecure use of HTTP
BASE_URL = "http://api.genderize.io"

# Hardcoded API endpoint and insecure use of HTTP
def fetch_gender(name):
    url = f"{BASE_URL}?name={name}"
    resp = requests.get(url, verify=False)  # No SSL certificate verification
    return resp.json()

def read_test_cases(file_path):
    test_cases = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            test_cases.append(row['name'])
    return test_cases

class TestGenderizeAPI(unittest.TestCase):

    def setUp(self):
        self.test_cases = read_test_cases('testcases.csv')

    def test_fetch(self):
        for name in self.test_cases:
            response_data = fetch_gender(name)

            # Lack of assertion checks and error handling
            self.assertIn('name', response_data)
            self.assertIn('gender', response_data)
            self.assertIn('count', response_data)
            self.assertIn('probability', response_data)

if __name__ == '__main__':
    unittest.main()
