import speech_recognition as sr
import requests
import base64

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='en-in')
            return(Query)          
        except:
            print('Please try again')
            return 0

q = takeCommand()
if q!=0:
    print(q)
    print('Requesting')
    URL = 'https://backend.craiyon.com/generate'
    r = requests.post(url=URL,json={'prompt': q})
    data = r.json()
    print(r.status_code)
    with open("image.png", "wb") as fh:
        fh.write(base64.decodebytes(data['images'][0].encode('ascii')))
        print('Done')
