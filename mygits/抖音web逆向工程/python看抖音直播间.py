import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

url = 'https://live.douyin.com/72737528171?column_type=single&is_amemee_tied=0&search_id=20240711224941F710BC70FC72F760A&search_result_id=7490315150525111305'

resp = requests.get(url, headers=headers)
if resp.status_code == 200:
    html = resp.text
    print(html)
else:
    print(f"请求失败，状态码: {resp.status_code}")