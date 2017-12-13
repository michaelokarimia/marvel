import os
import client
import json


directory = './cache/'
charactersPath = directory+ 'characters.json'
AllCharactersPath = directory + 'allCharacters.txt'

api = None

class reportCache:

    def __init__(self):

        self.api = client.Client()

    def getAllComicsStarringCharacter(self, characterId):

        limit = 100
        offset = 0

        # no cache available so pull it from the API

        result = self.api.request('characters/{}/comics'.format(characterId), limit, offset)

        jsonData = result['data']

        return json.loads(jsonData)

    def getCharacters(self, limit=1, offset=0, fetchFromCache=True):

        if(fetchFromCache):
            if os.path.isfile(charactersPath) and os.path.exists(directory):
                with open(charactersPath) as f:
                    jsonstr = f.readlines()

                return jsonstr
            else:
                self.getCharacters(limit,offset,False)

        else:
            #no cache available so pull it from the API
            result = self.api.request('characters', limit, offset)

            jsonData = result['data']

            #write results

            if not os.path.exists(directory):
                os.makedirs(directory)

            if os.path.isfile(charactersPath):
                os.remove(charactersPath)
            with open(charactersPath, 'x') as f:
                f.write(jsonData)

            my_dict = json.loads(jsonData)

            return my_dict

    def getAllCharactersList(self, RetrieveFromCache=True):

        returnList = []

        if(RetrieveFromCache):
            # check cache before returning file
            if os.path.isfile(AllCharactersPath):
                with open(AllCharactersPath, 'r') as f:
                    for line in f:

                        lsplt = line.split('\t')

                        character = tuple((lsplt[0],lsplt[1],int(lsplt[2].strip()),
                                           lsplt[3], lsplt[4]))

                        returnList.append(character)



                return returnList
            else:
                #if there is no file with the cache, call self which will call the API and create one
                return self.getAllCharactersList(False)

        total = self.getCharacters(fetchFromCache=False)['data']['total']

        limit = 100

        offset = 0

        while(offset < total):

            response = self.getCharacters(limit, offset, fetchFromCache=False)

            results = response['data']['results']

            for ch in results:
                returnList.append( (ch['id'], ch['name'], ch['comics']['available'],
                                    ch['comics']['items'], ch['comics']['collectionURI']))

            offset = offset + limit

        #cache results

        if not os.path.exists(directory):
            os.makedirs(directory)

        if os.path.isfile(AllCharactersPath):
            os.remove(AllCharactersPath)
        with open(AllCharactersPath, 'x') as f:
            for char in returnList:
                print(char)
                f.write('{}\t{}\t{}\t{}\t{}\n'.format(char[0], char[1], str(char[2]), char[3], char[4]))

        return returnList
