import json
import requests
import re
from bs4 import BeautifulSoup

# This illustrates an example of transforming JSON from the HTML served
# by JCVI servers to a prototype AIP-compliant data frame. It's implemented as a 
# query type. We use the souper-handy BeautifulSoup module
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/

def search(arg):

# arg contains a dict with one or key:values
#
# transcript is AGI identifier and is mandatory
# material is the tissue or treatment and is restricted below to a limited list

	# In the future, ADAMA will check a query, map_*, or generic request against a list of mandatory
	# parameters specified for each service. For now, if we want to enforce that behavior we need to 
	# implement it ourselves. 
	#
	# ADAMA will have a graceful, cross-language exception handling scheme in a future release
	# At present, we are hand-coding a return
    if not ('transcript' in arg):
        return
        
	# Check that client has requested what looks like a valid transcript identifier    
    trans = arg['transcript']
    trans = trans.upper()
    p = re.compile('AT[1-5MC]G[0-9]{5,5}\.[0-9]+', re.IGNORECASE)
    if not p.search(trans):
        return
            
    # If material was passed make sure its in the (hard-coded) approved list
    # We also encode the written names of the samples here for inclusion into the JSON response
    # For cross-compatibility, we could map these treatments/tissues to one or more
    # third part ontologies and return those
    valid_materials = {'flower':'Flower Buds', 'iaa':'IAA', 'leaf':'Leaf', 'root':'Root', 'salicylic':'Salicylic Acid', 'nacl':'NaCl', 'young':'Young Siliques', 't87':'T87 Cell Culture'}
    
    if ('material' in arg):
        material = arg['material']
        material = material.lower()
        if not material in valid_materials.keys():
            return
    else:
        material = None
        
	# We can also use the params function of requests but I was lazy here
    url = 'http://www.jcvi.org/cgi-bin/arabidopsis/qpcr/ExpressionPerGenePerTissue?Submit=Search&format=html&gene=' + trans
    if not material is None:
        url = url + '&tissue=' + material
    
    r = requests.get(url)
    # This is where if differs from just transforming the data. 
    # We must implement a screen scraper!
    soup = BeautifulSoup(r.text)
    tables = soup.findChildren('table')
    # This will get the first (and only) table from the result page
    data_table = tables[0]
    # This extracts all its rows into a list, 
    # then deletes the header row because we don't need to process it
    rows = data_table.findChildren(['tr'])
    rows.pop(0)
    # Iterate over the rows, slotting their cells to a formatted JSON record
    for row in rows:
        # The HTML on this page is idiomatic. All cells are th instead of td
        cells = row.findChildren('th')
        # Stuff cells into a temporary dict
        # The strip() is needed because strings coming from bs4 have wierd whitespace padding
        # that needs to be removed
        record = { 'class':'transcript_property',
                   'transcript': trans,
                   'source_text_description': 'RT-PCR',
                   'expression_record': [ 
                        {'material_text_description': valid_materials.get( cells[1].string.strip().lower() ),
                        'cycle_time':cells[2].string.strip(),
                        'cycle_time_stdev':cells[3].string.strip(),
                        'absolute_concentration':cells[6].string.strip(),
                        'absolute_concentration_stdev':cells[7].string.strip(),
                        'ratio_to_invariants':cells[4].string.strip(),
                        'ratio_to_invariants_stdev':cells[5].string.strip() }
                   ]
        }
        print json.dumps(record, indent=2)
        print '---'
        
def list(arg):
	# We don't have a valid operation for the /list endpoint. At present, just return a nasty
	# looking stack trace from within ADAMA. At least the client will know they did something bad
    pass
