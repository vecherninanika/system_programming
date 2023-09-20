import requests
import json

cookies = {
    'i': '5MQ/dvc8lJiTUhizhaNvkLA7Pc9TyxemvqqD7OZtz/wIwwJ0+koHfADIDFsQgVdhfzDY8W6FN3fm9G1VBpvHMubqE90=',
    'yandexuid': '4111589471680802558',
    'yuidss': '4111589471680802558',
    'ymex': '1996162558.yrts.1680802558#1996162558.yrtsi.1680802558',
    'is_gdpr': '0',
    '_ym_uid': '1667992982404139470',
    '_ym_d': '1680870271',
    'L': 'U0FzfX1dVARtVABwcWVYVAVJC251eGddDF9YMRMR.1680976032.15306.341064.5feab964486208ad5497b940c4a70f96',
    'yandex_login': 'dilera',
    'gdpr': '0',
    'is_gdpr_b': 'COjOQRDaswEoAg==',
    'skid': '2819724831687020380',
    'yp': '1996336032.udn.cDpkaWxlcmE%3D#1694431269.szm.1:1920x1080:1846x948',
    'device_id': 'a0b7f1eede9fb33720adbc3f88eb5ffe7dfbc9359',
    'Session_id': '3:1695222888.5.0.1680976032111:IqT5VQ:1a.1.2:1|8967484.0.2.3:1680976032|3:10276035.86994.JVMAIcP5dlcioSAlI7_Q4FymNQc',
    'sessar': '1.1182.CiDDFACizj0izw6zgZexqGjgluEZrc4YHwBlUelukRzuUA.zdZJ83lYj8juTPHBiV58R_ATrAXTsLZSyV7d-NWaKns',
    'sessionid2': '3:1695222888.5.0.1680976032111:IqT5VQ:1a.1.2:1|8967484.0.2.3:1680976032|3:10276035.86994.fakesign0000000000000000000',
    'chromecast': "''",
    'lastVisitedPage': '%7B%7D',
    '_ym_isad': '1',
    'active-browser-timestamp': '1695231343981',
    '_ym_visorc': 'b',
    '_yasc': 'SAiNo15hEMsQ4VKVXgwvHbRUrRmcGZAUPDHn2VFhHb7DJIV8kJeMejkncm81rmk10UfPBbY=',
    'bh': 'EkEiQ2hyb21pdW0iO3Y9IjExMCIsICJOb3QgQShCcmFuZCI7dj0iMjQiLCAiR29vZ2xlIENocm9tZSI7dj0iMTEwIhoFIng4NiIiECIxMTAuMC41NDgxLjE3NyIqAj8wOgciTGludXgiQggiNS4xOS4wIkoEIjY0IlJcIkNocm9taXVtIjt2PSIxMTAuMC41NDgxLjE3NyIsIk5vdCBBKEJyYW5kIjt2PSIyNC4wLjAuMCIsIkdvb2dsZSBDaHJvbWUiO3Y9IjExMC4wLjU0ODEuMTc3IiI=',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    # 'Cookie': "i=5MQ/dvc8lJiTUhizhaNvkLA7Pc9TyxemvqqD7OZtz/wIwwJ0+koHfADIDFsQgVdhfzDY8W6FN3fm9G1VBpvHMubqE90=; yandexuid=4111589471680802558; yuidss=4111589471680802558; ymex=1996162558.yrts.1680802558#1996162558.yrtsi.1680802558; is_gdpr=0; _ym_uid=1667992982404139470; _ym_d=1680870271; L=U0FzfX1dVARtVABwcWVYVAVJC251eGddDF9YMRMR.1680976032.15306.341064.5feab964486208ad5497b940c4a70f96; yandex_login=dilera; gdpr=0; is_gdpr_b=COjOQRDaswEoAg==; skid=2819724831687020380; yp=1996336032.udn.cDpkaWxlcmE%3D#1694431269.szm.1:1920x1080:1846x948; device_id=a0b7f1eede9fb33720adbc3f88eb5ffe7dfbc9359; Session_id=3:1695222888.5.0.1680976032111:IqT5VQ:1a.1.2:1|8967484.0.2.3:1680976032|3:10276035.86994.JVMAIcP5dlcioSAlI7_Q4FymNQc; sessar=1.1182.CiDDFACizj0izw6zgZexqGjgluEZrc4YHwBlUelukRzuUA.zdZJ83lYj8juTPHBiV58R_ATrAXTsLZSyV7d-NWaKns; sessionid2=3:1695222888.5.0.1680976032111:IqT5VQ:1a.1.2:1|8967484.0.2.3:1680976032|3:10276035.86994.fakesign0000000000000000000; chromecast=''; lastVisitedPage=%7B%7D; _ym_isad=1; active-browser-timestamp=1695231343981; _ym_visorc=b; _yasc=SAiNo15hEMsQ4VKVXgwvHbRUrRmcGZAUPDHn2VFhHb7DJIV8kJeMejkncm81rmk10UfPBbY=; bh=EkEiQ2hyb21pdW0iO3Y9IjExMCIsICJOb3QgQShCcmFuZCI7dj0iMjQiLCAiR29vZ2xlIENocm9tZSI7dj0iMTEwIhoFIng4NiIiECIxMTAuMC41NDgxLjE3NyIqAj8wOgciTGludXgiQggiNS4xOS4wIkoEIjY0IlJcIkNocm9taXVtIjt2PSIxMTAuMC41NDgxLjE3NyIsIk5vdCBBKEJyYW5kIjt2PSIyNC4wLjAuMCIsIkdvb2dsZSBDaHJvbWUiO3Y9IjExMC4wLjU0ODEuMTc3IiI=",
    'Referer': 'https://music.yandex.ru/chart',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36',
    'X-Current-UID': '8967484',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Retpath-Y': 'https://music.yandex.ru/chart',
    'X-Yandex-Music-Client-Now': '2023-09-20T20:47:34+03:00',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

params = {
    'what': 'chart',
    'lang': 'ru',
    'external-domain': 'music.yandex.ru',
    'overembed': 'false',
    'ncrnd': '0.6865978660865513',
}

response = requests.get('https://music.yandex.ru/handlers/main.jsx', params=params, cookies=cookies, headers=headers)
data = response.json()['chartPositions']
dct = {}
for item in data:
    track = item['track']
    dct[track['chart']['position']] = {track['title']: [artist['name'] for artist in track['artists']]}
print(dct)

with open("data.json", "w") as f:
    json.dump(dct, f, ensure_ascii=False)