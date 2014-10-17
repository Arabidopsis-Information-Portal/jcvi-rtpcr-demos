import json
import requests
import re

# This illustrates an example of transforming JSON from the current format served
# by JCVI servers to a prototype AIP-compliant data frame. It's implemented as a 
# query type but if we sacrificed enforcement and validation of params it could
# be a map_filter type as well. 
     
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
    url = 'http://www.jcvi.org/cgi-bin/arabidopsis/qpcr/ExpressionPerGenePerTissue?Submit=Search&format=json&gene=' + trans
    if not material is None:
        url = url + '&tissue=' + material
    
    r = requests.get(url)
    for result in r.json()['expression']:
        record = { 'class':'transcript_property',
                   'transcript': trans,
                   'source_text_description': 'RT-PCR',
                   'expression_record': [ 
                        {'material_text_description': valid_materials[result['elem_tissue'].lower()],
                        'cycle_time':result['elem_cycle_time'],
                        'cycle_time_stdev':result['elem_cycle_time2'],
                        'absolute_concentration':result['elem_conc'],
                        'absolute_concentration_stdev':result['elem_conc2'],
                        'ratio_to_invariants':result['elem_ratio'],
                        'ratio_to_invariants_stdev':result['elem_ratio2']} 
                   ]
        }
        print json.dumps(record, indent=4)
        print '---'

def list(arg):
	# We don't have a valid operation for the /list endpoint. At present, just return a nasty
	# looking stack trace from within ADAMA. At least the client will know they did something bad
    pass
