from fastapi import FastAPI
import wget
import time
import os

app = FastAPI()

count = 0;


@app.get("/")
def root():
    global count;
    return {"Total Number of Download: " + str(count)}

@app.get("/start1")
def start1():
    download();
    return {"start 2"}

@app.get("/start")
def download():
    while 1:
        wget.download(
            'http://fileupload.arpudhacloud.tk/download.php?id=1&token=fcoZgcU1hmtb8FfLAxYBRVT3tE1Hctqc&download')
        print("sleeping for 5 sec")
        time.sleep(5)
        print("deleting a file")
        os.remove("100MB.bin")
        print("file deleted")
        print("sleeping for 5 sec")
        time.sleep(5)
        global count;
        count = count + 1;
    return {"Download completed"}

