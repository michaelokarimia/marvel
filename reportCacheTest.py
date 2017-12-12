import unittest
import os
import reportCache

class reportCacheTest(unittest.TestCase):

    def testcan_cache_list_of_characters_to_file(self):

        path = 'characters.json'

        if (os.path.isfile(path)):
            os.remove(path)

        subject = reportCache.reportCache()

        response = subject.getCharacters()

        self.assertEqual(response['data']['total'], 1491)

    def test_getPopularCharacters(self):

        path = 'characters.json'

        if (os.path.isfile(path)):
            os.remove(path)

        subject = reportCache.reportCache()

        popular = subject.getPopularCharacters(2, 0)

        self.assertEqual(popular, "3-D Man 12\nA-Bomb (HAS) 0")

    def test_getAllCharacters(self):

        path = 'characters.json'

        if (os.path.isfile(path)):
            os.remove(path)

        subject = reportCache.reportCache()

        list = subject.getAllCharactersList()

        print(list)

        sortedList = sorted(list, key=lambda character: character[1], reverse=True) #sort by appearances

        self.assertEqual(sortedList[0][0], 'A.I.M.')




if __name__ == '__main__':
    unittest.main()