import os
import client
import json

charactersPath = 'characters.json'
popularCharactersPath = 'popularcharacters.json'

api = None

class reportCache:

    def __init__(self):

        self.api = client.Client()

    def clearCache(self):
        if os.path.isfile(charactersPath):
            os.remove(charactersPath)


    def getCharacters(self, limit=1, offset=0, fetchFromCache=True):

        if(fetchFromCache):
            if os.path.isfile(charactersPath):
                f = open(charactersPath)
                jsonstr = f.readlines()
                f.close()

                return jsonstr
            else:
                self.getCharacters(limit,offset,False)

        else:
            #no cache available so pull it from the API
            result = self.api.request('characters', limit, offset)

            jsonData = result['data']

            #write results
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
            if os.path.isfile(popularCharactersPath):
                with open(popularCharactersPath, 'r') as f:
                    for line in f:

                        lsplt = line.split('\t')

                        character = tuple((lsplt[0],int(lsplt[1].strip())))
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

            count = response['data']['count']

            results = response['data']['results']

            print('limit: {}, offset: {} total: {}\n count: {}\nresultsCount {}'.format(limit, offset, total, count, len(results)))

            for ch in results:
                print(ch['name'])
                returnList.append( (ch['name'], ch['comics']['available']))

            offset = offset + limit

        #cache results

        if os.path.isfile(popularCharactersPath):
            os.remove(popularCharactersPath)
        with open(popularCharactersPath, 'x') as f:
            for char in returnList:
                f.write('{}\t{}\n'.format(char[0], str(char[1])))

        return returnList
