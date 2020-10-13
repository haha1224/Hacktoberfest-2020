# Youtube 不分類熱門

## Description

請從 Youtube 不分類熱門影片中找出影片標題以及網址，盡量讓結果排版整齊舒服。

## Requirement

* BeautifulSoup

## Hint

* Youtube 不分類熱門影片的 base url：https://www.youtube.com.tw/feed/trending。
* 如果有用到 selenium，executable_path 記得要設定成絕對值。
* Headless Chrome Driver 可以用以下設定達成。

```python
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
```
