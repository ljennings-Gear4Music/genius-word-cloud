import requests
import json
import geniuswordcloud

import os
os.getcwd()


def main():
    client_access_token = 'ZnMQX0OWuKOSMGz79rqdwi1MvdmQAQiUS-U5bAFCeR2l9B6vERxYDok6re-hbd8-'
    base_url = 'https://api.genius.com'

    artist_id = geniuswordcloud.get_artist_id('eminem')
    print(artist_id)

    path = "artists/{0}/songs".format(artist_id)
    print(path)
    request_uri = '/'.join([base_url, path])

    params = {'per_page': 10, 'sort': 'popularity'}  # TODO - Work out max per page
    token = 'Bearer {}'.format(client_access_token)
    headers = {'Authorization': token}

    r = requests.get(request_uri, params=params, headers=headers)
    parsed = json.loads(r.text)
    print(json.dumps(parsed, indent=4, sort_keys=True))

    word_dict = dict()
    for song in parsed["response"]["songs"]:
        if song["primary_artist"]["id"] == artist_id:  # TODO - This should be dynamic
            print('Processing:' + song['path'])
            lyrics = geniuswordcloud.get_lyrics_from_url('https://genius.com' + song["path"])
            for word in lyrics.split():
                if word.lower() in word_dict:
                    word_dict[word.lower()] += 1
                else:
                    word_dict[word.lower()] = 1

    index = 0
    for k, v in sorted(word_dict.items(), key=lambda x: x[1], reverse=True):
        if index != 10:
            print(k, v)
            index += 1


if __name__ == "__main__":
    main()
