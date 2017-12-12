import unittest
import os
import reportCache

class reportCacheTest(unittest.TestCase):

    def testcan_cache_list_of_characters_to_file(self):

        subject = reportCache.reportCache()

        dict = subject.getCharacters(10,0,False)

        self.assertEqual(str(type(dict)), "<class 'dict'>")

    def test_getAllCharacters(self):

        subject = reportCache.reportCache()

        list = subject.getAllCharactersList(True)

        sortedList = sorted(list, key=lambda character: character[1], reverse=True) #sort by appearances

        self.assertEqual(sortedList[0], ('Spider-Man', 3095) )

        self.assertEqual(len(sortedList), 1491)



if __name__ == '__main__':
    unittest.main()