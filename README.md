### apiflbdeeze

deezer api for flb player

# Endpoints

## api search

requires :

- category
- query

### category

can either be

- artists eg drake
- albums  
- playlists
- tracks

example <http://127.0.0.1:8000/search/?category=albums&query=gods%20plan>

outputs  

``` json
{"search": "albums", "query": "gods plan", "results": [{"id": 61230722, "title": "Drake God's Plan", "cover": "https://e-cdns-images.dzcdn.net/images/cover/3d6d04f86f7769e3f6539bc765cf9a4e/250x250-000000-80-0-0.jpg", "tracklist": "https://api.deezer.com/album/61230722/tracks"}, {"id": 127866022, "title": "God's Plan", "cover": "https://e-cdns-images.dzcdn.net/images/cover/b56637e2ea018dc53adf8891daaf34ee/250x250-000000-80-0-0.jpg", "tracklist": "https://api.deezer.com/album/127866022/tracks"}, {"id": 58518952, "title": "God's Plan", "cover": "https://e-cdns-images.dzcdn.net/images/cover/dcc069bab48e2681ef0488a4aa507aa4/250x250-000000-80-0-0.jpg", "tracklist": "https://api.deezer.com/album/58518952/tracks"}, {"id": 61778572, "title": "Gods Plan", "cover": "https://e-cdns-images.dzcdn.net/images/cover/1a6f83d753c722d7fe19bccdd83d82eb/250x250-000000-80-0-0.jpg", "tracklist": "https://api.deezer.com/album/61778572/tracks"}, {"id": 83221592, "title": "God's Plan", "cover": "https://e-cdns-images.dzcdn.net/images/cover/a37b4226b3afbdfa5c112daadbff9381/250x250-000000-80-0-0.jpg", "tracklist": "https://api.deezer.com/album/83221592/tracks"}, {"id": 9263218, "title": "God's Plan", "cover": "https://e-cdns-images.dzcdn.net/images/cover/92cc09319cdfd43b8ca28cc061086161/250x250-000000-80-0-0.jpg", "tracklist": "https://api.deezer.com/album/9263218/tracks"}, {"id": 86057812, "title": "God's Plan Ep", "cover": "https://e-cdns-images.dzcdn.net/images/cover/8c4925640d7334776a2b27e6d3531c75/250x250-000000-80-0-0.jpg", "tracklist": "https://api.deezer.com/album/86057812/tracks"}, {"id": 56432852, "title": "God's Plan", "cover": "https://e-cdns-images.dzcdn.net/images/cover/7a7db86b7b53d4b146704f5a1847c1cb/250x250-000000-80-0-0.jpg", "tracklist": "https://api.deezer.com/album/56432852/tracks"}, {"id": 62998722, "title": "God's Plan", "cover": "https://e-cdns-images.dzcdn.net/images/cover/5b7143eaf4ae758d51624285aa1f8a43/250x250-000000-80-0-0.jpg", "tracklist": "https://api.deezer.com/album/62998722/tracks"}, {"id": 98031042, "title": "Gods Plan", "cover": "https://e-cdns-images.dzcdn.net/images/cover/a5152fd87eabe7ded027e4012c72e7ee/250x250-000000-80-0-0.jpg", "tracklist": "https://api.deezer.com/album/98031042/tracks"}, {"id": 58919752, "title": "God's Plan", "cover": "https://e-cdns-images.dzcdn.net/images/cover/ff37088907648beff9115eff1ff401fc/250x250-000000-80-0-0.jpg", "tracklist": "https://api.deezer.com/album/58919752/tracks"}, {"id": 56474542, "title": "God's Plan", "cover": "https://e-cdns-images.dzcdn.net/images/cover/05e25afcc35643096725afe04c739430/250x250-000000-80-0-0.jpg", "tracklist": "https://api.deezer.com/album/56474542/tracks"}, {"id": 198088262, "title": "Gods Plan", "cover": "https://e-cdns-images.dzcdn.net/images/cover/2e6497b5857575e539fcf3c98c3f2752/250x250-000000-80-0-0.jpg", "tracklist": "https://api.deezer.com/album/198088262/tracks"}, {"id": 56351762, "title": "God's Plan", "cover": "https://e-cdns-images.dzcdn.net/images/cover/7f7f4f62c47cbad6241135b0ee64135a/250x250-000000-80-0-0.jpg", "tracklist": "https://api.deezer.com/album/56351762/tracks"}, {"id": 198293172, "title": "God's Plan", "cover": "https://e-cdns- .........
```

#### tracks

