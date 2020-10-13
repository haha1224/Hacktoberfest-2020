import json, requests

def main():
    url = 'https://www.dcard.tw/_api/posts?popular=true&limit=10'
    res = requests.get(url)
    json_Obj = json.loads(res.text)

    titles = [x['title'] for x in json_Obj]
    categories = [x['forumAlias'] for x in json_Obj]
    ids = [x['id'] for x in json_Obj]

    for index in range(len(titles)):
        print(titles[index] + '：' + 'https://www.dcard.tw/f/' + categories[index] + '/p/' + str(ids[index]))

if __name__ == '__main__':
    main()
