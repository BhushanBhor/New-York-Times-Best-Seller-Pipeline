# !/bin/bash
import requests
import json

def get_list():
    url = 'https://api.nytimes.com/svc/books/v3/lists.json'

    params = {'list': 'combined-print-and-e-book-fiction', 'api-key' : 'Utvwx7eVJCAACG6ecTuy0fanguKDRkR4'}
    response1 = requests.get(url, params=params)

    params = {'list': 'combined-print-and-e-book-nonfiction', 'api-key' : 'Utvwx7eVJCAACG6ecTuy0fanguKDRkR4'}
    response2 = requests.get(url, params=params)

 #   combined = response1 + response2
    data = response1.json()
    with open('fiction.json', 'w') as f:
        json.dump(data, f)

    data = response2.json()
    with open('non-fiction.json', 'w') as f:
        json.dump(data, f)

get_list()