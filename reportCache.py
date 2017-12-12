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

    def getPopularCharacters(self):

        response = self.getCharacters()

        data = response['data']

        results = data['results']

        returnStr = ''

        for c in results:
            returnStr = returnStr + '\n{} {}'.format(c['name'], c['comics']['returned'])

        print(returnStr)

        return returnStr