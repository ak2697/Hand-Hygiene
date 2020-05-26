
import requests

def classify(c):

    key = "b8d95190-83e9-11ea-8b62-f980abc25a5456db862e-ce9c-4286-b7a7-943922a3560d"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"
    response = requests.post(url, json={ "data" : c })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

def test(c):
    demo = classify(c)
    label = demo["class_name"]
    confidence = demo["confidence"]
    return ("result: '%s' with %d%% confidence" % (label, confidence))