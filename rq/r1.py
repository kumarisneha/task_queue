import requests
import time

def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())

def test():
    time.sleep(20)
