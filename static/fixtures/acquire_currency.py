import copy
import requests
from bs4 import BeautifulSoup
import json

header = {
    'cookies': 'utag_main=v_id:018747b6bb99006fb797c02748600506f003006700838$_sn:1$_ss:0$_st:1680538593028$ses_id:1680535370651%3Bexp-session$_pn:5%3Bexp-session',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
}

url = 'https://www.x-rates.com/table/?from=GBP&amount=1'
res = requests.get(url=url, headers=header)
soup = BeautifulSoup(res.text, "html.parser")
result = soup.find("tbody")
data = [{"model": "payapp.currency", "fields": {"symbol": "GBP", "country": "Great Britches", "rate": 1.00000}}]

for i, tags in enumerate(result.find_all('tr')):
    if i < 9:
        rate_tag = tags.find_next('a')
        temp = copy.deepcopy(data[0])
        print(data)
        temp['fields']['symbol'] = rate_tag.get("href").split('&to=')[1]
        temp['fields']['rate'] = float(rate_tag.text)
        temp['fields']['country'] = tags.select_one('td').text
        data.append(temp)

with open('currency.json', 'w') as f:
    json.dump(data, f)
