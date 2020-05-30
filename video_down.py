import requests
session = requests.session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}

with open('D:/sb/zxD20161011154409956/index.m3u8', 'r+') as f:
    for line in f:
        line = line.strip()
        if 'https' in line:
            print(line)
            while True:
                try:
                    r = session.get(line, timeout=10, headers=headers)
                    if r.status_code == 200:
                        break
                except Exception as ex:
                    print(ex)
            with open('D:/py/aierlan.mp4', 'ab+') as file:
                file.write(r.content)
            