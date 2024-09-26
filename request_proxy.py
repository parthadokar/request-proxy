import requests

def get_tor_session():
    session = requests.session()
    # Use socks5h for Tor
    session.proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    return session

# Print your normal public IP address
print('Normal Public IP:', requests.get("http://httpbin.org/ip").text)

# Make a request through the Tor connection
session = get_tor_session()
print("IP for Tor connection:", session.get("http://httpbin.org/ip").text)

try:
    # Any Onion website
    response = session.get('https://www.facebookwwwi.onion')  # Corrected URL
    print("Response Headers:")
    for key, value in response.headers.items():
        print(key, value)
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
