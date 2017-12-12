import unittest
import os
import reportCache

class reportCacheTest(unittest.TestCase):

    def testcan_cache_list_of_characters_to_file(self):

        subject = reportCache.reportCache()

        dict = subject.getCharacters(10,0,False)

        self.assertEqual(str(type(dict)), "<class 'dict'>")

    def test_getPopularCharacters(self):

        subject = reportCache.reportCache()

        popular = subject.getPopularCharacters(2, 0, False)

        self.assertEqual(popular, "3-D Man 12\nA-Bomb (HAS) 0")

    def test_getPopularCharacters_can_cache(self):

        subject = reportCache.reportCache()

        popular = subject.getPopularCharacters(2, 0, True)

        self.assertEqual(popular, "3-D Man 12\nA-Bomb (HAS) 0")


    def test_getAllCharacters(self):

        subject = reportCache.reportCache()

        list = subject.getAllCharactersList(True)

        sortedList = sorted(list, key=lambda character: character[1], reverse=True) #sort by appearances

        #print(sortedList)

        self.assertEqual(sortedList[0], ('A.I.M.',20) )

        self.assertEqual(len(sortedList), 1491)



if __name__ == '__main__':
    unittest.main()