returns

- id
- title
- artist_id
- artist_name
- artist_picture
- duration
- album_id
- album_cover

``` python
 JsonResponse({
    'id': result['id'],
    'title': result['title'],
    'artist_id': result['artist']['id'],
    'artist_name': result['artist']['name'],
    'artist_picture': result['artist']['picture'],
    'duration': result['duration'],
    'album_id': result['album']['id'],
    'album_cover': result['album']['cover_medium']
})

```

#### albums

returns

- id
- title
- cover = album image
-tracklist = url ie <https://api.deezer.com/album/62998722/tracks>

```python
 JsonResponse{
        'id': result['id'],
        'title': result['title'],
        'cover': result['cover_medium'],
        'tracklist': result['tracklist']
    }

```

#### artists

returns

- id
- artist name
- artist picture
- tracklist

```python

JsonResponse {
        'id': result['id'],
        'name': result['name'],
        'picture': result['picture_medium'],
        'tracklist': result['tracklist']
    }
```

#### playlists

returns

- id
- title
- picture
- tracklist

``` python

 JsonResponse{
    'id': result['id'],
    'title': result['title'],
    'picture': result['picture_medium'],
    'tracklist': result['tracklist']
} 
```

#### tracklist

returned from - albums,playlists and artists
contains example

``` json
{"data":[{"id":496525612,"readable":true,"title":"God's Plan","title_short":"God's Plan","title_version":"","isrc":"GBDMT1800186","link":"https:\/\/www.deezer.com\/track\/496525612","duration":189,"track_position":1,"disk_number":1,"rank":242768,"explicit_lyrics":false,"explicit_content_lyrics":0,"explicit_content_cover":2,"preview":"https:\/\/cdns-preview-e.dzcdn.net\/stream\/c-e876ec0fef5c332b4604a16d531e08ef-3.mp3","md5_image":"5b7143eaf4ae758d51624285aa1f8a43","artist":{"id":68249,"name":"Our Last Night","tracklist":"https:\/\/api.deezer.com\/artist\/68249\/top?limit=50","type":"artist"},"type":"track"}],"total":1}

```

## download api

requires id
example <http://127.0.0.1:8000/download/?id=533609232>

returns

- id
- title
- artist
- link
- quality
- lyrics_sync
- lyrics text

``` python

 output = {
    'id': track_id,
    'title': track['info']['DATA']['SNG_TITLE'],
    'artist': track['info']['DATA']['ART_NAME'],
    'link': link[0],
    'quality': link[1],
    'lyrics_sync': track['info']['LYRICS']['LYRICS_SYNC_JSON'],
    'lyrics_text': track['info']['LYRICS']['LYRICS_TEXT']
}
```

example output

