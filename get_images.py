#get_images.py
from config import *
import requests
from requests.auth import HTTPBasicAuth

import os
import wget
import csv

#WEB STUFF
query_url = "https://api.datamarket.azure.com/Bing/Search/v1/Image?Query='%s'&$format=json"
# create credential for authentication
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"
# create auth object
auth = HTTPBasicAuth(API_KEY, API_KEY)
# set headers
headers = {'User-Agent': user_agent}

def getWords(word_file, output_dir):
    reader = csv.DictReader(open(word_file, 'rU'))
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for row in reader:
        word = row['word']
        if not os.path.exists(word):
            os.mkdir(word)
        url = query_url % word
        # get response from search url
        response_data = requests.get(url, headers=headers, auth = auth)
        # decode json response content
        json_result = response_data.json()

        stuff = json_result['d']['results']

        count = 1
        for s in stuff[10:]:
            img_url = s['MediaUrl']
            ext = img_url.split('.')[-1]
            w = s['Width']
            h = s['Height']
            out = '%s/%s/%s_%s.%s' % (output_dir, word, word, count, ext)
            try:
                filename = wget.download(img_url, out)
            except:
                print "Error, could not download %s" % img_url
            count = count + 1
