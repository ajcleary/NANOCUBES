ADDING NANOCUBE ANOMALY DETECTION

Authors: 2015 Summer Interns: Matthew Lipshultz, Julien Homble, Andrew Cleary


#############################################################################

To Put Anamoly Feature into Another Client ( like GDELT ):

-copy anamoly.js, features.js, features_list.js, full_anom.js and all the new files in js folder, cgi-bin folder, and css folder into the client

Edits:( add these into the generic index.html commented out? )
-in index.html add the lines under extensions comment:
<!-- extensions -->
<script src="features.js"></script>
<script src="anomaly.js"></script>

and under in index.html: 
<link rel="stylesheet" href="css/leaflet.css"/>
<link rel="stylesheet" href="css/leaflet.draw.css"/>" 
add:
<link rel="stylesheet" href="css/bootstrap.min.css">

-add global port ( var port = "portnum" ) in main.js 

-Follow installing Run Server and Run in Browser below

#############################################################################

How To Run Server w/ CGI Scripts Locally:

-change the index.html and uncomment the features line around line 148
-download launchwin-1.0.1.6.msi from https://bitbucket.org/vinay.sajip/pylauncher/downloads
-start the server on putty using command    $ ncserve --port=<PORT#> < <DMP_FILENAME>
-open windows cmd prompt
-go to folder with index.html in it type $ python -m CGIHTTPServer  (or navigate there after)
-then look at your http://localhost:8000/ and python scripts work now

#############################################################################

How To Run In Browser:

-able to run cgi scripts
-make sure a server is running and port#
-change port # in main.js and set globals in anamoly.js to the wanted server port, time bins, and min and max level that you want to look at.
-change anomaly threshold to desired amount in anamolyDetection.py

#############################################################################
(deprecated dont install anymore)
Installing Pandas:

get python 2.7
$ setx PATH "%PATH%;C:\Python27\Scripts"
$ set https_proxy=http://one.proxy.att.com:8080
install  Microsoft Visual C++ Compiler for Python 2.7  from  https://www.microsoft.com/en-us/download/confirmation.aspx?id=44266
$ pip install pandas

#############################################################################

The Changes:

1. added new interface on the browser  ( run anomaly detection button )
2. user selects run or highlights a region timewindow and selects run
3. updated gui (added results window) to show found anomalies