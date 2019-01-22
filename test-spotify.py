#!/usr/bin/env python3.6

import base64
import requests
import os
import json
import time
import sys
from requests.auth import HTTPBasicAuth
import spotipy
import spotipy.util as util

"""


:param sys.argv[0] clientid
:param sys.argv[1] clientsecret
22.01.2019
Simone van Zyl
"""

scope = 'user-library-read'


def login(clientid, clientsecret):
    global scope

    token = util.prompt_for_user_token(clientid, scope)

    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_saved_tracks()
        for item in results['items']:
            track = item['track']
            print(track['name'] + ' - ' + track['artists'][0]['name'])
    else:
        print("Can't get token for" + username)

    #payload = {'grant_type':'client_credentials'}
    #auth_header = base64.b64encode(six.text_type(clientid +
    #    ':' + clientsecret).encode('ascii'))
    #headers = {'Authorization': 
    #           'Basic %s' % auth_header.decode('ascii')}

    #response = requests.get('https://accounts.spotify.com/api/token', 
    #           data=payload, headers=headers, verify=True)
    #print("JSON: '{}'".format(response.json))

if __name__ == "__main__":
    clientid = sys.argv[0]
    clientsecret = sys.argv[1]
    login(clientid, clientsecret)
