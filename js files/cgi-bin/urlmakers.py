import urllib, json, Queue, math
import main
#builds the url for the query of the selected region using the square tool
def urlBoxMaker(x1, x2, y1, y2, z, port, bin_start, group_size, num_groups, histogram):

	base = "http://nanocube.govspc.att.com:"
	base = base + port
	extenstion = '/query/pos='
	base = base + extenstion
	base  = base + "<qaddr(" + str(x1) + "," + str(y1) + "," + str(z) + "),qaddr(" + str(x1) + "," + str(y2) + "," + str(z) + "),qaddr(" + str(x2) + "," + str(y2) + "," + str(z) + "),qaddr(" + str(x2) + "," + str(y1) + "," + str(z)+ ")>/@time=" + str(bin_start) + ":" + str(group_size) + ":" + str(num_groups)
	histstring = ""
	if (histogram != None):
		if (main.histogramstring == ""):
			keys = histogram.keys()
			for i in range(0, len(histogram)):
				histstring = "/" + str(keys[i]) + "=<"
				for j in range(0, len(histogram[keys[i]])):
					histstring = histstring + str(histogram[keys[i]][j])
					if (j != (len(histogram[keys[i]])-1)):
						histstring = histstring + ","	
				histstring = histstring + ">"
			main.histogramstring = histstring

	return base + main.histogramstring

################################################################################################

def urlPolygonMaker(coordList, port, timestart, timeend, histogram):

	base = "http://nanocube.govspc.att.com:"
	base = base + port
	extenstion = '/query/pos=<'
	base = base + extenstion
	for i in range(0, len(coordList)):
		if (i == len(coordList)-1):
			base = base + "qaddr(" + str(coordList[i]['x']) + "," + str(coordList[i]['y']) + "," + str(coordList[i]['level']) + ")>/@time=0:"+timestart+":"+timeend
		else:
			base = base + "qaddr(" + str(coordList[i]['x']) + "," + str(coordList[i]['y']) + "," + str(coordList[i]['level']) + "),"

	histstring = ""
	if (histogram != None):

		if (main.histogramstring == ""):
			keys = histogram.keys()

			for i in range(0, len(histogram)):
				histstring = "/" + str(keys[i]) + "=<"

				for j in range(0, len(histogram[keys[i]])):
					histstring = histstring + str(histogram[keys[i]][j])
					if (j != (len(histogram[keys[i]])-1)):
						histstring = histstring + ","	
			
				histstring = histstring + ">"

			main.histogramstring = histstring

	return base

################################################################################################
# Given x,y,z coordinates of a box, formats the url to request the JSON
def urlMaker(x, y, z, port, timestart, timeend, histogram):

	base = "http://nanocube.govspc.att.com:"
	base = base + port
	extenstion = '/query/pos='
	base = base + extenstion
	histstring = ""
	base = base + "qaddr(" + str(x) + "," + str(y) + "," + str(z) + ")" + "/@time=0:"+timestart+":"+timeend
	if (histogram != None):
		if (main.histogramstring == ""):
			keys = histogram.keys()
			for i in range(0, len(histogram)):
				histstring = "/" + str(keys[i]) + "=<"
				for j in range(0, len(histogram[keys[i]])):
					histstring = histstring + str(histogram[keys[i]][j])
					if (j != (len(histogram[keys[i]])-1)):
						histstring = histstring + ","	
				histstring = histstring + ">"
			main.histogramstring = histstring
	
	return base + main.histogramstring

################################################################################################
# Given a url, sends the request and receives the JSON file.
# Format the JSON to retreive an array of {key, val}s 
def processURL(url):
	response = urllib.urlopen(url);
	data = json.loads(response.read())
	formatteddata = data[['root'][0]]['children']
	return formatteddata
	#print type(data)
	#print formatteddata[0]['addr']
	#print formatteddata[0]['value']	