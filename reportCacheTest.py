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

        data = response['data']

        total = data['total']



        # js['data']['results'][0]['comics']['returned']

        self.assertEqual(total, 1491)


if __name__ == '__main__':
    unittest.main()