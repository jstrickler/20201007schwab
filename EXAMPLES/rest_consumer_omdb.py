import requests
from pprint import pprint

with open('omdbapikey.txt') as api_in:
    OMDB_API_KEY = api_in.read().rstrip()

OMDB_URL = "http://www.omdbapi.com"

def main():
    requests_params = {'t': 'Black Panther', "apikey": OMDB_API_KEY}
    request_headers = {'auth': ('my_id', 'my_apikey')}
    response = requests.get(OMDB_URL, params=requests_params) 
    # ,headers=request_headers)
    if response.ok: #  status_code == requests.codes.OK:
        raw_data = response.json()  # parse response.content into Python data

        print(f"raw_data['Title']: {raw_data['Title']}")
        print(f"raw_data['Director']: {raw_data['Director']}")
        print(f"raw_data['Year']: {raw_data['Year']}")
        print(f"raw_data['Runtime']: {raw_data['Runtime']}")
        print()

        print('-' * 60)
        print("raw JSON:")
        pprint(response.content.decode())
        print('-' * 60)
        
        print("raw DATA:")
        pprint(response.json(), sort_dicts=False)
    else:
        print(f"response.status_code: {response.status_code}")

if __name__ == '__main__':
    main()
