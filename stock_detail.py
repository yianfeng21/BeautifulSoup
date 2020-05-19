# $ pip install requests
# $ pip install beautifulsoup4
# $ pip install lxml

import requests
from bs4 import BeautifulSoup

def get_web_page(stock_id):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                             'AppleWebKit/537.36 (KHTML, like Gecko)'
                             'Chrome/66.0.3359.181 Safari/537.36'}
    payload = {'q': stock_id}
    resp = requests.get("https://www.google.com/search", params=payload, headers=headers)  # resp=response
    # resp.encoding = 'utf-8'
    print('查詢網頁：',resp.url)
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text

def get_stock_info(dom):
    soup = BeautifulSoup(dom, 'lxml')  # soup = BeautifulSoup(response.text, 'lxml')
    # print(soup.prettify())  # 排版後的html印出來
    stock = dict()
    sections = soup.find_all('g-card-section')

# 第2個 g-card-section，取出公司名及即時股價資訊
    divs = sections[1].find_all('div', recursive=False)
    stock['Name：'] = divs[0].text
    stock['Status：'] = divs[1].text
    spans = sections[1].find_all('span', recursive=False)
    stock['Current_price：'] = spans[0].text
    stock['Current_change：'] = spans[1].text

# 第4個 g-card-section，有左右兩個table分別存放股票資訊
    for table in sections[3].find_all('table'):
        for tr in table.find_all('tr')[:5]:
            key = tr.find_all('td')[0].text.lower().strip()
            value = tr.find_all('td')[1].text.strip()
            stock[key] = value
        return stock

if __name__ == '__main__':
    page = get_web_page('TPE: '+'2330')
    if page:
        stock = get_stock_info(page)
        print(stock["Current_price："])
        # for k, v in stock.items():
            # print(k, v)