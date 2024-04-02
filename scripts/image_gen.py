import json
import requests
import time
import os
hf_token= "_____________________"


headers = {"Authorization": f"Bearer {hf_token}"}
model= "stabilityai/stable-diffusion-xl-refiner-1.0"
model= "karimbenharrak/stable-diffusion-xl-refiner-1.0-with-endpoint-handler"
API_URL = f"https://api-inference.huggingface.co/models/{model}"


def query(filename,tries=0):
    if tries == 3:
        return
    with open(filename, "rb") as f:
        data = f.read()
        
    response = requests.request("POST", API_URL, headers=headers, data=data)
    # print(response)
    
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
    else:
        print(response.content)
        query(filename, tries=tries+1)
    
        

def gen_image(url:str, uid:str= "temp"):
    basename= os.path.basename(url)
    filename= f"media/{uid}/{basename}"
    with open(filename, "wb") as f:
        f.write(requests.get(url=url).content)
        
    query(filename)

