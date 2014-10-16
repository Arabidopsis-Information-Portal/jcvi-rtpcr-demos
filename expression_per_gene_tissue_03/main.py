import json
import requests
import re

def fail(message):
     # This is a simple failure message generator for generic ADAMA adapters
     # It will eventually be replaced with a system-wide fail function
     return 'text/plaintext; charset=ISO-8859-1', message
     
def search(arg):

# arg contains a dict with two key:values
#
# transcript is gene identifier
# format is the data format for return

	# In the future, ADAMA will check a query, map_*, or generic request against a list of mandatory
	# parameters specified for each service. For now, if we want to enforce that behavior we need to 
	# implement it ourselves. 
    if not (('transcript' in arg) and ('format' in arg)):
        return fail('Both transcript and format are required parameters')
        
	# Check that client has requested what looks like a valid transcript identifier    
	# ADAMA will have a graceful, cross-language exception handling scheme in a future release
	# At present, we are hand-coding a fail(message) routine in the adapter. See above.
    trans = arg['transcript']
    trans = trans.upper()
    
    p = re.compile('AT[1-5MC]G[0-9]{5,5}\.[0-9]+', re.IGNORECASE)
    if not p.search(trans):
        return fail('Please specify a valid AGI transcript identifier')
            
	# We want to support HTML or JSON but exclude text because what the service returns actually 
	# isn't CSV but pre-formatted HTML containing CSV
	# ADAMA will have a graceful, cross-language exception handling scheme in a future release
	# At present, we are hand-coding a fail(message) routine in the adapter. See above.
    fmt = arg['format']
    fmt = fmt.lower()
    if not fmt in ['html', 'json']:
        return fail('Supported formats are HTML and JSON')
    
	# We can also use the params function of requests but I was lazy here
    url = 'http://www.jcvi.org/cgi-bin/arabidopsis/qpcr/ExpressionPerGenePerTissue?Submit=Search&format=' + fmt + '&gene=' + trans
    r = requests.get(url)
    
	# Here's a new bit of error handling, unique to the generic type
    if r.ok:
		# If we get a 200 status from the remote GET, we inspect the returned Content-Type header and send
		# that back along with the content of the HTTP response. If we want to over-ride that
		# content type for some reason, we simply return a string with the appropriate MIME type
        return r.headers['Content-Type'],r.content
    else:
		# If there was an error of some kind, we try valiantly to grab any error text from the
		# remote service and return it to the client. Again, in the future ADAMA will have graceful error
		# reporting but we are waiting till we've seen a few error cases to implement it
        fail(r.text)

def list(arg):
	# We don't have a valid operation for the /list endpoint. At present, just return a nasty
	# looking stack trace from within ADAMA. At least the end client will know they did something bad
    pass
