import json
import requests
import re

def search(arg):
    locus = arg['locus']
    locus = locus.upper()

    url = 'http://www.jcvi.org/cgi-bin/arabidopsis/qpcr/ExpressionPerGenePerTissue?format=json&Submit=Search&gene=' + locus
    r = requests.get(url)
    
    if r.ok:
        return r.headers['Content-Type'],r.content
    else:
        # probably failed so return whatever text the remote service sent
        return r.headers['Content-Type'],r.text

def list(arg):
    pass
