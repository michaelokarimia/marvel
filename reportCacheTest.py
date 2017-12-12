import unittest
import os
import reportCache

class reportCacheTest(unittest.TestCase):

    def test_can_cache_list_of_characters_to_file(self):

        path = 'characters.json'

        if (os.path.isfile(path)):
            os.remove(path)

        subject = reportCache.reportCache()

        response = subject.getCharacters()

        self.assertEqual(response['data']['total'], 1491)

    def test_getPopularCharacters(self):

        subject = reportCache.reportCache()

        popular = subject.getPopularCharacters()

        print(popular)

        self.assertEqual(popular, "Aaron Stack")


if __name__ == '__main__':
    unittest.main()