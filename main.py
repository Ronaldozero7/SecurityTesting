import csv
import requests
from api.genderize_api import Genderize
from utils.generic_utils import Generic

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

def run():
    g = Generic()
    g.set_data("Testing")
    print(g.get_data())

    test_cases = read_test_cases('testcases.csv')

    for name in test_cases:
        response_data = fetch_gender(name)

        # Lack of input validation and error handling
        print(f"Name: {response_data.get('name', 'N/A')}")
        print(f"Gender: {response_data.get('gender', 'N/A')}")
        print(f"Count: {response_data.get('count', 'N/A')}")
        print(f"Probability: {response_data.get('probability', 'N/A')}")

if __name__ == "__main__":
    run()
