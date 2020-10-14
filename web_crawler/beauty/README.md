# PTT 表特版

## Description

請從 PTT 表特版 index2250.html ~ index2264.html 之間隨機挑一張照片，印出網址以及照片。

## Requirement

* BeautifulSoup
* 請用這個 [file](https://github.com/yiyu0x/web_crawler/blob/master/yiyu_crawler_lib.py) 做開發，如果有想到更好的演算法可以更新，如果沒有的話，請照著上面的程式繼續做下去。

## Hint

* 表特版的 base url：https://webptt.com/m.aspx?n=bbs/Beauty/
* 表特版的 html 名稱格式為：index + \<數字，介於 2250 ~ 2264\> + .html
* io package 中的 BytesIO 函式可以讀入影像字串。
* skimage package 的 imread, imshow, show 分別可以讀入影像、設定影像參數以及印出影像。
