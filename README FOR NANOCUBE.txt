NANOCUBE ANOMALY DETECTION ALGORITHM, PUTTING IT IN THE BROWSER, STEPS AND LOG

Authors: 2015 Summer Interns: Matthew Lipshultz, Julien Homble, Andrew Cleary







Idea:
1. a new interface on the browser  ( run anomaly detection button )
2. user selects run or highlights a region and selects run
3. send (query / run command ??) to server
4. server runs algorithm and sends results back
5. update gui (added results window) to show results

Installing Pandas:
get python 2.7
setx PATH "%PATH%;C:\Python27\Scripts"
set https_proxy=http://one.proxy.att.com:8080
install  Microsoft Visual C++ Compiler for Python 2.7  from  https://www.microsoft.com/en-us/download/confirmation.aspx?id=44266
pip install pandas

To Run Server w/ CGI Scripts:
change the index.html and uncomment the features line around line 148
download launchwin-1.0.1.6.msi from https://bitbucket.org/vinay.sajip/pylauncher/downloads
start the server on putty using command    ncserve --port=<PORT#> < <DMP_FILENAME>
open windows cmd prompt
in your index folder type python -m CGIHTTPServer  (or navigate there after)
then look at your http://localhost:8000/ and python scripts work hopefully 

To Run In Browser-
able to run cgi scripts
change port # and time window in features.js global variable to the wanted server port and time bins you want to consider

.