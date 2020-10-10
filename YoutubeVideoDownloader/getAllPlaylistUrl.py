# getAllPlaylist.py
""" 
@author Dhairyashil Patil    
@description 1) pass the playlist URL on line number 10, 
             2) Generate Google_API key and replace 'your_key' with generated key.
             3) Copy and Use the generated list to download audio files.
"""
import googleapiclient.discovery
from urllib.parse import parse_qs, urlparse

#extract playlist id from url
url = 'https://www.youtube.com/playlist?list=PLu57YNLRwh4WEp5tHnWpYgWDFBw4ZZ60d' #enter your playlist URL here
query = parse_qs(urlparse(url).query, keep_blank_values=True)
playlist_id = query["list"][0]

print(f'get all playlist items links from {playlist_id}')
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = "your_key")
#go to https://console.developers.google.com/apis/credentials ang generate your own api key
request = youtube.playlistItems().list(
    part = "snippet",
    playlistId = playlist_id,
    maxResults = 50
)
response = request.execute()

playlist_items = []
while request is not None:
    response = request.execute()
    playlist_items += response["items"]
    request = youtube.playlistItems().list_next(request, response)

print(f"total: {len(playlist_items)}")
print([ 
    f'https://www.youtube.com/watch?v={t["snippet"]["resourceId"]["videoId"]}&list={playlist_id}&t=0s'
    for t in playlist_items
])