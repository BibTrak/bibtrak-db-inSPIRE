from urllib2 import Request, urlopen, URLError

#Fetches information on the paper from the inSPIRE api.
#Params:
#	id - the record id of the paper
#
#Returns:
#	A JSON string with the author, title, collaboration and publication info, and DOI
def fetch(id):
	apiURL = "https://inspirehep.net/"
	reqStr = "record/"+id+"?of=recjson&ot=recid,authors,title,collaboration,publication_info,standard identifier&rg=1"
	request = Request(apiURL+reqStr);
	try:
		response = urlopen(request);
		paperData = response.read();
		return paperData
	except URLError as e:
		raise URLError("inSPIRE fetch command encountered URLError:"+repr(e))

def main(*args):
	print(fetch(args[0]))

	return 0
		
if __name__ == "__main__":
	import sys
	raw_args = sys.argv[1:]
	sys.exit(main(*raw_args))