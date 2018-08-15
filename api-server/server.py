from flask import Flask, jsonify
import time
app = Flask(__name__)

import os

from dotenv import load_dotenv
def start():
	if os.getenv('REQUESTS_SINCE_START'):
		f = open(".env", "r")
		lineArray = []
		for x in f:
			lineArray.append(x)
		newEnv = open(".env", "w")
		for x in lineArray:
			if 'REQUESTS_SINCE_START=' in x:
				newEnv.write('REQUESTS_SINCE_START=' + str(0) + '\n')
			else:
				newEnv.write(x)
		newEnv.close()
	else: 
		f = open(".env", "a")
		f.write("REQUESTS_SINCE_START=0")
		f.close()
	if os.getenv('REQUESTS_SINCE_INCEPTION'):
		pass
	else: 
		f = open(".env", "a")
		f.write("\nREQUESTS_SINCE_INCEPTION=0")
		f.close()		
	load_dotenv(override=True)


def getFirstRequestEver():
	if os.getenv('FIRST_REQUEST_EVER'):
		pass
	else:
		f = open(".env", "a")
		f.write("\nFIRST_REQUEST_EVER=" + str(time.time()))
		f.close()
	load_dotenv(override=True)
	return os.getenv('FIRST_REQUEST_EVER')

def getAppRunDuration():
	return time.perf_counter()

def getRequestsSinceStart():
	f = open(".env", "r")
	lineArray = []
	for x in f:
		lineArray.append(x)
	newEnv = open(".env", "w")
	for x in lineArray:
		if 'REQUESTS_SINCE_START=' in x:
			newEnv.write('REQUESTS_SINCE_START=' + str(int(x[21:]) + 1) + '\n')
		else:
			newEnv.write(x)
	newEnv.close()
	load_dotenv(override=True)
	return os.getenv('REQUESTS_SINCE_START')

def getRequestsSinceInception():
	f = open(".env", "r")
	lineArray = []
	for x in f:
		lineArray.append(x)
	newEnv = open(".env", "w")
	for x in lineArray:
		if 'REQUESTS_SINCE_INCEPTION=' in x:
			newEnv.write('REQUESTS_SINCE_INCEPTION=' + str(int(x[25:]) + 1) + '\n')
		else:
			newEnv.write(x)
	newEnv.close()
	load_dotenv(override=True)
	return os.getenv('REQUESTS_SINCE_INCEPTION')

def status():
	firstRequest = getFirstRequestEver()
	appDuration = getAppRunDuration()
	requestsStart = getRequestsSinceStart()
	requestsInception = getRequestsSinceInception()
	return jsonify(firstRequestTimeEver=firstRequest, appRunDuration=appDuration, requestsSinceStart=requestsStart,requestsSinceInception=requestsInception)

@app.route('/status')
def getStatus():
	return status()

start()