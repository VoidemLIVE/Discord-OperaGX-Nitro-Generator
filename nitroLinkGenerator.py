import requests
import time

repeater = int(input("How many links do you want to generate? "))

for i in range(repeater):
    url = 'https://api.discord.gx.games/v1/direct-fulfillment'
    headers = {
        'authority': 'api.discord.gx.games',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'origin': 'https://www.opera.com',
        'referer': 'https://www.opera.com/',
        'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36',
    }

    data = {
        'partnerUserId': 'eeedb8905668a310ae1b0f4bf058bfbe53af33463a6ca9c1c91fdb309960f7a6',
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        json_response = response.json()
        token = json_response.get('token')
        appender = "https://discord.com/billing/partner-promotions/1180231712274387115/" + token
        with open('links.txt', 'a') as file:
            file.write(appender + '\n')
            time.sleep(0.5)
    else:
        print("Error:", response.status_code, response.text)
