import requests

# API key for authentication
api_key = ''
headers = {'X-OTX-API-KEY': api_key}

# Endpoint to get IoCs from a specific pulse
pulse_id = '56a790f74637f23550f3c093'
url = f'https://otx.alienvault.com/api/v1/pulses/{pulse_id}'

response = requests.get(url, headers=headers)
pulse_data = response.json()

# Print basic information about the pulse
print(f"Pulse Name: {pulse_data.get('name')}")
print(f"Description: {pulse_data.get('description')}")
print("Indicators of Compromise (IoCs):")

# Extracting IoCs
iocs = pulse_data.get('indicators', [])
for ioc in iocs:
    print(f"Indicator: {ioc['indicator']} - Type: {ioc['type']} - Description: {ioc.get('description', 'No description provided')}")
