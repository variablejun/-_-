import urllib.request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time
SCROLL_PAUSE_SEC = 1
def scroll_down():
     global driver
     last_height = driver.execute_script("return document.body.scrollHeight")

     while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_SEC)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            time.sleep(SCROLL_PAUSE_SEC)
            new_height = driver.execute_script("return document.body.scrollHeight")

            try:
                driver.find_element_by_class_name("mye4qd").click()
            except:

               if new_height == last_height:
                   break
        last_height = new_height

keyword = input('검색할 태그를 입력하세요 : ')
url = 'https://search.daum.net/nate?w=img&nil_search=btn&DA=NTB&enc=utf8&q={}'.format(keyword)

driver = webdriver.Chrome('C:/Program Files (x86)/Google/chromedriver/chromedriver')
driver.get(url)

time.sleep(1)

scroll_down()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
images = soup.find_all('img', attrs={'class':'thumb_img'})

print('number of img tags: ', len(images))

n = 1
for i in images:

    try:
        imgUrl = i["src"]
    except:
        imgUrl = i["data-src"]
        
    with urllib.request.urlopen(imgUrl) as f:
        with open('../_data/green/green' + keyword + str(n) + 'd.jpg', 'wb') as h:
            img = f.read()
            h.write(img)


    n += 1