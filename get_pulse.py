import requests

# API key for authentication
api_key = ''
headers = {'X-OTX-API-KEY': api_key}

# URL for the search endpoint
search_term = 'APT 29'
url = f'https://otx.alienvault.com/api/v1/search/pulses?q={search_term}'

response = requests.get(url, headers=headers)
search_results = response.json()

# Print pulse names and IDs
for result in search_results.get('results', []):
    print(f"Pulse Name: {result.get('name')} - Pulse ID: {result.get('id')}")
