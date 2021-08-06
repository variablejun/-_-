import urllib.request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time
SCROLL_PAUSE_SEC = 1 # 대기시간
def scroll_down():
     global driver
     # 스크롤의 높이
     last_height = driver.execute_script("return document.body.scrollHeight")

     while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_SEC) # 스크롤을 끝까지 내렷을때 로딩 대기시간
        #스크롤 높이를 다시 가져옴
        new_height = driver.execute_script("return document.body.scrollHeight")
        #다시가져온 높이와 기존 높이가 같으면  대기후 
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
url = 'https://www.google.com/search?q={}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjgwPKzqtXuAhWW62EKHRjtBvcQ_AUoAXoECBEQAw&biw=768&bih=712'.format(keyword)

driver = webdriver.Chrome('C:/Program Files (x86)/Google/chromedriver/chromedriver')
driver.get(url)

scroll_down()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
images = soup.find_all('img', attrs={'class':'rg_i Q4LuWd'})

print('number of img tags: ', len(images))

n = 1
for i in images:

    try:
        imgUrl = i["src"]
    except:
        imgUrl = i["data-src"]
        
    with urllib.request.urlopen(imgUrl) as f:
        with open('../_data/green/green' + keyword + str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)


    n += 1