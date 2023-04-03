import requests

header = {
    'cookies': 'utag_main=v_id:018747b6bb99006fb797c02748600506f003006700838$_sn:1$_ss:0$_st:1680538593028$ses_id:1680535370651%3Bexp-session$_pn:5%3Bexp-session',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
}

url = 'https://www.x-rates.com/table/?from=GBP&amount=1'

res = requests.get(url=url, headers=header)
print(res)


