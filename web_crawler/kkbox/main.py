import http.client, json, requests
from bs4 import BeautifulSoup
from kkbox_developer_sdk.auth_flow import KKBOXOAuth

def main():
    CLIENT_ID="460c75bbc275c0694737a476c09d2a3d"
    CLIENT_SECRET="6cb1d4094ff089250df8b7ff9f48e48b"

    auth = KKBOXOAuth(CLIENT_ID, CLIENT_SECRET)
    token = auth.fetch_access_token_by_client_credentials()


    conn = http.client.HTTPSConnection("api.kkbox.com")

    headers = {
        'accept': "application/json",
        'authorization': "Bearer " + token.access_token
        }

    conn.request("GET", "/v1.1/charts?territory=TW", headers=headers)

    res = conn.getresponse()
    data = res.read()

    # print(data.decode("utf-8"))

    json_obj = json.loads(data)
    keys = json_obj['data'][0].keys() # ['id', 'title', 'description', 'url', 'images', 'updated_at', 'owner']
    daily_url = json_obj['data'][2]['url']

    res = requests.get(daily_url)
    soup = BeautifulSoup(res.text, 'html.parser')

    titles = [x.text.strip().replace('\n', '') for x in soup.select('a.song-title')]
    
    artist_album = soup.select('div.song-artist-album') # 有些沒有專輯名稱，直接選取會分不清楚
    artist_album = [x.select('a') for x in artist_album]
    artists = [x[0]['title'] for x in artist_album]

    albums = []

    for item in artist_album:
        if len(item) == 1: # 只有歌手名稱
            albums.append('')
            continue
        albums.append(item[1]['title'])

    for i in range(len(titles)):
        print('歌曲：' + titles[i], end='')
        print(' 歌手：' + artists[i], end='')
        print(' 專輯：' + albums[i])

if __name__ == '__main__':
    main()
