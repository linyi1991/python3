# 參閱11-7頁

import requests as req
from tqdm import tqdm

url = 'http://swf.com.tw/scrap/img/IR.png'


def download(url):
    filename = url.split('/')[-1]
    r = req.get(url, stream=True)

    # with open(filename, 'wb') as f:
    #     for data in r.iter_content(1024):
    #         f.write(data)

    with open(filename, 'wb') as f:
        for data in tqdm(r.iter_content(1024)):
            f.write(data)

    return filename


download(url)
