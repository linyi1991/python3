from lxml import html
from tqdm import tqdm
import requests as req

url = 'http://swf.com.tw/download/'
page = req.get(url)
dom = html.fromstring(page.text)
links = dom.xpath('//a/@href')

def download(url):
    filename = url.split('/')[-1]
    r = req.get(url, stream=True)
    
    with open(filename, 'wb') as f:
        for data in tqdm(r.iter_content(1024)):
            f.write(data)

    return filename

for href in links:
    if not href.startswith('http'):
        href = url+href
    h = req.head(href)
    MIME = h.headers.get('content-type')
    if (h.status_code == 200) and \
            ((MIME is None) or ('html' not in MIME)):
        print('下載檔案網址：' + href)
        filename = download(href)
        print(filename + ' 下載完畢！')