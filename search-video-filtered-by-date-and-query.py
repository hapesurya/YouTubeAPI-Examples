api_key = "xxxxxxx" #MASUKKAN IP KEY YOUTUBE ANDA DISINI

from apiclient.discovery import build

youtube = build('youtube', 'v3', developerKey=api_key)

from datetime import datetime

start_time = datetime(year=2019, month=1, day=1).strftime('%Y-%m-%dT%H:%M:%SZ') #CEK TERLAMA
end_time = datetime(year=2019, month=6, day=30).strftime('%Y-%m-%dT%H:%M:%SZ') #CEK TERBARU

res = youtube.search().list(part='snippet',
                            q='xxxxx', #KATA KUNCI PENCARIAN
                            type='video',
                            publishedAfter=start_time,
                            publishedBefore=end_time,
                            maxResults=50).execute()

for item in sorted(res['items'], key=lambda x:x['snippet']['publishedAt']):
    print(item['snippet']['title'], item['snippet']['publishedAt'], item['id']['videoId'])
