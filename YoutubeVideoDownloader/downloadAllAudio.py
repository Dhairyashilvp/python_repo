from collections import defaultdict
d = defaultdict(list)
# Pass the array list generated using getAllPlaylistUrl.py or multiple video URL
urlList = [
    'https://www.youtube.com/watch?v=JwO2RbDpMzk&list=PLu57YNLRwh4WEp5tHnWpYgWDFBw4ZZ60d&t=0s', 
    'https://www.youtube.com/watch?v=vZ_NpLWuL00&list=PLu57YNLRwh4WEp5tHnWpYgWDFBw4ZZ60d&t=0s', 
    'https://www.youtube.com/watch?v=6BYIKEH0RCQ&list=PLu57YNLRwh4WEp5tHnWpYgWDFBw4ZZ60d&t=0s', 
    'https://www.youtube.com/watch?v=-eFqg8JnohY&list=PLu57YNLRwh4WEp5tHnWpYgWDFBw4ZZ60d&t=0s', 
    'https://www.youtube.com/watch?v=zneEjAenV8Y&list=PLu57YNLRwh4WEp5tHnWpYgWDFBw4ZZ60d&t=0s', 
    'https://www.youtube.com/watch?v=hMBKmQEPNzI&list=PLu57YNLRwh4WEp5tHnWpYgWDFBw4ZZ60d&t=0s', 
    'https://www.youtube.com/watch?v=53H2E__xNbI&list=PLu57YNLRwh4WEp5tHnWpYgWDFBw4ZZ60d&t=0s', 
    'https://www.youtube.com/watch?v=zzwRbKI2pn4&list=PLu57YNLRwh4WEp5tHnWpYgWDFBw4ZZ60d&t=0s', 
    'https://www.youtube.com/watch?v=XgyB-SI3TOY&list=PLu57YNLRwh4WEp5tHnWpYgWDFBw4ZZ60d&t=0s', 
    'https://www.youtube.com/watch?v=ATf05n5LBHQ&list=PLu57YNLRwh4WEp5tHnWpYgWDFBw4ZZ60d&t=0s', 
    'https://www.youtube.com/watch?v=_kUrW9SEaJc&list=PLu57YNLRwh4WEp5tHnWpYgWDFBw4ZZ60d&t=0s', 
    'https://www.youtube.com/watch?v=HELDauyokPE&list=PLu57YNLRwh4WEp5tHnWpYgWDFBw4ZZ60d&t=0s', 
    'https://www.youtube.com/watch?v=zaCbuB3w0kg&list=PLu57YNLRwh4WEp5tHnWpYgWDFBw4ZZ60d&t=0s', 
    'https://www.youtube.com/watch?v=v2-9rIL_f4w&list=PLu57YNLRwh4WEp5tHnWpYgWDFBw4ZZ60d&t=0s', 
    'https://www.youtube.com/watch?v=l12_JIQ2TqA&list=PLu57YNLRwh4WEp5tHnWpYgWDFBw4ZZ60d&t=0s', 
    'https://www.youtube.com/watch?v=QYh6mYIJG2Y&list=PLu57YNLRwh4WEp5tHnWpYgWDFBw4ZZ60d&t=0s', 
    'https://www.youtube.com/watch?v=q0hyYWKXF0Q&list=PLu57YNLRwh4WEp5tHnWpYgWDFBw4ZZ60d&t=0s', 
    'https://www.youtube.com/watch?v=YykjpeuMNEk&list=PLu57YNLRwh4WEp5tHnWpYgWDFBw4ZZ60d&t=0s', 
    'https://www.youtube.com/watch?v=dW2MmuA1nI4&list=PLu57YNLRwh4WEp5tHnWpYgWDFBw4ZZ60d&t=0s', 
    'https://www.youtube.com/watch?v=jH1RNk8954Q&list=PLu57YNLRwh4WEp5tHnWpYgWDFBw4ZZ60d&t=0s'
]
d1 = {"title":"","bitRate":""}
itr = 0
for url in urlList:
    video = pafy.new(url) 
    bestaudio = video.getbestaudio() 
    d1['title'] = bestaudio.title 
    d1['bitRate'] = bestaudio.title 
    d[itr].append(d1)
    itr += 1
    bestaudio.download()