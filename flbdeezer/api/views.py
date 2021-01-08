import django
from django.shortcuts import render
from django.http import JsonResponse
from pydeezer import Deezer
from pydeezer.constants import track_formats

myarl = 'dc5b637d8a21db2175dced43ef16a9e6d6a49ca2cf764f63daf1dd0aa8e80175f843970a754e2412c2f207b2d58244ae112dd851826bfa544f1ea6ac9e49f215b749156c22ec6d7b376c09c7467e2dd8b8d636a68f4cef4d32fdad61fbeaa7a8'


def searchdeezer(request):
    # category can be [tracks,albums,artists,playlists]
    # query is the searc term
    category, query = '', ''
    deezer = Deezer()

    try:
        category = request.GET['category']
        query = request.GET['query']

    except django.utils.datastructures.MultiValueDictKeyError:
        return JsonResponse({
            'error': 'required params: category[tracks, albums, artists, playlists] and query ie Drake',
            'example': 'http://127.0.0.1:8000/search/?category=albums&query=gods%20plan'
        })

    # make sure all params are included
    # edit to change limit and index
    limit = 30
    index = 0
    search_results = []

    if category == 'tracks':
        search_results = deezer.search_tracks(query, limit, index)
        # best for api
        filtered_list = []
        for result in search_results:
            filtered_result = {
                'id': result['id'],
                'title': result['title'],
                'artist_id': result['artist']['id'],
                'artist_name': result['artist']['name'],
                'artist_picture': result['artist']['picture'],
                'duration': result['duration'],
                'album_id': result['album']['id'],
                'album_cover': result['album']['cover_medium']
            }
            filtered_list.append(filtered_result)

        search_results = filtered_list

    if category == 'albums':
        search_results = deezer.search_albums(query, limit, index)
        flist = []
        for result in search_results:
            fresult = {
                'id': result['id'],
                'title': result['title'],
                'cover': result['cover_medium'],
                'tracklist': result['tracklist']
            }
            flist.append(fresult)
        # click tracklist to get 50 tracks from album
        search_results = flist

    if category == 'artists':
        search_results = deezer.search_artists(query, limit, index)
        flist = []
        for result in search_results:
            fresult = {
                'id': result['id'],
                'name': result['name'],
                'picture': result['picture_medium'],
                'tracklist': result['tracklist']
            }
            flist.append(fresult)
        # click tracklist to get 50 tracks from artist
        search_results = flist

    if category == 'playlists':
        search_results = deezer.search_playlists(query, limit, index)
        flist = []
        for result in search_results:
            fresult = {
                'id': result['id'],
                'title': result['title'],
                'picture': result['picture_medium'],
                'tracklist': result['tracklist']
            }
            flist.append(fresult)
        # click tracklist to get 50 tracks from playlist
        search_results = flist

    output = {
        'search': category,
        'query': query,
        'results': search_results
    }

    return JsonResponse(output)


def downloaddeezer(request):
    # track id in url params
    try:
        track_id = request.GET['id']
    except django.utils.datastructures.MultiValueDictKeyError:
        return JsonResponse({
            'error': 'required params: id',
            'example': 'http://127.0.0.1:8000/download/?id=533609232'
        })

    deezer = Deezer(arl=myarl)
    track = {}
    output = {}

    try:
        track = deezer.get_track(track_id)
        track_info = track['info']['DATA']
        link = deezer.get_track_download_url(track_info)

        output = {
            'id': track_id,
            'title': track['info']['DATA']['SNG_TITLE'],
            'artist': track['info']['DATA']['ART_NAME'],
            'link': link[0],
            'quality': link[1],
            'lyrics_sync': track['info']['LYRICS']['LYRICS_SYNC_JSON'],
            'lyrics_text': track['info']['LYRICS']['LYRICS_TEXT']
        }

    except Exception as e:
        output = {
            'id': track_id,
            'error': str(e),
            'text': 'an error occured creating link'
        }

    return JsonResponse(output)
