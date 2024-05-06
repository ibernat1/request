import requests
import json
import time
import subprocess
import platform
import re
from datetime import datetime

def handleRequest(URL): 
    log = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} "
    start_time = time.time()
    response = requests.get(URL)
    end_time = time.time()
    log += f"czas wykonywania: {end_time-start_time}"
    log += validateResponse(response)
    saveToFile(log)
    print(log)

def validateResponse(response):
    if response.status_code == 200 :
        log = "http status code: 200 "
    else:
        log = f"http status code: {response.status_code}"
    if response.headers.get("Content-Type") == "application/vnd.orangeott.v1+json":
        log +=  "content type: json "
        log += validateJson(response.content)
    else: 
        log +=  f"content type: {response.headers.get('Content-Type')} "
    return log
    
def validateJson(text):
    try:
        json_object = json.loads(text)
    except ValueError as e:
        return "is not valid "
    return "is valid"
        
def saveToFile(text):
    f = open("log.txt", "a")
    f.write(text + "\n")
    f.close()

if __name__ == "__main__":
    URL = "https://tvgo.orange.pl/gpapi/status"
    X = 10
    Y = 5
    for x in range (0,X):
        start = time.time()
        handleRequest(URL)
        time.sleep(Y)