#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import re
from os.path import join as urljoin

import jcvi_common

"""
This illustrates an example of transforming JSON from the current format served
by JCVI servers to a prototype AIP-compliant data frame. It's implemented as a
query type but if we sacrificed enforcement and validation of params it could
be a map_filter type as well.
"""

def search(args):
    """
    args contains a dict with one or key:values

    transcript is AGI identifier and is mandatory
    material is the tissue or treatment and is restricted below to a limited list
    """

    """
	In the future, ADAMA will check a query, map_*, or generic request against a list of mandatory
	parameters specified for each service. For now, if we want to enforce that behavior we need to
	implement it ourselves.

	ADAMA will have a graceful, cross-language exception handling scheme in a future release
	At present, we are hand-coding a return
    """
    if not ('transcript' in args):
        return

    """
	Check that client has requested what looks like a valid transcript identifier
    """
    trans = args['transcript'].upper()
    p = re.compile('AT[1-5MC]G[0-9]{5,5}\.[0-9]+', re.IGNORECASE)
    if not p.search(trans):
        return

    """
    If material was passed make sure its in the (hard-coded) approved list
    We also encode the written names of the samples here for inclusion into the JSON response
    For cross-compatibility, we could map these treatments/tissues to one or more
    third part ontologies and return those
    """
    valid_materials = { 'flower': 'Flower Buds', 'iaa': 'IAA', 'leaf': 'Leaf', \
            'root': 'Root', 'salicylic': 'Salicylic Acid', 'nacl': 'NaCl', \
            'young': 'Young Siliques', 't87': 'T87 Cell Culture'}

    if 'material' in args:
        material = args['material'].lower()
        if material not in valid_materials.keys():
            return
    else:
        material = None

    """
	Build the url from the base + the intended endpoint action
    Also encode the params (payload) into a dict
    """
    url = urljoin(jcvi_common.base_url(), 'ExpressionPerGenePerTissue')
    payload = { 'gene': trans, 'format': 'json', 'Submit': 'Search' }
    if material:
        payload['tissue'] = material

    """
    Make the request to the remote service
    """
    r = requests.get(url, params=payload)

    """
    Iterate through the results
    Foreach record from the remote service, build the response json
    Print this json to stdout followed by a record separator "---"
    ADAMA takes care of serializing these results
    """
    for result in r.json()['expression']:
        record = {
                'transcript': trans,
                'class': 'transcript_property',
                'source_text_description': 'RT-PCR',
                'expression_record': {
                    'material_text_description': valid_materials[result['elem_tissue'].lower()],
                    'cycle_time': result['elem_cycle_time'],
                    'cycle_time_stdev': result['elem_cycle_time2'],
                    'absolute_concentration': result['elem_conc'],
                    'absolute_concentration_stdev': result['elem_conc2'],
                    'ratio_to_invariants': result['elem_ratio'],
                    'ratio_to_invariants_stdev': result['elem_ratio2']
                }
            }
        print json.dumps(record, indent=2)
        print '---'

def list(args):
    """
	We don't have a valid operation for the /list endpoint. At present, just return a nasty
	looking stack trace from within ADAMA. At least the client will know they did something bad
    """
    pass
