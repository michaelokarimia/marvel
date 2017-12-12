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

        path = 'characters.json'

        if (os.path.isfile(path)):
            os.remove(path)

        subject = reportCache.reportCache()

        popular = subject.getPopularCharacters(2, 0)

        print(popular)

        self.assertEqual(popular, "3-D Man 12\nA-Bomb (HAS) 0")


if __name__ == '__main__':
    unittest.main()