import requests
from io import BytesIO
from skimage import io
from yiyu_crawler_lib import beauty_hot

def main():
    url = beauty_hot()
    print(url)
    res = requests.get(url)
    img = io.imread(BytesIO(res.content))
    io.imshow(img)
    io.show()

if __name__ == "__main__":
    main()
