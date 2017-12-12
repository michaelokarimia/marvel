import unittest
import reportCache


class ReportCacheTest(unittest.TestCase):

    def test_can_cache_list_of_characters_to_file(self):

        subject = reportCache.reportCache()

        dict = subject.getCharacters(10,0,False)

        self.assertEqual(str(type(dict)), "<class 'dict'>")

    def test_getAllCharacters(self):

        subject = reportCache.reportCache()

        list = subject.getAllCharactersList(True)

        self.assertEqual(len(list), 1491)



if __name__ == '__main__':
    unittest.main()