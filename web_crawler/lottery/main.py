# coding=utf-8
import requests
from bs4 import BeautifulSoup

def main():
    url = "https://www.taiwanlottery.com.tw/index_new.aspx#"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    def bingoBingo():
        bingo_bingo = soup.select("div.contents_box01")[0].select("div.ball_tx")

        print("BingoBingo: ")

        for index in range(len(bingo_bingo)):
            if index == 9:
                print(bingo_bingo[index].text)
            else:
                print(bingo_bingo[index].text, end=' ')

    def winWin():
        win_win = soup.select("div.contents_box06")[0].select("div.ball_tx")

        print("\n雙贏彩：")

        for index in range(len(win_win)):
            if index == 11:
                print(win_win[index].text)
            else:
                print(win_win[index].text, end=' ')

    def threeStar():
        three_star = soup.select("div.contents_box04")[0].select("div.ball_tx")
        
        print("\n三星彩：")

        for index in range(len(three_star)):
            print(three_star[index].text, end=' ')

        return True

    def fourStar():
        four_star = soup.select("div.contents_box04")[1].select("div.ball_tx")
        
        print("\n四星彩：")

        for index in range(len(four_star)):
            print(four_star[index].text, end=' ')

        return True

    bingoBingo()
    winWin()
    threeStar()
    fourStar()

if __name__ == '__main__':
    main()
