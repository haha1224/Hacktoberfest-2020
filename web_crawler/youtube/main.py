import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

url = 'https://www.youtube.com.tw/feed/trending'
executable_path = 'D:\\桌面\\github build\\web_crawler\\youtube\\chromedriver.exe'

# driver = webdriver.Chrome(executable_path=executable_path,chrome_options=chrome_options)
driver = webdriver.Chrome(executable_path=executable_path)
driver.get(url)

res = driver.find_element_by_id('dismissable').get_attribute('innerHTML')
soup = BeautifulSoup(res, 'html.parser')

base_url = 'https://youtube.com/'
obj_list = soup.select('a#video-title')
titles = [x['title'] for x in obj_list]
urls = [x['href'] for x in obj_list]

for index in range(len(titles)):
    print(titles[index] + '：' + urls[index])
    