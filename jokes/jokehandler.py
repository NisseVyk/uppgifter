import requests
import datetime


class Jokehandler:

    def __init__(self, adress):
        self.adress = adress


    def get_joke(self):
        req = requests.get(self.adress)
        json_data = req.json()
        joke = json_data['joke']

        nu = datetime.datetime.now
        print(f"Metod getJoke körs tid: {nu}")

        return joke
    
