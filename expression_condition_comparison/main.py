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
    if not args.viewkeys() & {'material1', 'material2', 'foldchange'}:
        return

    """
    Check that foldchange is a valid number
    """
    foldchange = args['foldchange']
    try:
        n = float(foldchange)
    except (ValueError, TypeError):
        return

    """
    Check materials to make sure they're in the (hard-coded) approved list
    """
    valid_materials = { 'flower': 'Flo', 'iaa': 'IAA', 'leaf': 'Lea', \
            'root': 'Roo', 'salicylic': 'Sal', 'nacl': 'NaC', \
            'young': 'You', 't87': 'T87'}

    material1 = args['material1'].lower()
    if material1 not in valid_materials.keys():
        return
    tissue1 = valid_materials[material1]

    material2 = args['material2'].lower()
    if material2 not in valid_materials.keys():
        return
    tissue2 = valid_materials[material2]

    """
	Build the url from the base + the intended endpoint action
    Also encode the params (payload) into a dict
    """
    url = urljoin(jcvi_common.base_url(), 'ExpressionConditionComparison')
    payload = { 'tissue1': tissue1, 'tissue2': tissue2, 'change': foldchange }

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
    p = re.compile('AT[1-5MC]G[0-9]{5,5}\.[0-9]+', re.IGNORECASE)
    for result in r.json()['compare_table']:

        # check that transcript uses a valid transcript identifier
        transcript = result['elem_target_id']
        if not p.search(transcript):
            continue

        record = {
                'transcript': transcript,
                'class': 'transcript_property',
                'source_text_description': 'RT-PCR',
                'expression_comparison_record': {
                        'material1_text_description': result['elem_tissue1'],
                        'expression_value_material1': result['elem_tissue1_value'],
                        'expression_value_material1_stdev': result['elem_tissue1_value2'],
                        'material2_text_description': result['elem_tissue2'],
                        'expression_value_material2': result['elem_tissue2_value'],
                        'expression_value_material2_stdev': result['elem_tissue2_value2']
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
