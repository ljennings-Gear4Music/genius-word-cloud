import re
import time
import requests
from bs4 import BeautifulSoup


def get_lyrics_from_url(song_url):
    time.sleep(3)  # Sleep to stop genius from rate limiting us
    response = requests.get(song_url)
    # TODO - check response code before continuing
    html = BeautifulSoup(response.text, "html.parser")
    [h.extract() for h in html('script')]
    lyrics = html.find("div", class_="lyrics").get_text()

    # Strip brackets for example [Verse 1] or [Chorus]
    lyrics = re.sub(r'(\[)(\s|\w)+?(\])', "", lyrics)

    # Strip punctuation
    lyrics = re.sub(r'([.,?!"\':;()])+', "", lyrics)

    return lyrics