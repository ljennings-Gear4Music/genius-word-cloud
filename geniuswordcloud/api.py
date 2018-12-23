import requests
import json


def get_artist_id(artist_name):
    client_access_token = 'ZnMQX0OWuKOSMGz79rqdwi1MvdmQAQiUS-U5bAFCeR2l9B6vERxYDok6re-hbd8-'
    base_url = 'https://api.genius.com'

    path = 'search/'
    request_uri = '/'.join([base_url, path])

    params = {'q': artist_name}  # TODO - Work out max per page
    token = 'Bearer {}'.format(client_access_token)
    headers = {'Authorization': token}

    r = requests.get(request_uri, params=params, headers=headers)
    if r.status_code != 200:
        return None

    parsed = json.loads(r.text)

    if not parsed['response']['hits']:
        return None

    return parsed['response']['hits'][0]['result']['primary_artist']['id']