```json

{"id": "533609232", "title": "God's Plan", "artist": "Drake", "link": "https://e-cdns-proxy-9.dzcdn.net/mobile/1/5f6e97eddc7213a0bf49cb212e0888f343c54399006685f0739ae113a3171a44cebf23baced2b98c6d9d77e9e8639d9bd68910f109c230c139c8df66f5eddbd03203a78a938d3658f887c5f1a1b2ca3d", "quality": "MP3_128", "lyrics_sync": [{"lrc_timestamp": "[00:04.36]", "milliseconds": "4360", "duration": "3290", "line": "Yeah they wishin' and wishin' and wishin' and wishin'"}, {"lrc_timestamp": "[00:07.69]", "milliseconds": "7690", "duration": "4390", "line": "They wishin' on me, yuh"}, {"line": ""}, {"lrc_timestamp": "[00:12.51]", "milliseconds": "12510", "duration": "3040", "line": "I been movin' calm, don't start no trouble with me"}, {"lrc_timestamp": "[00:15.59]", "milliseconds": "15590", "duration": "3120", "line": "Tryna keep it peaceful is a struggle for me"}, {"lrc_timestamp": "[00:18.74]", "milliseconds": "18740", "duration": "3070", "line": "Don't pull up at 6 AM to cuddle with me"}, {"lrc_timestamp": "[00:21.85]", "milliseconds": "21850", "duration": "3080", "line": "You know how I like it when you lovin' on me"}, {"lrc_timestamp": "[00:24.96]", "milliseconds": "24960", "duration": "3100", "line": "I don't wanna die for them to miss me"}, {"lrc_timestamp": "[00:28.08]", "milliseconds": "28080", "duration": "3070", "line": "Yes I see the things that they wishin' on me"}, {"lrc_timestamp": "[00:31.17]", "milliseconds": "31170", "duration": "3070", "line": "Hope I got some brothers that outlive me"}, {"lrc_timestamp": "[00:34.29]", "milliseconds": "34290", "duration": "3100", "line": "They gon' tell the story, shit was different with me"}, {"line": ""}, {"lrc_timestamp": "[00:37.43]", "milliseconds": "37430", "duration": "3440", "line": "God's plan, God's plan"}, {"lrc_timestamp": "[00:41.66]", "milliseconds": "41660", "duration": "2210", "line": "I hold back, sometimes I won't, yuh"}, {"lrc_timestamp": "[00:44.78]", "milliseconds": "44780", "duration": "3040", "line": "I feel good, sometimes I don't, ayy, don't"}, {"lrc_timestamp": "[00:47.87]", "milliseconds": "47870", "duration": "3080", "line": "I finessed down Weston Road, ayy, 'nessed"}, {"lrc_timestamp": "[00:51.00]", "milliseconds": "51000", "duration": "2940", "line": "Might go down a G-O-D, yeah, wait"}, {"lrc_timestamp": "[00:54.06]", "milliseconds": "54060", "duration": "2690", "line": "I go hard on Southside G, yuh, Way"}, {"lrc_timestamp": "[00:57.15]", "milliseconds": "57150", "duration": "2830", "line": "I make sure that north side eat"}, {"lrc_timestamp": "[01:00.55]", "milliseconds": "60550", "duration": "2520", "line": "And still"}, {"line": ""}, {"lrc_timestamp": "[01:03.84]", "milliseconds": "63840", "duration": "980", "line": "Bad things"}, {"lrc_timestamp": "[01:05.00]", "milliseconds": "65000", "duration": "1510", "line": "It's a lot of bad things"}, {"lrc_timestamp": "[01:06.54]", "milliseconds": "66540", "duration": "3280", "line": "That they wishin' and wishin' and wishin' and wishin'"}, {"lrc_timestamp": "[01:09.86]", "milliseconds": "69860", "duration": "5410", "line": "They wishin' on me"}, {"lrc_timestamp": "[01:16.27]", "milliseconds": "76270", "duration": "1070", "line": "Bad things"}, {"lrc_timestamp": "[01:17.43]", "milliseconds": "77430", "duration": "1500", "line": "It's a lot of bad things"}, {"lrc_timestamp": "[01:18.97]", "milliseconds": "78970", "duration": "3250", "line": "That they wishin' and wishin' and wishin' and wishin'"}, {"lrc_timestamp": "[01:22.23]", "milliseconds": "82230", "duration": "1670", "line": "They wishin' on me"}, {"lrc_timestamp": "[01:24.47]", "milliseconds": "84470", "duration": "3330", "line": "Yuh, ayy, ayy (ayy)"}, {"line": ""}, {"lrc_timestamp": "[01:27.85]", "milliseconds": "87850", "duration": "3020", "line": "She say, \"Do you love me?\" I tell her, \"Only partly\""}, {"lrc_timestamp": "[01:30.89]", "milliseconds": "90890", "duration": "3210", "line": "I only love my bed and my momma, I'm sorry"}, {"lrc_timestamp": "[01:34.12]", "milliseconds": "94120", "duration": "3070", "line": "Fifty Dub, I even got it tatted on me"}, {"lrc_timestamp": "[01:37.23]", "milliseconds": "97230", "duration": "3460", "line": "81, they'll bring the crashers to the party"}, {"lrc_timestamp": "[01:40.74]", "milliseconds": "100740", "duration": "1070", "line": "And you know me"}, {"lrc_timestamp": "[01:42.66]", "milliseconds": "102660", "duration": "2520", "line": "Turn a O-2 into the O-3, dog"}, {"lrc_timestamp": "[01:45.78]", "milliseconds": "105780", "duration": "2460", "line": "Without 40, Oli', there'd be no me"}, {"lrc_timestamp": "[01:48.87]", "milliseconds": "108870", "duration": "1850", "line": "'Magine if I never met the broskis"}, {"line": ""}, {"lrc_timestamp": "[01:52.07]", "milliseconds": "112070", "duration": "2730", "line": "God's plan, God's plan"}, {"lrc_timestamp": "[01:56.30]", "milliseconds": "116300", "duration": "2890", "line": "I can't do this on my own, ayy, no, ayy"}, {"lrc_timestamp": "[01:59.34]", "milliseconds": "119340", "duration": "2140", "line": "Someone watchin' this shit close, yep, close"}, {"lrc_timestamp": "[02:02.50]", "milliseconds": "122500", "duration": "3030", "line": "I've been me since Scarlett Road, ayy, road, ayy"}, {"lrc_timestamp": "[02:05.62]", "milliseconds": "125620", "duration": "2240", "line": "Might go down as G-O-D, yeah, wait"}, {"lrc_timestamp": "[02:08.73]", "milliseconds": "128730", "duration": "2370", "line": "I go hard on Southside G, ayy, Way"}, {"lrc_timestamp": "[02:11.84]", "milliseconds": "131840", "duration": "2950", "line": "I make sure that north side eat, yuh"}, {"lrc_timestamp": "[02:15.14]", "milliseconds": "135140", "duration": "680", "line": "And still"}, {"line": ""}, {"lrc_timestamp": "[02:18.44]", "milliseconds": "138440", "duration": "1150", "line": "Bad things"}, {"lrc_timestamp": "[02:19.62]", "milliseconds": "139620", "duration": "1480", "line": "It's a lot of bad things"}, {"lrc_timestamp": "[02:21.15]", "milliseconds": "141150", "duration": "3310", "line": "That they wishin' and wishin' and wishin' and wishin'"}, {"lrc_timestamp": "[02:24.50]", "milliseconds": "144500", "duration": "1240", "line": "They wishin' on me"}, {"lrc_timestamp": "[02:26.61]", "milliseconds": "146610", "duration": "3100", "line": "Yeah, yeah"}, {"lrc_timestamp": "[02:30.84]", "milliseconds": "150840", "duration": "970", "line": "Bad things"}, {"lrc_timestamp": "[02:32.05]", "milliseconds": "152050", "duration": "1470", "line": "It's a lot of bad things"}, {"lrc_timestamp": "[02:33.59]", "milliseconds": "153590", "duration": "3170", "line": "That they wishin' and wishin' and wishin' and wishin'"}, {"lrc_timestamp": "[02:36.78]", "milliseconds": "156780", "duration": "1860", "line": "They wishin' on me"}, {"lrc_timestamp": "[02:39.06]", "milliseconds": "159060", "duration": "1310", "line": "Yeah"}], "lyrics_text": "Yeah they wishin' and wishin' and wishin' and wishin'\r\nThey wishin' on me, yuh\r\n\r\nI been movin' calm, don't start no trouble with me\r\nTryna keep it peaceful is a struggle for me\r\nDon't pull up at 6 AM to cuddle with me\r\nYou know how I like it when you lovin' on me\r\nI don't wanna die for them to miss me\r\nYes I see the things that they wishin' on me\r\nHope I got some brothers that outlive me\r\nThey gon' tell the story, shit was different with me\r\n\r\nGod's plan, God's plan\r\nI hold back, sometimes I won't, yuh\r\nI feel good, sometimes I don't, ayy, don't\r\nI finessed down Weston Road, ayy, 'nessed\r\nMight go down a G-O-D, yeah, wait\r\nI go hard on Southside G, yuh, Way\r\nI make sure that north side eat\r\nAnd still\r\n\r\nBad things\r\nIt's a lot of bad things\r\nThat they wishin' and wishin' and wishin' and wishin'\r\nThey wishin' on me\r\nBad things\r\nIt's a lot of bad things\r\nThat they wishin' and wishin' and wishin' and wishin'\r\nThey wishin' on me\r\nYuh, ayy, ayy (ayy)\r\n\r\nShe say, \"Do you love me?\" I tell her, \"Only partly\"\r\nI only love my bed and my momma, I'm sorry\r\nFifty Dub, I even got it tatted on me\r\n81, they'll bring the crashers to the party\r\nAnd you know me\r\nTurn a O-2 into the O-3, dog\r\nWithout 40, Oli', there'd be no me\r\n'Magine if I never met the broskis\r\n\r\nGod's plan, God's plan\r\nI can't do this on my own, ayy, no, ayy\r\nSomeone watchin' this shit close, yep, close\r\nI've been me since Scarlett Road, ayy, road, ayy\r\nMight go down as G-O-D, yeah, wait\r\nI go hard on Southside G, ayy, Way\r\nI make sure that north side eat, yuh\r\nAnd still\r\n\r\nBad things\r\nIt's a lot of bad things\r\nThat they wishin' and wishin' and wishin' and wishin'\r\nThey wishin' on me\r\nYeah, yeah\r\nBad things\r\nIt's a lot of bad things\r\nThat they wishin' and wishin' and wishin' and wishin'\r\nThey wishin' on me\r\nYeah"}
```

to download
_wite link contents in binary to a file_

