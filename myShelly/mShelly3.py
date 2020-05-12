import requests

url = 'https://shelly-4-eu.shelly.cloud/device/status'
myobj = {'id': '58EE34', 'auth_key':'MTU0M2Z1aWQECD1F8EBD5D95FCDD3EA3FD255BF3FF18AE0E49760F878480DEEA91B2B5C228B69494AEE79F2F4C3'}

x = requests.post(url, data = myobj)

print(x.text)