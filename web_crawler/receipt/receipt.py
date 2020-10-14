from bs4 import BeautifulSoup # 匯入濃湯
import requests
res = requests.get('https://bluezz.com.tw/')
soup = BeautifulSoup(res.text, "html.parser") # soup 看整理過的code
aa = soup.select('img.blog_pic')
for ii in aa:
    print(ii.get('src'))
