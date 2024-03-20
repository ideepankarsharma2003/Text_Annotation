import json
import requests
import time


headers = {"Authorization": f"Bearer {HF_API_KEY}"}
API_URL = "https://api-inference.huggingface.co/models/dslim/bert-large-NER"



def query(payload, tries=0):
    if tries==3:
        return []
    response = requests.post(API_URL, headers=headers, json=payload)
    response= response.json()
    try:
        if type(response)!=type([1, 2]):
            raise Exception('Faulty Response')
    except:
        print(f"""
              [Try ({tries+1}): Model is Loading, Going for Sleep of 20 seconds]
              """)
        time.sleep(20)
        response= query(payload=payload, tries=tries+1)
        
    finally:
        return response
        


def get_ner_results(text:str):
    payload= {
        "inputs": text
    }
    
    ner_results= query(payload=payload)
    return ner_results