import os
import client
import json

charactersPath = 'characters.json'

api = None

class reportCache:


    def __init__(self):

        self.api = client.Client()

    def getCharacters(self, limit=1, offset=0):

        #check cache before returning file

        if os.path.isfile(charactersPath):
            f = open(charactersPath)
            jsonstr = f.readlines()
            f.close()

            my_dict = json.loads(jsonstr[0])

            return my_dict


        else:
            #no cache available so pull it from the API
            result = self.api.request('characters', limit, offset)

            jsonData = result['data']

            f = open(charactersPath, 'x')

            f.write(jsonData)

            f.close()

            my_dict = json.loads(jsonData)

            return my_dict

    def getPopularCharacters(self, limit, offset):

        response = self.getCharacters(limit, offset)

        data = response['data']

        results = data['results']

        returnStr = ''

        for c in results:
            returnStr = returnStr + '{} {}\n'.format(c['name'], c['comics']['returned'])

        return returnStr.strip()

    def getAllCharactersList(self):
        dict = {'key': 'value'}

        #flush cache

        if os.path.isfile(charactersPath):
            os.remove(charactersPath)

        limit = 100

        offset = 0

        response = self.getCharacters(limit, offset)

        total = response['data']['total']

        count = response['data']['count']


        results = response['data']['results']

        print('total: {}\n count: {}\nresultsCount {}'.format(total, count, len(results)))

        mylist = []

        for ch in results:
            mylist.append( (ch['name'], ch['comics']['returned']))


        return mylist
