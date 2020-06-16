from tqdm import tqdm
import re
import requests as req
from selenium import webdriver

driver_path = "C:\\webdriver\\chromedriver.exe"
url = 'http://pybook.epizy.com/files/'

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(driver_path, options=option)
driver.implicitly_wait(10)  # 隱性等待，最長10秒

driver.get(url)
links = driver.find_elements_by_xpath('//a')

file_set = set()
pattern = re.compile(r'[\w]+.r(?:ar|\d{1,3})$')

def download(url):
    filename = url.split('/')[-1]
    r = req.get(url, stream=True)
    with open(filename, 'wb') as f:
        for data in tqdm(r.iter_content(1024)):
            f.write(data)

    return filename

for a in links:
    href = a.get_attribute("href")
    rar = pattern.search(href)

    if rar:
        file_set.add(rar.group())

for rar in file_set:
    link = url + rar
#     print(href)

    h = req.head(link)
    if h.status_code == 200:
        filename = download(link)
        print(filename + ' 檔案下載完畢！')

driver.quit()