import os
import client
import json

charactersPath = 'characters.json'

api = None

class reportCache:


    def __init__(self):

        self.api = client.Client()

    def getCharacters(self):

        #check cache before returning file

        if os.path.isfile(charactersPath):
            f = open(charactersPath)
            jsonstr = f.readlines()
            f.close()

            #characterdict = json.loads(jsonstr)

            my_dict = json.loads(jsonstr[0])

            return my_dict


        else:
            #no cache available so pull it from the API
            result = self.api.request('characters')

            jsonData = result['data']

            f = open(charactersPath, 'x')

            f.write(jsonData)

            f.close()

            my_dict = json.loads(jsonData)

            return my_dict
