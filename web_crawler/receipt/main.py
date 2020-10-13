import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://bluezz.com.tw/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    soup = soup.select('img')

    imgs = []
    titles = []

    for index in range(len(soup)):
        try:
            titles.append(soup[index]['alt'])
        except:
            continue
        imgs.append(soup[index]['src'])
    
    for index in range(len(imgs)):
        print(titles[index] + '：' + imgs[index])

if __name__ == '__main__':
    main()
