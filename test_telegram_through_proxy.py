# pip install -U requests[socks]
import requests

TOKEN = '600000000:AAEurdrttJQ6166HRMULceE4CvwAAAAAAAA'

URL = "https://api.telegram.org/bot{}/getupdates".format(TOKEN)

proxies = {
    'https': 'socks5://123.123.123.123:1080',
}

WITH_PROXY = True

if __name__ == '__main__':
    if WITH_PROXY:
        r = requests.get(URL, proxies=proxies)
    else:
        r = requests.get(URL)
    print(r.text)  # return {"ok":true,"result":[]} if success connects
